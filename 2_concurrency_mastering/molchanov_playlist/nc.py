import socket
import sys

if len(sys.argv) != 3:
    print(f"Usage: python {sys.argv[0]} <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((host, port))
    while True:
        message = input("Send: ")
        if message.lower() == 'exit':
            break
        
        client_socket.send(message.encode())
        data = client_socket.recv(4096)
        
        if not data:
            break
            
        print(f"Received: {data.decode()}")

except Exception as e:
    print(f"Error: {e}")
finally:
    client_socket.close()