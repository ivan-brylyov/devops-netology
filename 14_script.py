#!/usr/bin/env python3

import os
import sys
import Path

mypath = Path().absolute()
print('catalog: ', mypath)

bash_command = ["git status"];
if len(sys.argv) > 1:
    bash_command.insert(0, "cd " + mypath)
result_os = os.popen(' && '.join(bash_command)).read()
modified = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        modified = True
        prepare_result = result.replace('\tmodified:   ', '')
        print(mypath, '/',  prepare_result, sep='')
if not modified:
    print("not modified")