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

- Abstract
 - Overview
   - problem description
   - introduce tool
   - outline thesis
 - Introduction
- Tool
  - overview
  - web version
- Design and Implementation
  - overview
  - architecture
  - architecture of web-tool
- User Study
- Related Work and Reflections
  - related work
  - future work
- Conclusion
- Appendix
  - Detailed dev considerations

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
