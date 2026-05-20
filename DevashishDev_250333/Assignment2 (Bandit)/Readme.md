# Assignment 2

## Overview
Assignment 2 focuses on Linux operating system concepts through two complementary parts: a comparative study of shells and command-line interfaces, and a practical walkthrough of the OverTheWire Bandit wargame from levels 0 to 10.
Together, these submissions build both conceptual understanding and hands-on terminal problem-solving skills.

## Part 1: Shells and Command Interfaces
The first document studies shells as the interface between the user and the operating system kernel, emphasizing how different shells vary in scripting ability, platform support, use cases, and degree of system control.
It compares CMD, PowerShell, Bash, Zsh, Fish, Anaconda Prompt, sh, and Ksh, and explains why shell choice matters for administration, automation, development, and data-science workflows.

Key ideas covered:
- Interactive vs non-interactive shells and their roles in system use and automation.
- Differences in command style, scripting support, and power level across common shells.
- Practical command equivalents across CMD, PowerShell, Bash/Zsh, and Fish for tasks such as listing files, copying, deleting, viewing content, and checking networking details.
- A ranking of shells by system control, with PowerShell and Bash identified as especially powerful in their respective ecosystems.
- Use-case-driven recommendations, such as Bash for Linux/macOS administration, PowerShell for Windows infrastructure, Fish for beginner-friendly interaction, and Anaconda Prompt for Python-focused data workflows.

## Part 2: Bandit Wargame Walkthrough
The second document presents a structured walkthrough of OverTheWire Bandit, covering the progression from initial SSH access through increasingly specific file-search and text-processing challenges up to level 10.
The emphasis is on efficient command-line reasoning rather than brute force, with each level documenting the goal, commands used, justification, and possible alternatives.

Main Linux skills demonstrated:
- Remote access using `ssh` and repeated login across levels.
- File and directory navigation using commands such as `pwd`, `ls`, `cd`, and `cat`.
- Handling unusual filenames, including names with spaces, hidden files, and files named `-`.
- Identifying files by type and attributes using `file` and `find`.
- Searching and filtering text efficiently with `grep`, `sort`, `uniq`, `strings`, and `awk`.
- Using redirection and pipelines, such as `2>/dev/null` and `|`, to refine results and suppress noise.

## Combined Learning Outcomes
Taken together, both parts of Assignment 2 show that Linux proficiency depends on both understanding the shell environment and using command-line tools effectively to solve real problems.
The shells document provides the conceptual foundation for choosing and understanding command interpreters, while the Bandit walkthrough applies that mindset to practical tasks involving navigation, filtering, search, and automation-oriented thinking.

This assignment develops core skills useful in system administration, software development, cybersecurity practice, and general Unix/Linux productivity.
In particular, Bash and related Unix tools emerge as central to Linux-based workflows because they combine scriptability, direct system interaction, and strong support for command composition.
