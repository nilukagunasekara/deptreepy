import sys
from trees import *
from patterns import *

help_message = (
"""
usage:

   python3 deptreepy.py <command> <arg>*

The command-arg combinations are

   match_wordlines '<pattern>'
   match_subtrees '<pattern>'

They read CoNLL-U content from std-in, for example, with '<eng-ud.conllu¨

The following patterns match both wordlines and trees, depending on the command:

   FORM  <strpatt>
   LEMMA <strpatt>
   POS   <strpatt>
   FEATS <strpatt>
   DEPREL <strpatt>
   HEAD_DISTANCE <inpred>
   AND <pattern>*
   OR  <pattern>*
   NOT <pattern>*

These patterns match trees:

   LENGTH <intpred>
   DEPTH <intpred>
   TREE <pattern> <pattern>*
   HAS_SUBTREE <pattern>*

The auxialiary concepts are:

   <strpatt>, a string with (*) matching one or more characters (like Unix filenames)
   <intpred>, one of =n, <n, >n, !n, giving a comparison to number n (which can be negative)

"""
)

if __name__ == '__main__':
    if not sys.argv[1:]:
        print(help_message)
    else:
      match sys.argv[1]:
        case 'match_wordlines':
            pattern = parse_pattern(sys.argv[2])
            print('#', pattern)
            match_wordlines(pattern, sys.stdin)
        case 'match_subtrees':
            pattern = parse_pattern(sys.argv[2])
            print('#', pattern)
            match_subtrees(pattern, sys.stdin)
        case 'help' | _:
            print(help_message)
            
