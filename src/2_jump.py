import random
import sys

input_data = []
pattern = None
m = None
n = None
chars = {0: 'a', 1: 'c', 2: 'g', 3: 't'}
inv_chars = {i: j for j, i in chars.items()} # reversed char dictionary

def init_input(filename):
    global input_data
    for i in range(2):
        try:
            reader = open(filename)
            for line in reader:
                line_arr = line.split(' ')
                for index, substring in enumerate(line_arr):
                    if index == 0:
                        continue
                    char_arr = list(substring)
                    if char_arr[len(char_arr) - 1] == '\n':
                        char_arr.pop()
                    input_data += char_arr
            print('File parsed correctly...')
            break
        except FileNotFoundError:
            print('File not found, please verify the path and try again')
            if i == 0:
                if '\\' in filename:
                    filename = '../data/' + filename[filename.index('\\') + 1:len(filename) - 1]
                else:
                    filename = '../data/' + filename
                continue
            sys.exit()
        except IndexError:
            print('Problem parsing the input file, check guidelines to ensure proper form')
            sys.exit()

if len(sys.argv) < 2:
    # No data file input was supplied
    # No pattern was supplied
    input_data = [chars.get(random.randint(0, 3)) for x in range(100, 300)]
    pattern = [chars.get(random.randint(0, 3)) for x in range(3, 8)]
elif len(sys.argv) < 3:
    # Data file supplied
    # No pattern supplied
    pattern = [chars.get(random.randint(0, 3)) for x in range(3, 8)]
    init_input(sys.argv[1])
elif len(sys.argv) < 4:
    # Data file supplied
    # Pattern supplied
    pattern = [x.strip() for x in sys.argv[2].split(',')]
    init_input(sys.argv[1])
else:
    # Arguments wrong and exit()
    print('Too many arguments, check guidelines for more info')
    sys.exit()

def gen_index_table():
    global input_data
    index_table = [[] for i in range(4)] # where index 0 = 'a', 1 = 'c', ...
    for index, value in enumerate(input_data):
        index_table[inv_chars.get(value)].append(index)
    return index_table

def two_jump():
    global input_data
    global pattern
    global chars
    global inv_chars
    input_length = len(input_data)
    pattern_length = len(pattern)
    firstLet = pattern[0]
    compare, counter, matches = 0, 0, []
    flag = True
    index_table = gen_index_table()
    is_odd = pattern_length % 2 == 1
    try:
        for i in index_table[inv_chars.get(firstLet)]:
            flag = True
            for j in range(0, pattern_length - 1, 2):
                if i + j >= input_length-1:
                    flag = False
                    break
                input_two = input_data[i + j] + input_data[i + j + 1] * 10
                pattern_two = pattern[j] + pattern[j + 1] * 10
                compare += 1
                if input_two != pattern_two:
                    flag = False
                    break
                else:
                    compare += 1
            if flag:
                if is_odd and input_data[i + pattern_length - 1] != pattern[pattern_length - 1]:
                    continue
                counter += 1
                matches.append(i)
        return [compare, counter, matches]
    except TypeError:
        print('Problem with input pattern, check the guidelines for more information')
        sys.exit()

result = two_jump()
print('Comparisons: ' + str(result[0]))
print('Counts: ' + str(result[1]))
print('Matching Indices: ' + str(result[2]))