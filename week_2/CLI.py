# 2
import sys
import getopt

def check_args(arguments):
    # This is to be implemented in your programs...
    return True

def run(arguments):
    try:
        opts, args = getopt.getopt(arguments, "o:", ["file"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    output = None
    file_name = None
    for option, argument in opts:
        print(option)
        if option in ("-f","--file"):
            file_name = argument
        elif option in ("-o", "--output"):
            output = argument
        else:
            assert False, "unhandled option"

    print(output)
    print(file_name)

if __name__ == '__main__':
    # Call me from the CLI for example with:
    # python your_script.py arg_1 [arg_2 ...]
    run(sys.argv[1:])