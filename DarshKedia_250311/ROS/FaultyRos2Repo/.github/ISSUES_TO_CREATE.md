# Pre-written GitHub Issues

---

## Issue #1 — "Package fails to build"
**Label:** bug  

The package does not build with `colcon build`. There are errors during compilation.
Figure out what is missing and fix it so the package builds cleanly.

---

## Issue #2 — "Nodes launch but no messages are received"
**Label:** bug  

When running the launch file (after fixing the build), the talker and listener nodes
start but the listener never prints anything. Investigate why messages are not flowing
between the two nodes.

---

## Issue #3 — "Launch file crashes immediately"
**Label:** bug  

Running `ros2 launch basic_comms comms.launch.py` results in an error and the launch
fails before the nodes even start. Find and fix the problem in the launch file.

---

## Issue #4 — "Repo needs proper Git hygiene"
**Label:** good-first-issue  

- There is no `.gitignore` file. The `build/`, `install/`, and `log/` folders
  should never be committed to the repo. Add a proper `.gitignore`.
- The README has no build or run instructions. Add clear steps so anyone can
  clone and run this package.
- Create a new branch, make your changes, and open a Pull Request.
