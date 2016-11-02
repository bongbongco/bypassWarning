from socket import *

HOST = "www.ryomyong.com"
PORT = 80
CRLF = "\r\n"
request = ''

bypassSocket = socket(AF_INET, SOCK_STREAM)
bypassSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
bypassSocket.connect((HOST, PORT))

packet = []
packet.append("GET / HTTP/1.1%s" % (CRLF))
packet.append("User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64)%s%s" % ('A'*15000, CRLF))
packet.append("HOST: %s%s%s" % (HOST, CRLF,CRLF))

bypassSocket.send(request.join(packet))
buffer = bypassSocket.recv(4096)
response = ''

while buffer:
    response += buffer
    buffer = bypassSocket.recv(4096)
header_data, _, body = response.partition(CRLF + CRLF)

print header_data
print body

bypassSocket.close()