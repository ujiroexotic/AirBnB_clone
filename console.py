#!/usr/bin/python3
""" Console interpreter for models """

import cmd

class HBNBCommand(cmd.Cmd):
    """ Airbnb command prompt interface """
    prompt = '(hbnb) '

    def do_create(self, line):
        print ("creates a new instance of BaseModel")

    def help_create(self):
        print ("creates a new instance of BaseModel")
        print("ex: (hbnb) create BaseModel\n")

    def do_update(self, line):
        print("Updates an instance based on the class name and id\n")

    def help_update(self):
        print("Updates an instance based on the class name and id")
        print('ex: (hbnb) Update <class name> <id> <attribute name> "<attribute value>"\n')

    def do_show(self, line):
        print("prints the string repr of instance based on class name")

    def help_show(self):
        print("prints the string repr of instance based on class name")
        print("ex: (hbnb) show BaseModel 1234-1234-1234\n")

    def do_destroy(self, line):
        print("destroys class instance")

    def help_destroy(self):
        print("Destroys class instance based on class name and id")
        print("ex: (hbnb) destroy BaseModel 1234-1234-1234\n")

    def do_all(self, line):
        print("prints all string represenation of all instances")
    
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
