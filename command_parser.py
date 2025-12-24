def parse_command(command):
    if "light on" in command:
        return "LIGHT_ON"
    elif "light off" in command:
        return "LIGHT_OFF"
    elif "fan on" in command:
        return "FAN_ON"
    elif "fan off" in command:
        return "FAN_OFF"
    else:
        return "UNKNOWN"
