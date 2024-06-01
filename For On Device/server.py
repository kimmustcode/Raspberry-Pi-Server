from socket import * 

HOST = "0.0.0.0"
PORT = 42069

with socket(AF_INET, SOCK_STREAM) as s: 
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()

    while True:
        data = conn.recv(1024)
        if data: 
            print("@kimmustcode: " + str(data.decode('utf-8')))
        if not data: 
            break 

