#!/usr/bin/python3
"""
This module contains the command interpeter
for managing Airbnb files
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models import storage, allclasses
from datetime import datetime
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """
    Class that inherits from cmd.Cmd
    """
    prompt = '(hbnb) '
<<<<<<< HEAD
    classes = allclasses
=======
    classes = (
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review')
>>>>>>> a67e2842b3e7c37c76e0d4091a0a10b0227be0d0

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
<<<<<<< HEAD
            print("{}".format(new.id))
        else:
            print("** class doesn't exist **")
=======
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
>>>>>>> a67e2842b3e7c37c76e0d4091a0a10b0227be0d0

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        saves the changes into JSON file
        """
<<<<<<< HEAD
        if not args:
            print("** class name missing **")
            return
        tokens = args.split(" ")
        objects = storage.all()

        if tokens[0] in self.classes:
            if len(tokens) < 2:
                print("** instance id missing **")
=======
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
>>>>>>> a67e2842b3e7c37c76e0d4091a0a10b0227be0d0
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
<<<<<<< HEAD
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
        try:
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
        except AttributeError:
            print("** attribute name missing **")

    def do_show(self, args):
        """ show string representation of an instance"""
        tokens = args.split()
        objects = storage.all()
        try:
            if len(tokens) == 0:
                print("** class name missing **")
                return
            if tokens[0] in self.classes:
                if len(tokens) > 1:
                    key = tokens[0] + "." + tokens[1]
                    if key in objects:
                        obj = objects[key]
                        print(obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        except AttributeError:
            print("** instance id missing **")

    def default(self, args):
        """
        default method to use with command()
        """
        try:
            tokens = args.split(".")
            cls = tokens[0]
            uuid = shlex.split(tokens[1])
            fields = uuid[0].split("(")
            uuid[0] = fields[1]
            new_cmd = []
            for item in uuid:
                new_cmd.append(item[:])
            fields = fields[0]
            execute = fields + " " + cls + " " + " ".join(new_cmd)
            final = execute[:-1]
            self.onecmd(final)
        except:
            print("** invalid command **")

    def do_count(self, args):
        """
        Counts number of instances of a class
        """
        objects = storage.all()
        instances = []
        count = 0
        if args in self.classes:
            for name in objects:
                if name[0:len(args)] == args:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")
=======
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
>>>>>>> a67e2842b3e7c37c76e0d4091a0a10b0227be0d0

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
<<<<<<< HEAD
        return
=======
        pass
>>>>>>> a67e2842b3e7c37c76e0d4091a0a10b0227be0d0

if __name__ == "__main__":
    HBNBCommand().cmdloop()
