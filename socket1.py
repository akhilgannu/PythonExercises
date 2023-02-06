import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('en.wikipedia.org', 80))
command = 'GET http://en.wikipedia.org/wiki/A HTTP/1.0\n\n'.encode()
mysock.send(command)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()