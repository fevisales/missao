#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    fst_param = sys.argv[1]
    parameters = sys.argv[2]

    pattern = r'\b' + re.escape(fst_param) + r'\b'

    found = re.findall(pattern, parameters)
    
    count = len(found)
    
    if count == 0:

        print("none")
    else:
        print(count)
