import socket  

def send_post_request(pin):
    host = "127.0.0.1"
    port = 8888
    resource = "/verify"  # The endpoint where the server accepts PIN for verification
    form_data = f"magicNumber={pin:03d}"  # The form data, PIN is formatted to 3 digits

    # Build the raw HTTP POST request
    request = f"""POST {resource} HTTP/1.1\r\nHost: {host}:{port}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(form_data)}\r\nConnection: close\r\n\r\n{form_data}"""

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)
        client_socket.connect((host, port))  # Connect to the server
        client_socket.sendall(request.encode())  # Send the POST request
        print(f"Request sent for PIN: {pin:03d}")
        client_socket.close()
    except socket.error as e:
        print(f"Socket error: {e}")

