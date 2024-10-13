import socket
import time


class HttpServer:
    def __init__(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("localhost", 8090))

    def listen(self):
        print("listening...")
        self.server.listen(5)
        while True:
            (clientsocket, addr) = self.server.accept()
            print(clientsocket)
            print(addr)

            buf = clientsocket.recv(4096)

            if len(buf) > 0:
                self._parse(buf.decode(), clientsocket)

    # NOTE: to terminate the connection we need to first accept it and then pass it on to the session socket

    def _parse(self, msg, clientsock):
        # will parse the message and return a response
        # for simplicity each line of the request ends with /n

        l = msg.split("\n", maxsplit=2)  # headers, host, content

        request_type = l[0]
        request_host = l[1]
        request_content = l[2]

        time.sleep(5)  # to define timeout
        if request_type.startswith("GET"):
            print("sending...")
            clientsock.send("200".encode())


s = HttpServer()
s.listen()
