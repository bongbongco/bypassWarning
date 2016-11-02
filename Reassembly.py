from socket import *

HOST = "www.ryomyong.com"
PORT = 80
CRLF = "\r\n"

bypassSocket = socket(AF_INET, SOCK_STREAM)
bypassSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
bypassSocket.connect((HOST, PORT))

packet = []
packet.append("GET / HTTP/1.1%s" % (CRLF))
packet.append("User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64)%s%s" % ('A'*200, CRLF))
packet.append("Connection: keep-alive%s" % (CRLF))
packet.append("Upgrade-Insecure-Requests: 1%s" % (CRLF))
packet.append("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8%s" % (CRLF))
packet.append("Accept-Encoding: gzip, deflate, sdch%s" % (CRLF))
packet.append("Accept-Language: ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4%s" % (CRLF))
packet.append("Accept-Charset: utf-8%s" % (CRLF))
packet.append("Cache-Control: no-cache%s" % (CRLF))
packet.append("Content-Type: application/x-www-form-urlencoded%s" % (CRLF))
packet.append("HOST: %s%s%s" % (HOST, CRLF, CRLF))

for packetLine in packet:
  segments = []
  segments += packetLine
  for segment in segments:
    bypassSocket.send(segment)

buffer = bypassSocket.recv(4096)
response = ''

while buffer:
    response += buffer
    buffer = bypassSocket.recv(4096)
header_data, _, body = response.partition(CRLF + CRLF)

print header_data
print body

'''
for packetLine in packet:
  bypassSocket.send(packetLine)
print bypassSocket.recv(102400)
'''

bypassSocket.close()