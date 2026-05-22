---
name: Bug Report
about: Something is broken
title: ''
labels: bug
assignees: ''
---

**What is broken:**
The talker and listener nodes launch successfully, but the listener never receives or prints any messages.

**What you expected:**
The listener node should receive and display messages published by the talker node.

**Steps to reproduce:**
1. Build the package
2. Source the workspace
3. Run: ros2 launch basic_comms comms.launch.py
4. Observe that the listener node does not print received messages
