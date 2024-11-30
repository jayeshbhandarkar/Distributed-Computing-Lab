import socket
import struct

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 6667))
    server_socket.listen(1)
    print("Server is waiting for a connection...")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    try:
        data = conn.recv(8)
        a, b = struct.unpack('!ii', data)
        print(f"Received numbers: {a} and {b}")
        print(f"Sum: {a + b}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()
        server_socket.close()
        print("Server closed.")

if __name__ == "__main__":
    server_program()