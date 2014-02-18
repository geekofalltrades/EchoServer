from lettuce import step
from lettuce import world

from echo_client import call_echo_server


@step('the message (.+)')
def the_message(step, msg):
    world.msg = msg


@step('I submit that message to the echo server')
def submit_message(step):
    world.echo = call_echo_server(world.msg)


@step('I receive back (.+)')
def compare(step, expected):
    assert world.echo == expected, "Got %s" % world.echo
