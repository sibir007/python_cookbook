from socket import socket, AF_INET, SOCK_DGRAM


def call_udp_claint(adr):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.sendto(b'', adr)
    resp = sock.recvfrom(8132)
    print(resp)


if __name__ == '__main__':
    call_udp_claint(('localhost', 20000))
