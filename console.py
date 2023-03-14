#!/usr/bin/python3
""" Console interpreter for models """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state imprt State
from models.city import City
from models.review import Review
from models import storage

STORAGE = storage.all()

MODEL_CLASS = {
        "basemodel": BaseModel,
        "user": User
        }


def parse_line_logic(self, line):
    command = cmd.Cmd.parseline(self, line)
    model = command[0]
    id_ = command[1]

    if model is None:
        print("** class name missing **")
        return None
    if model.lower() not in MODEL_CLASS.keys():
        print("** class doesn't exist **")
        return None
    if id_ == "" or id_ is None:
        print("** instance id is missing **")
        return None
    modelId = model + '.' + id_
    if modelId not in STORAGE.keys():
        print("** no instance found **")
        return None

    return modelId


class HBNBCommand(cmd.Cmd):
    """ Airbnb command prompt interface """
    prompt = '(hbnb) '

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        elif line.lower() not in MODEL_CLASS.keys():
            print("** class doesn't exist **")
        else:
            model = MODEL_CLASS[line.lower()]()
            model.save()
            print(model.id)

    def help_create(self):
        print("creates a new instance of BaseModel")
        print("ex: (hbnb) create BaseModel\n")

    def do_update(self, line):
        command = line.split(' ')
        length = len(command)

        if command[0] == "":
            print("** class name missing **")
            return
        elif command[0].lower() not in MODEL_CLASS.keys():
            print("** class doesn't exists **")
            return
        if length == 1:
            print("** instance id missing **")
            return

        modelId = command[0] + '.' + command[1]

        if modelId not in STORAGE.keys():
            print("** no instance found **")
            return
        model = STORAGE[modelId]

        if length == 2:
            print("** attribute name missing **")
            return

        if length == 3:
            print("** value missing **")
            return

        value = command[3]

        try:
            model.__dict__[command[2]] = eval(value)
        except NameError:
            model.__dict__[command[2]] = value
        model.save()

    def help_update(self):
        print("Updates an instance based on the class name and id")
        string = 'ex: (hbnb) Update <class name> <id> '
        string += '<attribute name> "<attribute value>"\n'
        print(string)

    def do_show(self, line):
        modelId = parse_line_logic(self, line)
        if modelId is not None:
            print(STORAGE[modelId])

    def help_show(self):
        print("prints the string repr of instance based on class name")
        print("ex: (hbnb) show BaseModel 1234-1234-1234\n")

    def do_destroy(self, line):
        modelId = parse_line_logic(self, line)
        if modelId is not None:
            STORAGE.pop(modelId)
            storage.save()

    def help_destroy(self):
        print("Destroys class instance based on class name and id")
        print("ex: (hbnb) destroy BaseModel 1234-1234-1234\n")

    def do_all(self, line):
        command = cmd.Cmd.parseline(self, line)
        model = command[0]
        result = []
        if model is None:
            for key in STORAGE.keys():
                result.append(STORAGE[key].__str__())
        else:
            for key in STORAGE.keys():
                if model in key:
                    result.append(STORAGE[key].__str__())
        if len(result) == 0:
            print("** class doesn't exist **")
            return
        print(result)

    def help_all(self):
        print("prints all string representation of all istances")
        print("ex: (hbnb) create BaseModel\n")

    def do_EOF(self, line):
        """ control-c to end program """
        print("")
        return True

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        return

    def postcmd(self, stop, line):
        return cmd.Cmd.postcmd(self, stop, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
