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

    def default(self, arg):
        """Default when command prefix not recognized."""
        s = (arg.replace('.', ' ').replace('(', ' ').replace(')', ' '))
        print("HERE IS s...", s)
        l = s.split()
        print("Here is l...", l)
        if len(l) > 1:
            cmd = l.pop(1)
            print("HERE IS CMD...", cmd)
        if '{' in s and cmd == 'update':
            s = s.replace('update', '')
            print("HERE IS NEW s....", s)
            d = re.spllit(r"\s(?!{[^{]*})", s)
            print("\n\n Here is new d...", d)
        """
            for k, v in eval(d[3]).items():
                print(l[0]), print(l[1]), print(k), print(v)
                args = l[0] + ' ' + l[1][:-1] + ' ' + k + ' ' + str(v)
                self.do_update(args)
            return
        args = ' '.join(l).replace(',', '')
        try:
            eval('self.do_' + cmd + '(args)')
        except:
            print('Invalid argument.')"""
    """        
    def default(self, args):
        ""
        default method to use with command()
        ""
        tokens = args.split(".")
        cls = tokens[0]
        uuid = shlex.split(tokens[1])
        fields = uuid[0].split("(")
        uuid[0] = fields[1]
        new_cmd = []
        for item in uuid:
            print("HERE IS THE ITEM", type(item), item)
            new_cmd.append(item[:])
            if '{' in item in cls == "update":
                print("I AM HERE")
                
        fields = fields[0]
        execute = fields + " " + cls + " " + " ".join(new_cmd)
        final = execute[:-1]
        self.onecmd(final)
      """

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
