#!/usr/bin/env python3

import readline
from bash_completion import bash_complete_line
from subprocess import Popen, PIPE

cache = {}

def make_completer(vocabulary):
    # Caching completions because the custom_complete function
    # is called many times over, see
    # https://docs.python.org/3/library/readline.html#readline.set_completer
    # Not a real solution, because completions can change depending on context
    def custom_complete(text, state):
        if text in cache:
            results = cache[text]
        else:
            results = bash_complete_line(text, return_line=True)
            results = [x for x in results] + [None]
            cache[text] = results
        return results[state] + " "
    return custom_complete

def main():
    vocabulary = {'ls', 'uname', 'cat', 'unalias', 'cd', 'vim'}
    readline.parse_and_bind('tab: complete')
    readline.set_completer(make_completer(vocabulary))

    try:
        while True:
            s = input('# ').strip()
            try:
                if s.split()[0] not in vocabulary:
                    print("Let's stick to the basics for now")
                    continue
            except:
                continue # no input
            p = Popen(s, shell=True, executable='/bin/bash', stdout=PIPE)
            stdout, stderr = p.communicate()
            print(stdout.decode("utf-8"), end='')
    except (EOFError, KeyboardInterrupt) as e:
        print('\nShutting down...')

if __name__ == '__main__':
    main()
