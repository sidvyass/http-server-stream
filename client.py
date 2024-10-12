import socket


class ClientSocket:
    def __init__(self) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(("localhost", 8090))

    def sendmsg(self):
        print("sending...")
        s = "GET / HTTP /1.1 \n Host: localhost \n Content: Hello world! \n how are you"
        self.sock.send(s.encode())

        print("waiting for reply...")
        buf = self.sock.recv(2048)

        if len(buf) > 0:
            print(buf.decode())


c = ClientSocket()
c.sendmsg()
