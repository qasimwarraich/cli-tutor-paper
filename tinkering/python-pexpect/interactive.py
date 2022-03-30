#!/usr/bin/env python3

import pexpect, struct, fcntl, termios, signal, sys

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
input_buffer = b""

# detect when leaving the shell into a nested environment
nested = False

# bytes are directly sent to the underlying bash shell
# so that tab-completion and everything else works
def input_filter(s):
    global input_buffer, nested
    # so we add each byte to a buffer before sending it to bash
    input_buffer+=s
    # but if the user hits return, we check the entire input buffer
    # unless we're in a nested environment (like vim, man, etc.)
    if s == b'\r' and not nested:
        tokens = input_buffer.split()
        # clear the input buffer
        input_buffer = b""
        try:
            # restrict permitted commands
            if tokens[0] not in vocabulary:
                print("\r\nLet's stick to the basics for now\r")
                return b"\x03" # not sure how to hide the ^C
            else:
                # if we're going into a nested environemnt like vim
                # need to disable the filtering
                if tokens[0] == b'vim':
                    nested = True
                # not sure how to reset nested = False when exiting,
                # maybe mess with bash's job management or check $?
                return s
        # user didn't enter any command, just return
        except IndexError:
            return s
    else:
        return s

def output_filter(s):
    # we can intercept output from the shell to add or change stuff
    if b"invalid option" in s:
        s += b"\nTIP: Try typing 'man' followed by the command name to learn more\r\n"
    return s

print('tutor starting')

p = pexpect.spawn('/bin/bash')
p.setwinsize(*get_terminal_size())
# signal.signal(signal.SIGWINCH, sigwinch_passthrough)
p.interact(input_filter=input_filter, output_filter=output_filter)
p.kill(1)

print('tutor has ended')

