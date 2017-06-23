from __future__ import print_function
import os, re

class Exim():

    def scan(self):

        queue = os.popen('exim -bp')
        user_count = {}

        for line in queue:
            if len(line) <= 1:
                pass
            else:
                if re.match(r'^\d', line.split()[0]):
                    pass
                else:
                    if line.split()[0] in user_count:
                        user_count[line.split()[0]] += 1
                    else:
                        user_count[line.split()[0]] = 1
        for k, v in user_count.items():
            print(v, k)
