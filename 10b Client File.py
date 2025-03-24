import socket


def connect_to_server():
    # Client setup
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_host = '127.0.0.1'  # Localhost
    server_port = 12345  # Port number

    try:
        # Attempt to connect to the server
        client_socket.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")

        # Receive the message from the server
        message = client_socket.recv(1024).decode()
        print(f"Received from server: {message}")
    except socket.error as e:
        # This will catch network-related errors (connection failure, etc.)
        print(f"Socket error: {e}")
    except Exception as e:
        # This will catch any other general exceptions
        print(f"Client error: {e}")
    finally:
        # Ensure the client socket is always closed
        client_socket.close()


if __name__ == "__main__":
    connect_to_server()

