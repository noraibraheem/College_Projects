from socket import *
s=socket(AF_INET,SOCK_STREAM)

host ='127.0.0.1'
port = 40674

s.connect((host,port))

while True:
    text_input=input("client: ")
    s.send(text_input.encode('utf-8'))

    if text_input=='Q':
        break
    recieved_data=s.recv(2048)
    if recieved_data.decode('utf-8')=='Q':
        break
    print("server: ",recieved_data.decode('utf-8'))
s.close()