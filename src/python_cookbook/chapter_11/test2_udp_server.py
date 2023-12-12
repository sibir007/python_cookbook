from socketserver import ThreadingUDPServer, BaseRequestHandler
import time


class TimeUdpHandler(BaseRequestHandler):
    def handle(self):
        print(f'Got connection {self.client_address}')
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


if __name__ == '__main__':
    serv = ThreadingUDPServer(('', 20000), TimeUdpHandler)
    serv.serve_forever()
