"""Create error-handled subprocess that runs in specific directory

This module provides a function that error handles subprocess
calls and runs the subprocess in a specific working directory.
This is functionality is important for Latex, because:

1) Most build tools for Latex are not written in Python
2) Because they create many files, latex commands should be run
in the same directory as the latex file that is being built
"""

from subprocess import Popen, CalledProcessError, PIPE
from . import assertions

def check_output_cwd(args, cwd, timeout=None):
    '''Open a subprocess in another working directory

    Raises ValueError if system binary does not exist
    Raises CalledProcessError if the return code is non-zero

    :returns: a tuple of standard output and standard error from subprocess

    :param args: a list of command line arguments for subprocess
    :param cwd: the working directory for the subprocess
    :param timeout: number of seconds before giving up
    '''
    assertions.list_is_type(args, str)
    assertions.is_binary(args[0])
    with Popen(args, cwd=cwd, stdout=PIPE) as active_subprocess:
        active_subprocess.wait(timeout=timeout)
        stdout, stderr = active_subprocess.communicate()
        returncode = active_subprocess.returncode
    if returncode != 0:
        raise CalledProcessError(returncode, args, output=None)
    else:
        return (stdout, stderr)
