#!/usr/bin/python3
"""Entry point for the command interpreter of the HBNB application"""


import cmd

class HBNBCommand(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_EOF(self, line):
        """Typing the command 'EOF' will cleanly exit the console session"""

        return True

    def do_quit(self, line):
        """Typing 'quit' will cleanly exit the console session"""

        return True

    def do_create(self, line):

    def do_show(self, line):

    def do_destroy(self, line):

    def do_all(self, line):

    def do_update(self, line):

    def emptyline(self):
        """Empty lines will go to the next input loop"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
