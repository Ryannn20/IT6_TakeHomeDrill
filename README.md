This project contains a Python script designed to guess a web application's 3-digit numeric PIN using a brute-force method. The script attempts all combinations (000 to 999) to find the correct PIN. It interacts with a simple web server that requires a PIN for access.

Objective
The objective of this challenge was to create a Python script that:
Connects to a server using a socket.
Sends HTTP POST requests to test PIN combinations.
Handles rate limiting by waiting before retrying invalid attempts.
Successfully identifies the correct PIN.

Solution Overview
The solution involves the following components:
Socket Communication: Using Python's socket library to send and receive data between the client and the web server.
HTTP POST Request: Constructing and sending an HTTP POST request with a PIN as the form data.
Brute Force Loop: A loop that tries all 3-digit PIN combinations (from 000 to 999) systematically.
Rate Limiting Handling: When the server limits the number of requests (e.g., with a "Please wait" message), the script waits for a while before continuing.
Server Response Handling: Analyzing the server's response to determine whether the PIN is correct or not.

Stages of the Project
Stage 1: Basic Socket Connection
The first step was to establish a socket connection to the server. This ensures that the client can communicate with the server at the correct address and port. 
Stage 2: Send HTTP POST Request
In this stage, I created the functionality to send an HTTP POST request to the /verify endpoint. The request contains a PIN formatted as magicNumber=XXX.
Stage 3: Handle Server Response
This stage involved receiving the response from the server after sending the PIN. The response was decoded and analyzed to determine whether the PIN was correct or not.
Stage 4: Brute-Force Loop with Rate Limiting
The final stage involved implementing the brute-force loop that tries all possible PIN combinations, while respecting any rate-limiting the server imposes. If the server returns a "Please wait" message, the script waits for a short period before continuing.


Files
solution.py: main python script
README.md: explains the solution process


Drive Video Link (can't upload the video to youtube, youtube said the video is too long):
https://drive.google.com/file/d/1jRP4lSA3p_1UVFp-3G7v7tX48bqcBQIw/view?usp=sharing

