# Lights Out Game (BFS Solver)

A desktop implementation of the classic puzzle game **Lights Out** developed using **Python** and **Tkinter**.

The game includes an integrated AI solver powered by the **Breadth-First Search (BFS)** algorithm to calculate the minimum number of moves required to solve the puzzle optimally.

---

## Features

### Solvable Puzzle Generation

* Generates only mathematically solvable board configurations
* Uses randomized reverse-move generation logic

### Multiple Difficulty Levels

* Easy Mode (3x3 Grid)
* Hard Mode (4x4 Grid)

### BFS AI Solver

* Calculates the optimal solution path
* Displays the minimum required moves to solve the board

### Auto-Solver Animation

* Visualizes the solving process automatically
* Uses Python threading to maintain a smooth and responsive UI

### Move Counter

* Tracks player moves in real time
* Compares user performance against the optimal solution

---

## Tech Stack

* Python 
* Tkinter
* Breadth-First Search (BFS)
* Python Threading

---

## Project Structure

```bash
├── main.py
```

---

## Game Mechanics

The game consists of a grid of lights.

When a player clicks a cell:

* The selected light toggles its state
* The adjacent lights (up, down, left, right) also toggle

The objective is to turn all lights off using the fewest possible moves.

---

## BFS Solver Overview

The AI solver treats each board configuration as a unique state within a graph.

Using Breadth-First Search:

* Each move generates a neighboring state
* States are explored level-by-level
* The first discovered solution guarantees the minimum number of moves

This ensures that the solver always finds the optimal solution path.


---

## Educational Purpose

This project was developed for educational purposes to demonstrate:

* Breadth-First Search (BFS)
* State-space search problems
* Graph traversal algorithms
* Puzzle-solving logic
* GUI development using Tkinter
* Thread-based asynchronous UI updates
