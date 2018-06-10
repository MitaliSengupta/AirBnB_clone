#!/usr/bin/python3
"""
This module contains the command
line interpreter
"""
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """
    class the custom command interpreter inherits
    from cmd
    """
    prompt = '(hbnb) '
    classes = ('BaseModel')
    filepath = storage._FileStorage.__file_path

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
        prints the string representation of an instance

        usage: show <class_name> <id>
        """
        tokens = args.split()
        if len(tokens) == 0:
            print('** class name missing **')
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(tokens) < 2:
            print('** instance id missing **')
        else:
            try:
                with open(self.filepath, encoding='UTF-8') as myfile:
                    dump = json.load(myfile)
            except FileNotFoundError:
                dump = None
                print('** no instance found **')
                return
            if dump:
                cls = tokens[0]
                uid = tokens[1]
                keys = "{}.{}".format(cls, uid)
                for key, val in dump.items():
                    del val['__class__']
                    if keys in dump.keys():
                        obj_dict = dump[key]
                        obj = eval(cls)(**obj_dict)
                        print(obj)
                        return
            print('** no instance found **')

    def do_destroy(self, args):
        """
        Destroy command to delete an instance based on class name for id
        """
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dict_of_objs = models.storage.all()
            for key in dict_of_objs.keys():
                if arg_list[1] == dict_of_objs[key].id:
                    del dict_of_objs[key]
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """
        All command to display all objects that currently exist
        """
        arg_list = args.split()
        if len(args) > 0:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
        dict_of_objs = models.storage.all()
        for key in dict_of_objs.keys():
            print(dict_of_objs[key])
            try:
                with open(self.storage.__FileStorage__file_path,
                          encoding="UTF-8") as myfile:
                    dump = json.load(myfile)
            except FileNotFoundError:
                dump = None
                print("** no instance found **")
                return

    def do_update(self, args):
        """
        Update command to add or update an attribute
        """
        arg_list = args.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")


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
