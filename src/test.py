import TwoJump

from TwoJump import *

two_jump = TwoJump('actactactggact')
result = two_jump.match_pattern("act")

for i in result:
    print(str(i))