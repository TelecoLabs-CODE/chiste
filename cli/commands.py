from cmd import Cmd

class MyPrompt(Cmd):
    def do_exit(self, inp):
        print("Bye")
        return True

    def do_add(self, inp):
        print("Adding '{}'".format(inp))

    def do_example_cmd():
        print("Command for an example")

MyPrompt().cmdloop()
print("after")
