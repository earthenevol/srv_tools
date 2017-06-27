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
        rex = re.compile(r'\@\$GLOBALS.\d*continue|FbU73jxn|edE0lF|GLOBALS.*x61|edE0lF|IGlmICgg|"1\.sh"|GLOBALS.*ieetj84|rBOxlFeDa|rWmpisiBWQ|na20571|eval.*q272748|GET.*ineedthispage|x77.x69.x76|rWmyiJg3T|hacked\ by|eNqdWPtv|vd56b6998|filesman|Googleman|YYKJKaSZ.*\$_POST.*ppeRDsIfDuUi|5ebfbb39|c99shell|bar\/index|client.*x05.x01|POST.*do.*brut|img.*empty.*referrer|AtOPvMzpDq|5UpbRhpW|Qb08tTv2|ko0l|eval.stripslashes.array_pop\(\$_POST|www.*_POST.*yt.*ad.e|QGluaV9|doctoregpg|AnonGhost|AJVkA2M4om|an9dcW1i|PCT4BA6OD|aXNfdXBsb|zZ3HjuNg|E7DsuED2|DarkCrewFriends|zaprosname|HZBL02N|edoced|ZXZhbChiY|7X17f9rG|JGNtZD1i|7b35f9pV0|x7f.x45.x4c|ZXZhbChzd|snatveyz|x65.x76.x61|\@\$_COOKIE.*\$_COOKIE.*\$_COOKIE.*\$_COOKIE|testa.*veio|ezenmedia|19ca14e7ea63|php\ \ \ \ \ \ \ \ .*\$|shakeboomb|js.jquery.min.php|chr.*chr.*chr.*\..*\..*eval|error.*hexToStr.*strlen.*hexdec|GLOBALS.*Array.base64_decode.*function|rot13\(.riny|\*\/extract\(\$_COOKIE|5pJQhrPh|x33JlcG|7a3cb9bdfa|magmi_exploit|9091968376|\$_0=|\$joebbceb|NzcoJHVybCk7aWYo|zu1\&ULb\^NDtdc|Jx5tyfcGPCJrv8wS|Fr83LNbXERFycCdjxt|r3\^U6LXQgh|T7GPRXekUwTOFbI80|aWYobWQ1KCRfQ09PS0lFW|AuDnhyQaYMz|Vm5dgnDqIbaMVl|YagOK6t1bXQHYVPp|JiLebW7l9qf0|iepplewdpd|edtodsodub|GCx0eRz0XcPuXrXcKK|XN4uS8LvAiXwRhf5xq|2OuljEmswYF6ZRGtMc|q6DP2xJQlrqFBjpyHvE|J487nmIhJmg9C3KhX3R3Kbb|JElJSUlJSUlJSTFJMT0n|eotcegdlqc')
        files = os.walk(homedir, topdown=True)
        excluded_dirs = set(['performance'])
        for pa, dirs, fil in files:
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            for fi in fil:
                file_size = os.path.getsize(pa + '/' + fi)
                if file_size > 100000000:
                    print('skipping file {0} because it is {1} bytes in size'.format(pa + '/' + fi, file_size))
                    continue
                with open(pa + '/' + fi) as op:
                    for line in op:
                        res = rex.search(line)
                        if res:
                            print('File {0} is infected, string found is {1}'.format(pa + '/' + fi, res.group(0)))

    def testing(self, user):
        file_check = open('/root/testing.txt').read()
        rex = re.compile(r'\@\$GLOBALS.\d*continue')
        result = rex.search(file_check)
        if result:
            print(result.group(0))
