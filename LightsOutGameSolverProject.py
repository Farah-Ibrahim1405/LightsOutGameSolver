import random  
import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread

def generate_solvable_grid(size, moves_count=10):
    grid = [[0]*size for _ in range(size)]
    for _ in range(moves_count):
        r = random.randint(0, size-1)
        c = random.randint(0, size-1)
        for dr, dc in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
            rr, cc = r+dr, c+dc
            if 0 <= rr < size and 0 <= cc < size:
                grid[rr][cc] ^= 1
    return grid

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

def tuple_to_board(board_tup):
    return [list(row) for row in board_tup]

def generate_neighbors(grid):
    size = len(grid)
    neighbors = []
    for row in range(size):
        for col in range(size):
            new_grid = [r[:] for r in grid]
            for dr, dc in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = row + dr
                c = col + dc
                if 0 <= r < size and 0 <= c < size:
                    new_grid[r][c] ^= 1
            neighbors.append((tuple(tuple(r) for r in new_grid), (row, col)))
    return neighbors

def bfs_solve(start_grid):
    start = board_to_tuple(start_grid)
    size = len(start_grid)
    target = tuple(tuple(0 for _ in range(size)) for _ in range(size))
    queue = [start]
    visited = {start}
    parent = {start: None}
    move_used = {start: None}
    while queue:
        current = queue.pop(0)
        if current == target:
            path = []
            while move_used[current] is not None:
                path.append(move_used[current])
                current = parent[current]
            return path[::-1]
        grid = tuple_to_board(current)
        for new_state, move in generate_neighbors(grid):
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)
                parent[new_state] = current
                move_used[new_state] = move
    return None

# =====GUI=====
class LightsOutGUI:
    def __init__(self, master):
        self.master = master
        master.title("Lights Out (BFS Mode)")
        self.size = None
        self.grid = None
        self.moves = 0
        self.optimal = 0
        self.buttons = []
        self.create_menu()

    def clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def create_menu(self):
        self.clear()
        self.master.configure(bg="#001f3f")
        tk.Label(self.master, text="Select Difficulty", font=("Arial", 16), bg="#001f3f", fg="white").pack(pady=10)
        tk.Button(self.master, text="Easy (3x3)", width=10, height=2, bg="#7FDBFF", command=lambda: self.start_game(3)).pack(pady=5)
        tk.Button(self.master, text="Hard (4x4)", width=10, height=2, bg="#7FDBFF", command=lambda: self.start_game(4)).pack(pady=5)

    def start_game(self, size):
        self.size = size
        self.grid = generate_solvable_grid(size) 
        path = bfs_solve(self.grid)
        self.optimal = len(path) if path else "No Solution"
        self.moves = 0
        self.show_game()

    def show_game(self):
        self.clear()
        self.master.configure(bg="#001f3f") 
        info_frame = tk.Frame(self.master, bg="#001f3f")
        info_frame.pack(pady=5)
        self.moves_label = tk.Label(info_frame, text=f"Moves: {self.moves}", font=("Arial",12), bg="#001f3f", fg="white")
        self.moves_label.grid(row=0, column=0, padx=10)
        self.opt_label = tk.Label(info_frame, text=f"Optimal: {self.optimal}", font=("Arial",12), bg="#001f3f", fg="white")
        self.opt_label.grid(row=0, column=1, padx=10)

        grid_frame = tk.Frame(self.master, bg="#001f3f")
        grid_frame.pack()
        self.buttons = []
        for r in range(self.size):
            row = []
            for c in range(self.size):
                color = "yellow" if self.grid[r][c] == 1 else "black"
                btn = tk.Button(grid_frame, bg=color, width=6, height=3, command=lambda r=r, c=c: self.click(r, c))
                btn.grid(row=r, column=c, padx=2, pady=2)
                row.append(btn)
            self.buttons.append(row)

        ctrl = tk.Frame(self.master, bg="#001f3f")
        ctrl.pack(pady=10)
        tk.Button(ctrl, text="Solve", bg="#7FDBFF", command=self.solve).grid(row=0, column=0, padx=5)
        tk.Button(ctrl, text="Randomize", bg="#7FDBFF", command=lambda: self.start_game(self.size)).grid(row=0, column=1, padx=5)
        tk.Button(ctrl, text="Back", bg="#7FDBFF", command=self.create_menu).grid(row=0, column=2, padx=5)

    def click(self, r, c, user_move=True):
        for dr, dc in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                self.grid[nr][nc] ^= 1
                color = "yellow" if self.grid[nr][nc] == 1 else "black"
                self.buttons[nr][nc].config(bg=color)
        if user_move:
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")

    def solve(self):
        path = bfs_solve(self.grid)
        if not path:
            messagebox.showinfo("No Solution", "This puzzle has no solution!")
            return
        def anim():
            for r, c in path:
                self.click(r, c, user_move=False)
                time.sleep(0.3)
        Thread(target=anim).start()

# Run the GUI
root = tk.Tk()
root.geometry("400x500")
app = LightsOutGUI(root)
root.mainloop()
