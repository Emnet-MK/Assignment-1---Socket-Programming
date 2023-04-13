# Import the module "socket" and "random"
import socket
import random

# Assign a port number
server_port = 16500 

# Create a new socket object using the socket module
# Set parameters to IPv4 address family and TCP protocol.
Socket_of_Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to the specified port server_port.
Socket_of_Server.bind(('', server_port))

# Start listening for incoming client connections on the server socket with a maximum of 1 pending connection.
Socket_of_Server.listen(1)

# Assign the server name
Name_of_Server="Emnet's server"

# Display a message of the server being ready
print('Hello client! This Server is ready to establish connection with you now .....')

#create a loop that will run indefinitely, waits for incoming connections from clients.
while True:
    
    # The Socket_of_Server.accept() method blocks until a client connects, 
    # and returns a new socket object (Socket_of_client) and the client's address (Address_of_client).
    Socket_of_client, Address_of_client = Socket_of_Server.accept()
    data = Socket_of_client.recv(2048)

    # data received is split into the Name_of_client and Number_input_from_client variables.
    Name_of_client, Number_input_from_client= data.decode().split(',')
    Number_input_from_client = int(Number_input_from_client)

    # A random number between 1 and 100 is generated and stored
    server_generated_num = random.randint(1, 100)

    # if number is not within the range 1 to 100 terminate loop 
    if Number_input_from_client < 1 or Number_input_from_client > 100:
        break

    #Calculate the sum of server_generated_num and Number_input_from_client and print it along with other details
    total_sum_of_numbers = server_generated_num + Number_input_from_client
    print(f"Name of Client: {Name_of_client}")
    print(f"Number received from client : {Number_input_from_client}")
    print(f"Number generated from the server: {server_generated_num}")
    print(f"The total sum of the numbers: {total_sum_of_numbers}")
    print(f"Address of client : {Address_of_client}")

    # Create message containing the server's name, generated number, and total sum of the numbers.
    # Send the message back to the client and close socket connection. 
    message = f"Emnet's server,{server_generated_num},{total_sum_of_numbers}"
    Socket_of_client.send(message.encode())
    Socket_of_client.close()
