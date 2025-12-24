def execute(action):
    if action == "LIGHT_ON":
        print("Light turned ON")
    elif action == "LIGHT_OFF":
        print("Light turned OFF")
    elif action == "FAN_ON":
        print("Fan turned ON")
    elif action == "FAN_OFF":
        print("Fan turned OFF")
    else:
        print("Command not recognized")
