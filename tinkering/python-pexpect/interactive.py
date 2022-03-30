#!/usr/bin/env python3

import pexpect, struct, fcntl, termios, signal, sys
from termcolor import cprint

# This is to adjust the window size when resizing the terminal
def get_terminal_size():
    s = struct.pack("HHHH", 0, 0, 0, 0)
    a = struct.unpack('hhhh', fcntl.ioctl(
                      sys.stdout.fileno(), termios.TIOCGWINSZ, s))
    return a[0], a[1]

# def sigwinch_passthrough(sig, data):
#     global p
#     if not p.closed:
#         p.setwinsize(*get_terminal_size())

# allowed commands
vocabulary = {'ls', 'uname', 'man', 'mkdir', 'cat', 'unalias', 'cd', 'vim'}
# everything's in bytes, not str
vocabulary = {str.encode(s) for s in vocabulary}


INPUT_BUFFER = b""

# detect when leaving the shell into a nested environment
NESTED = False

# 
def input_filter(input_byte):
    """
    Recieves input byte by byte on keypress in the interactive session
    bytes are directly sent to the underlying bash shell
    so that tab-completion and everything else works
    """
    global INPUT_BUFFER, NESTED

    # so we add each byte to a buffer before sending it to bash
    INPUT_BUFFER+=input_byte



    # but if the user hits return, we check the entire input buffer
    # unless we're in a nested environment (like vim, man, etc.)
    if input_byte == b'\r' and not NESTED:
        tokens = INPUT_BUFFER.split()
        print('\nINPUT BUFFER: ',tokens)
        # clear the input buffer
        INPUT_BUFFER = b""
        try:
            # Handle up arrow
            if b'\x1b[A' in tokens[0]:
                return input_byte

            # restrict permitted commands
            if tokens[0] not in vocabulary:
                # print("\r\nLet's stick to the basics for now\r")
                cprint("\r\n[TUTOR]: Let's stick to the basics for now\r", 'cyan', attrs=['bold'])
                return b"\x03" # not sure how to hide the ^C

            # if we're going into a nested environemnt like vim
            # need to disable the filtering
            if tokens[0] == b'vim':
                NESTED = True
            # not sure how to reset nested = False when exiting,
            # maybe mess with bash's job management or check $?

            return input_byte
        # user didn't enter any command, just return
        except IndexError:
            return input_byte
    else:
        return input_byte

def output_filter(output):
    """
    Recieves output from the interactive session

    """
    # we can intercept output from the shell to add or change stuff
    if b"invalid option" in output:

        cprint("\r\n[TUTOR]:  TIP: Try typing 'man' followed by the command name to learn more \r", 'yellow', attrs=['bold'])

        cprint("\r\n[ERROR Message]: \r", 'red', attrs=['bold'])
        # output += b"\nTIP: Try typing 'man' followed by the command name to learn more\r\n"
    return output
print('tutor starting')

p = pexpect.spawn('/bin/bash')
p.setwinsize(*get_terminal_size())
# signal.signal(signal.SIGWINCH, sigwinch_passthrough)
p.interact(input_filter=input_filter, output_filter=output_filter)
p.kill(1)

print('tutor has ended')

