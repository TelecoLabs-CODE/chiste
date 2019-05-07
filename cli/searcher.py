import json
import os
import sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
#            callback(pathname,f,top)
            with open(pathname, 'r') as json_file:
                data = json.load(json_file)
#            print(pathname)
            ncommands = 0
            ncommands = len(data)
            n_full_commands = 0
            for i in range(0,ncommands):
                command = data[i]["cmd"]
                if command != "":
                    n_full_commands += 1
                    print(command)
#            if n_full_commands != 0:
#                callback(pathname,f,top)
#                print("Full Commands: ", n_full_commands, "Holes: ", ncommands)

        else:
            # Unknown file type, print a message
            print('Skipping %s', pathname)

def visitfile(fullname,file,path):
    print('visiting', file, 'in', path, "=", fullname)

def json_show_all_commands():
    with open('jsonfiles/files/sample.json', 'r') as json_file:
        data = json.load(json_file)

    walktree("jsonfiles/files/linux", visitfile)
