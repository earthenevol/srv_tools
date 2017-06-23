import os, subprocess, re

class Data():

    def backup(self, target):
        home_dir = os.path.expanduser('~')

        if target == 'sites':
            subprocess.Popen(['tar', '-cvzf', 'public_html.tar.gz', '-C', home_dir, 'public_html'])
        if target == 'mail':
            subprocess.Popen(['tar', '-cvzf', 'mail.tar.gz', '-C', home_dir, 'mail'])
        if target == 'home':
            subprocess.Popen(['tar', '-cvzf', os.environ.get('USER') + '.tar.gz', '-C', home_dir, '.'])

    def scan(self, user):
        homedir = os.path.expanduser('~' + user)
        rex = re.compile(r'\@\$GLOBALS.\d*continue|FbU73jxn|edE0lF')
        files = os.walk(homedir, topdown=True)
        excluded_dirs = set(['performance'])
        for pa, dirs, fil in files:
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            for fi in fil:
                #print(open(pa + '/' + fi))
                op = open(pa + '/' + fi).read()
                res = rex.search(op)
                if res:
                    print('File {0} is infected'.format(pa + '/' + fi))

    def testing(self, user):
        file_check = open('/root/testing.txt').read()
        rex = re.compile(r'\@\$GLOBALS.\d*continue')
        result = rex.search(file_check)
        if result:
            print(result.group(0))
