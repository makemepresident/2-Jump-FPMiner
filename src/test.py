import sys
import re
import TwoJump
import time

from TwoJump import TwoJump

def init_input(filename):
    input_data = []
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

    expression = re.compile('[acgt]*')
    output = ''
    for i in input_data:
        if(re.fullmatch(expression, i) != None):
            output += i
    
    return output

if __name__ == '__main__':
    
    input_data = ''

    if(len(sys.argv) > 1):
        input_data = init_input(sys.argv[1])

    two_jump = TwoJump(input_data)

    start0 = time.perf_counter()
    for i in range(0, 1000):
        result0 = two_jump.match_pattern_no_op('act')
    stop0 = time.perf_counter()

    startb = time.perf_counter()
    for i in range(0, 1000):
        resultb = two_jump.match_pattern_chars('act')
    stopb = time.perf_counter()

    start1 = time.perf_counter()
    for i in range(0, 1000):
        result1 = two_jump.match_pattern('act')
    stop1 = time.perf_counter()

    start2 = time.perf_counter()
    for i in range(0, 1000):
        result2 = two_jump.match_pattern_2('act')
    stop2 = time.perf_counter()

    print("Two-Jump (no optimization): count = " + str(result0[0]))
    print("Two-Jump (no optimization): comparisons = " + str(result0[1]))
    #print("Two-Jump: indices = " + str(result1[2]))
    print("Two-Jump (no optimization): avg time (1000 runs) = " + str((stop0-start0)/1000))

    print("-----------------------------------------------")

    print("Two-Jump (optimized): count = " + str(result1[0]))
    print("Two-Jump (optimized): comparisons = " + str(result1[1]))
    #print("Two-Jump: indices = " + str(result1[2]))
    print("Two-Jump (optimized): avg time (1000 runs) = " + str((stop1-start1)/1000))

    print("-----------------------------------------------")

    print("Two-Jump (char comparison): count = " + str(resultb[0]))
    print("Two-Jump (char comparison): comparisons = " + str(resultb[1]))
    #print("Two-Jump: indices = " + str(result1[2]))
    print("Two-Jump (char comparison): avg time (1000 runs) = " + str((stopb-startb)/1000))

    print("-----------------------------------------------")

    print("Standard Index Search: count = " + str(result2[0]))
    print("Standard Index Search: comparisons = " + str(result2[1]))
    #print("2: indices = " + str(result2[2]))
    print("Standard Index Search: avg time (1000 runs) = " + str((stop2-start2)/1000))
