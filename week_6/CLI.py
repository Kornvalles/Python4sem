# 2
import sys
import getopt
import logging
from urllib.parse import urlparse

def check_args(arguments):
    # This is to be implemented in your programs...
    return True

def usage():
    return 'Usage : CLI.py –f <filename> or CLI.py --file_name <filename>'

def run(arguments):

    if check_args(arguments):
        opts, args = getopt.getopt(arguments, "f:h", ["file_name="])

        if opts:
            for option, argument in opts:
                if option in ("-h", "--help"):
                    print(usage())
                elif option in ("-f", "--file_name"):
                    with open(argument, "w") as f_obj:
                        with open(args[0]) as read_obj:
                            f_obj.write(read_obj.read())
                else:
                    print("Unknown syntax")
        else:
            with open(args[0]) as f_obj:
                content = f_obj.readlines()
                for line in content[:len(content)-1]:
                    print(line.strip().split(','))



if __name__ == '__main__':
    # Call me from the CLI for example with:
    # python your_script.py arg_1 [arg_2 ...]
    run(sys.argv[1:])