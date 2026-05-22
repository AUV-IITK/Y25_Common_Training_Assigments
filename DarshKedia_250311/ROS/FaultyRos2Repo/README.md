# basic_comms

A ROS2 package for robot communication.

## What it does

There is a talker node and a listener node. The talker sends messages. The listener receives them.

## Requirements

- ROS2 (tested on Humble)
- colcon

## Notes

- Something might not work. Check the code.
- Launch file is in the `launch/` folder.
- Good luck.

## Clone Repository

```bash
git clone https://github.com/AUV-IITK/FaultyRos2Repo.git
cd FaultyRos2Repo
```

## Build Instructions

```bash
source /opt/ros/humble/setup.bash

colcon build --symlink-install
```

## Source Workspace

```bash
source install/setup.bash
```

## Run Package

```bash
ros2 launch basic_comms comms.launch.py
```

## Expected Output

```text
[talker]: Publishing: 'Hello ROS2! Count: 0'
[listener]: Received: 'Hello ROS2! Count: 0'
```