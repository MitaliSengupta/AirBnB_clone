#!/usr/bin/python3
"""
This module contains the command interpeter
for managing Airbnb files
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage, allclasses
from datetime import datetime
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '
    classes = allclasses

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it to JSON file
        and prints the id
        """
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        if tokens[0] in self.classes:
            new = eval("{}()".format(tokens[0]))
            new.save()
            print("{}".format(new.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        objects = storage.all()

        if tokens[0] in self.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                print(objects[name])
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        saves the changes into JSON file
        """
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        objects = storage.all()

        if tokens[0] in self.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj = objects[name]
                if obj:
                    objs = storage.all()
                    del objs["{}.{}".format(type(obj).__name__, obj.id)]
                    storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        objects = storage.all()
        instances = []
        if not args:
            for name in objects:
                instances.append(objects[name])
            print(instances)
            return
        tokens = args.split(" ")
        if tokens[0] in self.classes:
            for name in objects:
                if name[0:len(tokens[0])] == tokens[0]:
                    instances.append(objects[name])
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Update an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        objects = storage.all()

        if tokens[0] in self.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
                return
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj = objects[name]
                untouchable = ["id", "created_at", "updated_at"]
                if obj:
                    token = args.split(" ")
                    if len(token) < 3:
                        print("** attribute name missing **")
                    elif len(token) < 4:
                        print("** value missing **")
                    elif token[2] not in untouchable:
                        obj.__dict__[token[2]] = token[3]
                        obj.updated_at = datetime.now()
                        storage.save()
        else:
            print("** class doesn't exist **")

    def do_quit(self, args):
        """
        Quit command exits out of the command interpreter
        """
        quit()

    def do_EOF(self, args):
        """
        EOF command exits out of the command interpreter
        """
        quit()

    def do_help(self, args):
        """
        Command lists all help details for each command
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        Returns back to the prompt
        """
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
