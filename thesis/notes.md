# Notes

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

## Existing literature

- Mostly very old papers
- If there is a comparison it is usually in the realm of network engineers not newbies.

## Look into

- Bash readline
- Capturing bash commands

## Paper structure

## Outline

- [x] Abstract
- [x] Overview
  - [x] problem description
      - [x] potential solution
  - [x] introduce tool
  - [x] outline thesis
- [x] Introduction
  - [ ] Interactive learning tools
  - [ ] Requirements
      - [x] RQs
- [ ] Tool (CLI-Tutor)
  - [ ] overview
      - [ ] cirriculum
      - [ ] lesson design
      - [ ] usability considerations
      - [ ] safety considerations
  - [ ] web version
- [ ] Design and Implementation
  - [ ] overview
  - [ ] original tinkering and considerations
  - [ ] features and considerations
      - [ ] readline
      - [ ] golang
      - [ ] logging
      - [ ] extensibility
      - [ ] embedded files
          - [ ] Running examples
      - [ ] usability 
  - [ ] architecture of cli-tool
  - [ ] architecture of web-tool
      - [ ] how sandboxing is achieved
- [ ] User Study
   - [ ] methodology
      - [ ] assignment
      - [ ] survey structure
   - [ ] participants
   - [ ] findings
- [ ] Related Work and Reflections
  - [ ] related work
  - [ ] future work
      - [ ] improvements to CLI-Tutor
      - [ ] areas to explore in the space
- [ ] Conclusion
- [ ] Appendix
  - [x] Survey questions
  - [ ] Detailed dev considerations

# Random notes

- Search engines can also be considered CLIs
- Elements of CLIs are often found in GUIs and websites. Like / to search
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

## Sample format

```tex

\chapter{Introduction}
\section{Section}
%
\subsubsection{Subsubsection}
\fig[.5\textwidth]{seal_blue}{seal logo}{logo}

\subsection{Subsection}
%

% NOTE: What are use cases for paragraphs like this or are they in place of
% list items as in the proposal.

% NOTE: Paragraphs titles should always have a point (.) after the title.
\paragraph{Paragraph.} Always with a point.

\begin{lstlisting}[caption=An example code snippet]
/**
 * Javadoc comment
 */
public class Foo {
	// line comment
	public void bar(int number) {
		if (number < 0) {
			return; /* block comment */
		}
	}
}
\end{lstlisting}


\section{Curriculum}

The Curriculum is an important part of defining such a tool 

\section{Interactive Learning Tool}

The Curriculum is an important part of defining such a tool 


```
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
