import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("localhost",1024))

s.listen(5)

while True:
    clt, adr=s.accept()
    
    stradr=str(adr)
    
    print("connection to"+stradr+"established")
    
    string ="Socket programming in python."
    
    arr = string.encode("utf-8")
    
    print(arr)
    
    clt.send(arr)
