# Notes

## Random notes

- Search engines can also be considered CLIs
- chat apps and search engines use cli like interaction things like slashes and @article{norman2007breakthrough,

-donehaskell of CLIs are often found in GUIs and websites. Like / to search
- Motivate the usage of CLIs. Uncovered features, batch processing, larger
  datasets, limited resources, ease of remote work.
- Asynchronous learnings, Computer based learning (linear learning).
- The tool should respect the GUI norm of things and such try to explain the
  cli without special knowledge and use metaphors from guis.
- Other tools have existed that aimed to personify this friendly environment
  (lisptutor)
- The shell unlike programming languages is its own environment so making a
  faithful representation of working env is prob a higher priority than when
  teaching a library or programming language.
- lesson5 typo in screenshots
- consequently, 
- progress tracking or state woudld be nice, perhaps sqlite 
- mobile version would be nice

## Feedback

Abstract:

may be worth pointing out that some modern applications in domains outside of software also use CLI (in the intro, mention explicit examples, e.g. Bloomberg terminals, STATA)

https://en.wikipedia.org/wiki/Bloomberg_Terminal#Core_Terminal

https://en.wikipedia.org/wiki/Stata#User_interface

Overview:

Start with a section with a very brief history lesson on CLI and on why the CLI
is still being used (in sw dev but also the above), why it matters etc.
(bascially what's in the abstract but with references, more examples, etc.).
Then problem description. I would also add a brief section method/approach that
describes how you ended up with "introducting cli-tutor". Just a brief summary.

Where you mention vimtutor, describe what it is and how it works in more
detail, and why it's nice (because it teaching from within itself).

But it reads very nicely in general!

## Curriculum

- What is textual interaction

- What is a shell (kind of like talking to the computer)
  - Prompt
  - Seed the interest with some cool command
    - curl something?

- How to formulate a command
  - Arguments
  - Flags
    - conventions i.e '--flag vs -f'

- Let's play with some commands
  - Examples and use cases.

- File system [chroot]
  - Meaning of '~'
  - ls, cd, touch, mkdir
  - Globbing

- Shell shortcuts
  - up arrow
  - tab-completion
  - history
  - double bang

- How to help yourself?
  - man pages

<!-- TODO: Rewrite -->
- Sticky situations extras.
  - set x
  - quoting
  - jobs, ps
  - exit status $?

- Streams: stdin, stdout stderr

- Unix pipes
  - Some simple examples of chaining

- Redirections

<!-- NOTE: How much programming knowledge can we reasonable assume? -->
- Bash
  - We said the shell evaluates commands, but what language.
  - Combining shell commands and Bash features
    - &&, ;, ||
  - Logical operators
  - Intro to scripting

- CLI Dev tools (Bonus Chapter)
  - jq
  - xml lint

## Should cover

- [x] ls
- [x] cd
- [x] touch
- [x] rm
- [x] man
- [x] wc
- [x] cat
- [ ] head
- [ ] tail
- [ ] find
- [ ] grep
- [ ] sed
- [ ] awk
- [ ] cut

## References

- [bashmanual](https://www.gnu.org/software/bash/manual/bash.pdf)
- [xinybash](https://learnxinyminutes.com/docs/bash/)
- [soups](https://www.usenix.org/system/files/soups2019-voronkov.pdf)
- [readline](https://eli.thegreenplace.net/2016/basics-of-using-the-readline-library/)
