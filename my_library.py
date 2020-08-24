from subprocess import Popen, PIPE, DEVNULL
from os.path import isfile, exists

# Just some functions that I use day-to-day with python
# Created by Simon Gardling

def run_command(command):
    process = Popen(command, stdout=PIPE, universal_newlines=True, shell=True, stderr=DEVNULL)
    stdout, stderr = process.communicate()
    del stderr
    return stdout

def yes_or_no(question):
    answer = input(question + " (y/n): ").lower().strip()
    print("")
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = input(question + "(y/n):").lower().strip()
        print("")
    if answer[0] == "y":
        return True
    else:
        return False