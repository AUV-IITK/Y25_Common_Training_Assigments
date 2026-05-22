---
name: Bug Report
about: Something is broken
title: ''
labels: bug
assignees: ''
---

**What is broken:**
The repository does not contain a .gitignore file, causing ROS2 build artifacts to appear in version control. The README also lacks build and run instructions.

**What you expected:**
The repository should ignore generated workspace artifacts and provide clear setup, build, and execution instructions for contributors.

**Steps to reproduce:**
1. Clone the repository
2. Build the workspace
3. Observe generated build/, install/, and log/ directories appearing in git status
4. Check README and observe missing build/run instructions
