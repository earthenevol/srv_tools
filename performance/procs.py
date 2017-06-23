from __future__ import print_function
import os

class Procs():

    def processes(self):

        current_processes = os.popen('ps faux')
        bad_users = ('root', 'apache', 'exim', 'dovecot', 'named', 'dbus', 'nscd', 'mysql', 'ntp', 'dovenull', 'mailnull')

        for proc in current_processes:
            if proc.split()[0] not in bad_users:
                print(proc, end='')
