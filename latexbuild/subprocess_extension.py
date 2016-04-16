"""Create error-handled subprocess that runs in specific directory

This module provides a function that error handles subprocess
calls and runs the subprocess in a specific working directory.
This is functionality is important for Latex, because:

1) Most build tools for Latex are not written in Python
2) Because they create many files, latex commands should be run
in the same directory as the latex file that is being built
"""

from subprocess import Popen, CalledProcessError, PIPE, STDOUT
from . import assertions

def check_output_cwd(args, cwd, timeout=None):
    '''Open a subprocess in another working directory

    Raises ValueError if system binary does not exist
    Raises CalledProcessError if the return code is non-zero

    :returns: list of standard output and standard error from subprocess

    :param args: a list of command line arguments for subprocess
    :param cwd: the working directory for the subprocess
    :param timeout: number of seconds before giving up
    '''
    assertions.list_is_type(args, str)
    assertions.is_binary(args[0])
    stdout_stderr = []
    with Popen(args, cwd=cwd, stdout=PIPE, stderr=STDOUT) as active_subprocess:
        for line in iter(active_subprocess.stdout.readline, b''):
            line_str = line.decode().strip()
            stdout_stderr.append(line_str)
            print(line_str)
        active_subprocess.wait(timeout=timeout)
        returncode = active_subprocess.returncode
    if returncode != 0:
        raise CalledProcessError(returncode, args, output=None)
    else:
        return stdout_stderr
