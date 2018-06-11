#!/usr/bin/python3
"""
This module contains the command
line interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """
    class the custom command interpreter inherits
    from cmd
    """
    prompt = '(hbnb) '
    classes = (
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review')

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        if not args:
            print("** class name missing **")
            return
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(args)()
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based
        on the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dict_of_objs = models.storage.all()
            key = arg_list[0] + "." + arg_list[1]
            if key in dict_of_objs:
                print(dict_of_objs[key])
                return
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Destroy command to delete an instance based on class name for id
        """
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dict_of_objs = models.storage.all()
            key = arg_list[0] + "." + arg_list[1]
            if key in dict_of_objs:
                del dict_of_objs[key]
                models.storage.save()
                return
            print("** no instance found **")

    def do_all(self, args):
        """
        All command to display all instances of a class or all objects
        """
        object_list = []
        arg_list = args.split()
        dict_of_objs = models.storage.all()
        if len(arg_list) > 0:
            if arg_list[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key in dict_of_objs.keys():
                    if dict_of_objs[key].__class__.__name__ == arg_list[0]:
                        object_list.append(dict_of_objs[key])
                return
        else:
            for key in dict_of_objs.keys():
                object_list.append(dict_of_objs[key])

        print(object_list)

    def do_update(self, args):
        """
        Update command to update or add an attribute to an instance
        """
        arg_list = args.split()
        dict_of_objs = models.storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            key = arg_list[0] + "." + arg_list[1]
            if key in dict_of_objs:
                setattr(dict_of_objs[key], arg_list[2], eval(arg_list[3]))
                dict_of_objs[key].save()
            else:
                print("** no instance found **")

    def do_quit(self, args):
        """
        Quit command to exit out of the interpreter
        """
        quit()

    def do_EOF(self, args):
        """
        EOF command to exit out of intepreter
        """
        quit()

    def do_help(self, args):
        """
        Help command to get more information on
        input commands if no parameter given display
        all commands
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        display prompt
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
