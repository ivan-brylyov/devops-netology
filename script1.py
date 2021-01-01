#!/usr/bin/env python3

import os
import sys

bash_command = ["git status"];
if len(sys.argv) > 1:
    bash_command.insert(0, "cd " + sys.argv[1])

result_os = os.popen(' && '.join(bash_command)).read()
modified = False
# print(result_os) #Вывод всего текста git status
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        modified = True
        prepare_result = result.replace('\tmodified:   ', '')
        print(sys.argv[1], '/',  prepare_result, sep='')

if not modified:
    print("not modified")