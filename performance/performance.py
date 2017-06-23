from __future__ import print_function
import os, sys, re, socket, subprocess


class Scans():

    class Procs():

        def processes(self):

            current_processes = os.popen('ps faux')
            bad_users = ('root', 'apache', 'exim', 'dovecot', 'named', 'dbus', 'nscd', 'mysql', 'ntp', 'dovenull', 'mailnull')

            for proc in current_processes:
                if proc.split()[0] not in bad_users:
                    print(proc, end='')


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


    class Network():

        def connects(self):

            connections = os.popen('ss -tuna')
            localhosts = re.compile('::1:\d+|127.0.0.1:\d+|\*:')

            for conn in connections:
                if re.match(localhosts, conn.split()[4]):
                    pass
                else:
                    print(conn.split())

        def ports(self):

            try:
                for port in range(1, 65535):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex(('198.1.108.68', port))
                    if result == 0:
                        print('Port {0} is open on 198.1.108.68'.format(port))
                    sock.close()

            except socket.error as er:
                print('Oops, something failed with connecting to', er)

    class Data():

        def backup(self):

            home_dir = os.path.expanduser('~')
            target = raw_input('What would you like to backup? ')
            if target == 'sites':
                subprocess.Popen(['tar', '-cvzf', 'public_html.tar.gz', '-C', home_dir, 'public_html'])
            if target == 'mail':
                subprocess.Popen(['tar', '-cvzf', 'mail.tar.gz', '-C', home_dir, 'mail'])
            if target == 'home':
                subprocess.Popen(['tar', '-cvzf', os.environ.get('USER') + '.tar.gz', '-C', home_dir, '.'])









