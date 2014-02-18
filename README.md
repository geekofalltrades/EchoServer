Echo Server

A simple socket-based echo server.

Usage (with echo_server.py running in separate terminal session):

>>>from echo_client import call_echo_server
>>>call_echo_server('This is a message.')
'This is a message.'

From the command line:
$ python echo_client.py "This is a message"
This is a message.

$python echo_client.py
Enter your message. This is a message.
This is a message.


Implementation:
The server implementation sticks closely to the walkthrough, simply add-
ing a loop in the server in which it waits for additional connections
after echoing each message from a client. The server is then quit with
Ctrl-C. The server script catches the KeyboardInterrupt that this raises
and closes the socket in the corresponding except statement, ensuring
that the socket is properly closed before the script exits (although I'm
not sure whether this is strictly necessary.)


Testing:
Four simple lettuce tests are set up in the "features" directory. Ensure
that an instance of the echo server is running with "python echo_server.py",
then run "lettuce" from the project directory to see the results of the
tests.