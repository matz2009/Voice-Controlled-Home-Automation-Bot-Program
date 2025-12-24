from voice_recognition import get_voice_command
from command_parser import parse_command
from actuator import execute

command = get_voice_command()
action = parse_command(command)
execute(action)
