
import socket

def start_server():
    # Server setup
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_host = '127.0.0.1'  # Localhost
    server_port = 12345        # Port number

    try:
        # Attempt to bind the server to the given address and port
        server_socket.bind((server_host, server_port))
        server_socket.listen(1)  # Listen for incoming connections
        print(f"Server is listening on {server_host}:{server_port}...")

        # Accept a connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Send a message to the client
        message = "Hello from server!"
        client_socket.sendall(message.encode())

        # Close the client connection
        client_socket.close()
        print("Message sent to client. Connection closed.")
    except socket.error as e:
        # This will catch socket-specific errors like binding, connection failures, etc.
        print(f"Socket error: {e}")
    except Exception as e:
        # This will catch other general errors
        print(f"Server error: {e}")
    finally:
        # Ensure that the server socket is always closed properly
        server_socket.close()

if __name__ == "__main__":
    start_server()
