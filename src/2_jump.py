import random # testing only

n = 20 # test_data length (hardcoded for testing)
m = 4 # pattern length (hardcoded for testing)

chars = {0: 'a', 1: 'c', 2: 'g', 3: 't'}
inv_chars = {i: j for j, i in chars.items()} # reversed char dictionary
# random.seed(435377) # commented out to test different values
#test_data = [chars.get(random.randrange(0, 4)) for x in range(random.randint(20, 50))]
#test_pattern = [chars.get(random.randrange(0, 4)) for x in range(4)]
test_data = ['c', 't', 'c', 'a', 't', 't', 'g', 'g', 'a', 'a', 'c', 'a', 't', 't', 'g', 'a', 't', 't', 'g', 'a', 't', 't', 'g', 'g', 'g', 'a', 't', 't', 'g', 'a', 't', 't', 'g']
test_pattern = ['a', 't', 't', 'g']

# for when test data is removed
input_data = test_data
pattern = test_pattern
# n = len(input_data)
# m = len(pattern)

def gen_index_table():
    # Generate index table based on page 6 of the reference paper
    index_table = [[] for i in range(4)] # where index 0 = 'a', 1 = 'c', ...
    for index, value in enumerate(test_data):
        index_table[inv_chars.get(value)].append(index)
    return index_table

def two_jump():
    firstLet = pattern[0] # 'a' in this case
    i, j, start_index, compare, counter = 0, 0, 0, 0, 0
    flag = True
    index_table = gen_index_table()
    start_index = index_table[inv_chars.get(firstLet)][i] # 1 in this case
    while n - start_index > m:
        while j < m:
            if m - j == 1:
                if input_data[start_index + j] != pattern[j]:
                    compare += 1
                    flag = False
                    break
            input_two = input_data[start_index + j] + input_data[start_index + j + 1]
            pattern_two = pattern[j] + pattern[j + 1]
            compare += 1
            if input_two != pattern_two:
                flag = False
                break
            else:
                compare += 1
            if input_data[start_index + j] != pattern[j] or input_data[start_index + j + 1] != pattern[j + 1]:
                flag = False
                break
            if flag is True:
                counter += 1
            else:
                flag = True
                j = 0
            i += 1
            start_index = index_table[inv_chars.get(firstLet)][i]
    return [compare, counter]

def not_shit_two_jump():
    firstLet = pattern[0] # 'a' in this case
    compare, counter = 0, 0
    flag = True
    index_table = gen_index_table()
    matches = []
    is_odd = m%2 == 1

    pattern_length = len(pattern)
    input_length = len(input_data)

    for i in index_table[inv_chars.get(firstLet)]: # [2,3,4]
        flag = True
        for j in range(0, pattern_length - 1, 2): # 0, 2
            # if m - j == 1:
            #     if input_data[i + j] != pattern[j]:
            #         compare += 1
            #         flag = False
            #         break
            if i + j >= input_length-1:
                flag = False
                break
            input_two = input_data[i + j] + input_data[i + j + 1]*10 # []
            pattern_two = pattern[j] + pattern[j + 1]*10
            compare += 1
            if input_two != pattern_two:
                flag = False
                break
            else:
                compare += 1
        
        if flag:
            if is_odd and input_data[i + pattern_length-1] != pattern[pattern_length-1]:
                continue

            counter += 1
            matches.append(i)

    return [compare, counter, matches]

print(input_data) # randomly generated DNA sequence
print(pattern) # predefined pattern to match
result = not_shit_two_jump()
print(str(result[0]) + ' comparisons')
print(str(result[1]) + ' counts')
print('Indices: ' + str(result[2]))