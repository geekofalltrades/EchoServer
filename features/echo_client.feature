Feature: Echo Client
    Send a message to the echo server and receieve the same message
    back. Assumes that the echo server is running.

    Scenario: Echo Messages
        Given the message <input>
        When I submit that message to the echo server
        Then I receive back <output>

    Examples:
    | input | output  |
    | 0     | 0       |
    | blargh| blargh  |
    | This is a message. | This is a message.  |
    | Here is another message.     | Here is another message.    |