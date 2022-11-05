from sys import stdout

line_write = True

def write(message_type, *args):
    global line_write

    if message_type == "line":
        print(args)
    elif message_type == "dot":
        print(".", end="")
    else:
        print("unknown message type: " + str(message_type))
        print(args)
    return
