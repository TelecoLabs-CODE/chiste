import argparse
import logging
import sys
from yaml import load, Loader

from . import utils
from . import TOOLS
from cli  import help
from jsonfiles import jsonparser


def call_jsonparser():
    jsonparser.json_parsing()
    return "\n\n"


def exit_menu_while():
    return "Bye-Bye my friend"


def menu():
    flag=0

    while(flag!=1):
        print("Welcome you are to CHISTE: find what you expect...")
        print("\n")
        print("    ################################")
        print("    #            CHISTE            #")
        print("    ################################")
        print("    #                              #")
        print("    #     1.  Console              #")
        print("    #     2.  Search a tool        #")
        print("    #     3.  Find your guide      #")
        print("    #     4   20Q                  #")
        print("    #     5.  Exit                 #")
        print("    #                              #")
        print("    ################################")
        print("\n")
        option = input("Select an option: ")
        switcher = {
            '1': call_console,
            '2': call_searcher,
#           '3':
            '5': exit_menu_while,
            'exit': exit_menu_while
        }

        if (option!='5' and option != 'exit'):
            func = switcher.get(option, lambda: "Invalid option")
            print(func())
        else:
            flag=1

def call_searcher():
    searcher = help.MyPrompt()
    searcher.cmdloop()


def call_console():
    console = help.MyPrompt()
    console.cmdloop()

def version():
    print("CHISTE 1.0")
    print("Copyright © 2019 Alberto Rafael Rodríguez Iglesias")
    print("License: To Be Defined")
    print("This is free software: you are free to change and redistribute it with respect to the current license.")
    print("There is NO WARRANTY, to the extent permitted by law.")

def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        level=logging.DEBUG,
                        stream=sys.stdout)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    parser = argparse.ArgumentParser(description='Security Assistant ( CHISTE )')
    for validator in TOOLS.keys():
        parser.add_argument('--' + validator, action='append', default=[])
    parser.add_argument('-f', '--file', type=str)
    parser.add_argument(
        '--menu',
        action='store_true',
        help=('Access the main menu/panel')
    )
    parser.add_argument(
        '--config',
        type=str,
        help='Configuration details for the tool'
    )
    parser.add_argument(
        '--console',
        action='store_true',
        help='Enter the interactive/console mode'
    )
    parser.add_argument(
        '--version',
        action='store_true',
        help='Shows current version of CHISTE'
    )

    opts, patchlist = parser.parse_known_args()
    config = {}

    session = None

    if opts.menu:
        menu()

    if opts.file:
        file_content = utils.get_content(opts.file)

    if opts.console:
        call_console()

    if opts.version:
        version()

    failed_validations = 0
    file_content = ""
    for validator in TOOLS.keys():
        validator_arguments = getattr(opts, validator.replace('-', '_'))
        for argument in validator_arguments:
            if not TOOLS[validator](file_content):
                failed_validations += 1

    return failed_validations

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
