#!/usr/bin/python3
"""Entry point for the command interpreter of the HBNB application"""


import cmd

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Typing the command 'EOF' will cleanly exit the console session"""

        return True

    def do_quit(self, line):
        """Typing 'quit' will cleanly exit the console session"""

        return True

    def emptyline(line):
        """Empty lines will go to the next input loop"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
