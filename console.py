#!/usr/bin/python3
"""Entry point for the command interpreter of the HBNB application"""


import cmd
import models
from models.base_model import BaseModel

class_list = {"BaseModel": BaseModel}

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
        arg = line.split()
        names = dir()
        if (len(arg) == 0):
            print("** class name is missing **")

        else:
            if arg[0] in class_list:
                new_obj = class_list[arg[0]]()
                models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        arg = line.split()
        try:
            dict_of_objs = models.storage.all()
            for key in dict_of_objs.keys():
                if arg[1] == dict_of_objs[key].id:
                    print(dict_of_objs[key])
                    break


        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        pass

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass

    def emptyline(self):
        """Empty lines will go to the next input loop"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
