import os, re, socket

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
