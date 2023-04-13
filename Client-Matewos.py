# Import the socket module to enable network communication
from socket import *

# Define the IP address and port number of the server
serverPort = ("192.168.0.38", 16500) 

# Create a socket object for the client
Socket_of_client = socket(AF_INET, SOCK_STREAM)

# Connect the socket object to the server
Socket_of_client.connect(serverPort)

# Define the name of the client
Name_of_client = "Matewos"

# Define a function to get a valid integer input from the client
def get_valid_integer():
    # Prompt the client to enter a number within a certain range
    Number_input_from_Client = int(input('Hello client! Please enter a number in the range of 1 upto 100: '))
    
    # Check if the entered number is within the specified range
    if 1 <= Number_input_from_Client <= 100:
        # If the number is valid, return it
        return Number_input_from_Client
    else:
        # If the number is not valid, inform the client and terminate the connection
        print("Sorry client! Since you have entered a number out of range your connection is lost.....try again!")
        
# Call the get_valid_integer function and store the returned value in a variable
Number_input_from_Client = get_valid_integer()

# Concatenate the name of the client and the number entered by the client into a string separated by a comma
message_sent_to_Server = Name_of_client + "," + str(Number_input_from_Client)

# Send the concatenated message to the server
Socket_of_client.send(message_sent_to_Server.encode()) 

# Receive data from the server and decode it
data_from_server = Socket_of_client.recv(2048)
data_from_server = data_from_server.decode().split(',') 

# Print the name of the server, the generated number from the server, and the sum of the client's number and the server's number
print("Name of server: " , data_from_server[0]) 
print("Number generated from the server: " , data_from_server[1])
print("The total sum of the numbers: " , data_from_server[2])

# Close the client socket object
Socket_of_client.close()
