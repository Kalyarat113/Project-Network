from socket import *

SERVER_NAME = "localhost"
SERVER_PORT = 5555

def receive_and_print_response():
    response = client_socket.recv(1024).decode()
    status_code, message = response.split(' ', 1)
    print(f"\n[{status_code}] {message}")
    return int(status_code)

# Create a socket object
client_socket = socket(AF_INET, SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_NAME, SERVER_PORT))

    while True:
        # Receive the current status and instructions
        status = receive_and_print_response()

        # Check if game over
        if status == 201:
            break

        # Player's turn
        if status in [303, 400, 401]:
            user_input = input("Enter a number: ")
            client_socket.send(user_input.encode())

finally:
    # Close the socket
    client_socket.close()
