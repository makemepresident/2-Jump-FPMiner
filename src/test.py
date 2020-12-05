import TwoJump

from TwoJump import *

two_jump = TwoJump(['A', 'C', 'T', 'A', 'C', 'T', 'A', 'C', 'T', 'G', 'G', 'A', 'C', 'T'])
result = two_jump.match_pattern(['A', 'C', 'T'])

for i in result:
    print(str(i))