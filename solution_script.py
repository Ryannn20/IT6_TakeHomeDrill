import socket  

def send_post_request(pin):
    host = "127.0.0.1"
    port = 8888
    resource = "/verify"
    form_data = f"magicNumber={pin:03d}"
    
    request = f"""POST {resource} HTTP/1.1\r\nHost: {host}:{port}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(form_data)}\r\nConnection: close\r\n\r\n{form_data}"""

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)
        client_socket.connect((host, port))
        client_socket.sendall(request.encode())
        
        response = b""  # Initialize an empty byte string to store the response
        while True:
            data = client_socket.recv(4096)  # Receive data in chunks
            if not data:  # If no more data is received, break the loop
                break
            response += data  # Append the received data to the response
        
        client_socket.close()
        
        # Decode the byte response into a string and print it
        print("Server response:", response.decode(errors="ignore"))
    except socket.error as e:
        print(f"Socket error: {e}")


