Feature: Echo Client
    Send a message to the echo server and receieve the same message
    back. Assumes that the echo server is running.

    Scenario: Echo Messages
        Given the message <input>
        When I submit that message to the echo server with a buffer of size 32
        Then I receive back <output>

    Examples:
    | input | output  |
    | 0     | 0       |
    | This is a short message. | This is a short message.  |
    | This message overflows the buffer, which is 32 bytes. | This message overflows the buffer, which is 32 bytes.  |
    | This message matches the buffer.  | This message matches the buffer. |