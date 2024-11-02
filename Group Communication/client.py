import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12346))
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input("")
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))
    client.close()
    
if __name__ == "__main__":
    start_client()
