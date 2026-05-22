---
name: Bug Report
about: Something is broken
title: ''
labels: bug
assignees: ''
---

**What is broken:**
The ROS2 package fails to build using colcon build. Compilation and linker errors occur due to incorrect message types and missing ROS2 dependencies.

**What you expected:**
The package should compile successfully and generate the talker and listener executables.

**Steps to reproduce:**
1. Clone the repository
2. Source the ROS2 environment
3. Run: colcon build --symlink-install
4. Observe compilation and linker errors during the build process
