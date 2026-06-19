# Retro Breakout Arcade Engine

An interactive, 2D arcade rendering application modeled in Python utilizing Object-Oriented Programming (OOP) inheritance hierarchies, real-time bounding box collision metrics, and vector velocity inversions.

## 🚀 Architectural Blueprint & Game Loop Mechanics
* **De-coupled Component Matrices:** Engineered using distinct state classes (`Paddle`, `Ball`, `Brick`, `Scoreboard`) inherited directly from the native `turtle.Turtle` graphics canvas object baseline.
* **Vector Reflection System:** Tracks continuous runtime coordinate interception vectors. Whenever the coordinate bounding parameters intersect with an active brick dimension, a physics function immediately flips the directional delta parameter step ($v_y \rightarrow -v_y$) to reflect the ball velocity cleanly.
* **Dynamic Canvas Teleportation Processing:** To optimize runtime performance arrays without continually destroying data variables, destroyed brick elements are instantly reassigned to outer space coordinate parameters ($x:2000, y:2000$) off-screen.

## 🛠️ Software Stack
* **Language Environment:** Python 3.x
* **Core Modules Used:** Turtle Graphics Canvas Engine, Time (Frame State Tracker Limits)
