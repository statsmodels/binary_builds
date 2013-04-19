"""
Outputs an Environmental Variable UPLOAD_BUILD that is set to either 1 or 0
"""
import os
import re
import sys

from rename_binaries import git_version

curdir = os.path.abspath(os.path.dirname("__file__"))

def check_remote_git_version():
    #use remote_file_list.out - this is the full dir/ls command with
    #permissions, user, group, etc. no flags are allowed, so we have to parse
    #check if version of remotely uploaded files is the most recent
    git_rev = git_version()

    with open(os.path.join(curdir, "remote_file_list.out")) as fin:
        for line in fin:
            if re.search(git_rev[:7], line):
                # found a match, don't do anything
                sys.exit(0)
        else:
            sys.exit(1)

if __name__ == "__main__":
    check_remote_git_version()

