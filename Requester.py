from socket import *

HOST = "www.ryomyong.com"
PORT = 80
CRLF = "\r\n"

bypassSocket = socket(AF_INET, SOCK_STREAM)
bypassSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
bypassSocket.connect((HOST, PORT))

packet = []
packet.append("GET / HTTP/1.1%s" % (CRLF))
packet.append("User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64)%s" % (CRLF))
packet.append("HOST: %s%s%s" % (HOST, CRLF, CRLF))

bypassSocket.send(''.join(packet))
print bypassSocket.recv(102400)
bypassSocket.close()