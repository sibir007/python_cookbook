import time
from socket import socket, AF_INET, SOCK_DGRAM


def time_servet(adr):
    serv = socket(AF_INET, SOCK_DGRAM)
    serv.bind(adr)
    while True:
        msg, adr = serv.recvfrom(8132)
        print(f'Got connection from {adr}')
        resp = time.ctime()
        serv.sendto(resp.encode('ascii'), adr)


if __name__ == '__main__':
    time_servet(('', 20000))
