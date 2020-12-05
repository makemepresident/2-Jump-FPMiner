class TwoJump:
    index_to_char_map = {0: 'a', 1: 'c', 2: 'g', 3: 't'}
    char_to_index_map = {i: j for j, i in index_to_char_map.items()} # reversed char dictionary

    def __init__(self, input_data):
        self.input_data = input_data

    def gen_index_table(self):
        index_table = [[] for i in range(4)] # where index 0 = 'a', 1 = 'c', ...
        for index, value in enumerate(self.input_data):
            index_table[self.char_to_index_map.get(value)].append(index)
        return index_table        

    def match_pattern(self, pattern):
        #If no pattern is supplied return default value
        if(pattern == ''):
            return [0, 0, []]

        #Initialize values
        input_length = len(self.input_data)
        pattern_length = len(pattern)
        first_letter = pattern[0]
        compare, counter, matches = 0, 0, []
        index_table = self.gen_index_table()
        is_odd = pattern_length % 2 == 1

        #Iterate through indices that match the first char of the pattern
        for i in index_table[self.char_to_index_map.get(first_letter)]:
            #Reset the flag each iteration
            flag = True

            #Iterate through the chars of the pattern by twos
            for j in range(0, pattern_length - 1, 2):
                #If pattern is larger than the remaining substring, set flag to false and break
                if i + pattern_length > input_length:
                    flag = False
                    break

                #Create unique sums of two chars, and compare them.
                input_two = self.input_data[i + j] + self.input_data[i + j + 1] * 10
                pattern_two = pattern[j] + pattern[j + 1] * 10
                compare += 1
                if input_two != pattern_two:
                    flag = False
                    break
                else:
                    compare += 1
            
            #If flag is still true, a match has been found. Add to count and save the index.
            if flag:
                if is_odd and self.input_data[i + pattern_length - 1] != pattern[pattern_length - 1]:
                    continue
                counter += 1
                matches.append(i)
        return [counter, compare, matches]