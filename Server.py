import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host,port))

s.listen(5)
print("Server Listening...")
while True:
    c, addr = s.accept()
    print("connection from : "+str(addr))
    msg = "Thanks for connecting"+"\r\n"
    c.send(msg.encode('ascii'))
    c.close()

