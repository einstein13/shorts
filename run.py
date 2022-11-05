import sys

class Main(object):

    def __init__(self):
        super(Main, self).__init__()

    def run(self, argv):
        if len(argv) > 1:
            arg = argv[1]
            arg = arg.replace("-", "")
            if arg == "help" or arg == "h":
                pass
                # print help
            elif arg == "auto" or arg == "a":
                pass
                # read auto file and follow it
            else:
                pass
                # print unknown command message
                # run standard process
        else:
            # run standard process
        return

m = Main()
m.run(sys.argv)