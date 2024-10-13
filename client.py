import socket
from base_logger import getlogger
from bs4 import BeautifulSoup  # use later


# how do we know when the data is complete?
# how do we check if the connection is broken in the middle?


class ClientSocket:

    def __init__(self) -> None:
        self.LOGGER = getlogger("client")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def get(self, url: str):
        self.LOGGER.info(f"GET request to {url}")
        get_string = f"""GET / HTTP/1.1 \r\n
                    Host: {url} \r\n
                    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) \r\n
                    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp \r\n
                    Connection: close \r\n"""

        print(len(get_string.encode()))
        self.sock.connect(("google.com", 80))
        self.sock.sendall(get_string.encode())

        response = b""
        while True:
            buf = self.sock.recv(4096)
            if not buf:
                break
            response += buf

        r = response.decode()
        print(r.splitlines()[0])  # just the status code

    def post(self):
        pass

    def put(self):
        pass


c = ClientSocket()
c.get("google.com")
