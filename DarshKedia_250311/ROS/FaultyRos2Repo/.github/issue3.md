---
name: Bug Report
about: Something is broken
title: ''
labels: bug
assignees: ''
---

**What is broken:**
Running the ROS2 launch file fails immediately because the specified executable cannot be found.

**What you expected:**
The launch file should successfully start both the talker and listener nodes.

**Steps to reproduce:**
1. Build the package
2. Source the workspace
3. Run: ros2 launch basic_comms comms.launch.py
4. Observe launch failure with executable not found error
