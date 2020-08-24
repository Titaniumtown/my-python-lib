from subprocess import Popen, PIPE, DEVNULL
from os.path import isfile, exists

def run_command(command):
    process = Popen(command, stdout=PIPE, universal_newlines=True, shell=True,stderr=DEVNULL)
    stdout, stderr = process.communicate()
    del stderr
    return stdout