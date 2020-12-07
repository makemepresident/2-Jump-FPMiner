input_data = ['c', 't', 'c', 'a', 't', 't', 'g', 'g', 'a', 'a', 'c', 'a', 't', 't', 'g', 'a', 't', 't', 'g', 'a', 't', 't', 'g', 'g', 'g', 'a', 't', 't', 'g', 'a', 't', 't', 'g']
pattern = ['a', 't', 't', 'g']
chars = {0: 'a', 1: 'c', 2: 'g', 3: 't'}
inv_chars = {i: j for j, i in chars.items()} # reversed char dictionary
m = len(input_data)
n = len(pattern)

def gen_index_table():
    # Generate index table based on page 6 of the reference paper
    index_table = [[] for i in range(4)] # where index 0 = 'a', 1 = 'c', ...
    for index, value in enumerate(input_data):
        index_table[inv_chars.get(value)].append(index)
    return index_table

def two_jump():
    firstLet = pattern[0] # Grab first character of the input pattern
    i, j, start_index, compare, counter = 0, 0, 0, 0, 0
    flag = True
    index_table = gen_index_table() # Generate index table
    start_index = index_table[inv_chars.get(firstLet)][i] # Get first index
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