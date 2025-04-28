import socket  # Importing socket library to create network connections

def send_post_request(pin):
    host = "127.0.0.1"  # Localhost address (assuming the server is running locally)
    port = 8888          # Port the server listens on (you should replace with the correct port)
    
    # Initialize the socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)  # Set a timeout for connection attempts
        client_socket.connect((host, port))  # Connect to the server

        print("Connected to the server!")  # Confirm successful connection
        client_socket.close()  # Close the connection after testing
    except socket.error as e:
        print(f"Socket error: {e}")
