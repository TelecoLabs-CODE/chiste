from cmd import Cmd
import os
from jsonfiles import jsonparser

class MyPrompt(Cmd):

    prompt = 'chiste$ '
    intro = ("\n"+
    "## Cybersecurity and Hacking Intelligence Scripting Toolbox for Everyone - Interactive Mode "+
    "\n"+
    "    _____ _    _ _____  _____ _______ ______    \n"+
    "   / ____| |  | |_   _|/ ____|__   __|  ____|   \n"+
    "  | |    | |__| | | | | (___    | |  | |__      \n"+
    "  | |    |  __  | | |  \___ \   | |  |  __|     \n"+
    "  | |____| |  | |_| |_ ____) |  | |  | |____    \n"+
    "   \_____|_|  |_|_____|_____/   |_|  |______|   Version 1.0\n"+
    "\n"+
    "[*] Starting the console...\n")

    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True
    def help_exit(self):
        print('exit the application. Shorthand: q Ctrl-D')

    def do_clear(self, inp):
        ''' Clear the screen  '''
        print("\n" * 100)

    def do_add(self, inp):
        print("Adding '{}'".format(inp))
    def help_add(self):
        print("Add a new entry to the system.")

    def do_cmds(self, inp):
        jsonparser.json_show_all_commands()
    def help_cmds(self):
        print("Show list of all commands available")

    def default(self, inp):
        if inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))

    do_EOF = do_exit
    help_EOF = help_exit

if __name__ == '__main__':
    MyPrompt().cmdloop()
