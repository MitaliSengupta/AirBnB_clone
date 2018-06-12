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
=======
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
  
    classes = ('BaseModel')
    filepath = models.storage._FileStorage.__file_path


    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id. Ex: $ create BaseModel
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

    def do_dict(self, args):
        """
        doesn't work properly
        """
        tokens = args.split(' ', 2)
        print(tokens)
        update_dict = json.loads(tokens[2].replace("'", '"'))
        print(update_dict)
        if self.storage._FileStorage__objects.get('{}.{}'.format(tokens[0], args[1][1:-1]), None) is None:
            print("** no instance found **")
        else:
            obj = self.storage._FileStorage__objects['{}.{}'.format(args[0], args[1][1:-1])]
            for k, v in update_dict.items():
                if getattr(obj, k, None) is not None:
                    setattr(obj, k, type(
                        getattr(obj, k, None))(v))
                else:
                    setattr(obj, k, v)
            models.storage.save()

    def default(self, args):
        """
        default method to use with command()
        """
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
        prints the string representation of an instance
        """
        arg_list = args.split()
        key = arg_list[0] + "." + arg_list[1]
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dict_of_objs = models.storage.all()
            if key in dict_of_objs:
                print(dict_of_objs[key])
                return
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Destroy command to delete an instance based on class name for id
        """
        arg_list = args.split()
        key = arg_list[0] + "." + arg_list[1]
        if len(arg_list) == 0:
            print("** class name missing **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        elif args[1] not in self.classes:
            print("** class doesn't exist **")
        else:
            dict_of_objs = models.storage.all()
            if key in dict_of_objs:
                del dict_of_objs[key]
                models.storage.save()
                return
            print("** no instance found **")

    def do_all(self, args):
        """
        All command to display all objects that currently exist
        """
        try:
            with open(self.fp, encoding="UTF-8") as myfile:
                dump = json.load(myfile)
        except FileNotFoundError:
            dump = None
        tokens = args.split()
        instances = []
        if len(tokens) > 0 and tokens[0] in self.classes:
            cls = tokens[0]
        elif len(tokens) > 0 and tokens[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            cls = None
        if dump:
            if cls is not None:
                for key, val in dump.items():
                    if val['__class__'] == cls:
                        del val['__class__']
                        model = eval(cls)(**val)
                        instances.append(model)
            elif cls is None:
                for key, val in dump.items():
                    cls = val['__class__']
                    del val['__class__']
                    model = eval(cls)(**val)
                    instances.append(model)
            if len(instances) > 0:
                print(instances)
        if dump is None and len(tokens) > 0 and cls is not None:
            pass

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
        EOF command exits out of the command interpreter
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
        Returns back to the prompt
        """
        return to display prompt
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
