# 🧠 Holberton School — Interview Preparation

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-work%20in%20progress-orange)

A collection of **algorithmic challenges** solved in **Python** as part of the
[Holberton School](https://www.holbertonschool.com/) curriculum.
These exercises are designed to prepare for **technical interviews**: each one
focuses on a classic problem-solving pattern (recursion, backtracking, graph
traversal, bit manipulation, parsing, etc.).

---

## 📂 Projects

| Project | Description | Key concepts |
| ------- | ----------- | ------------ |
| [`pascal_triangle`](./pascal_triangle) | Generate Pascal's triangle up to `n` rows | Lists, nested loops |
| [`lockboxes`](./lockboxes) | Determine whether all locked boxes can be opened using the keys found inside them | Graph traversal (BFS/DFS) |
| [`minimum_operations`](./minimum_operations) | Compute the fewest *Copy All* / *Paste* operations needed to get exactly `n` characters | Prime factorization, math reasoning |
| [`log_parsing`](./log_parsing) | Read logs from `stdin` and print running statistics (total file size, status code counts) | Stream processing, signal handling (`Ctrl+C`) |
| [`utf8_validation`](./utf8_validation) | Check whether a list of integers represents a valid UTF-8 encoding | Bitwise operations, encoding |
| [`nqueens`](./nqueens) | Find every way to place `N` non-attacking queens on an `N×N` chessboard | Backtracking, recursion |

---

## 🛠️ Requirements

- Ubuntu 20.04 LTS / macOS
- Python 3 (3.8+)
- Code style: [pycodestyle](https://pypi.org/project/pycodestyle/)
- Every file starts with `#!/usr/bin/python3` and is executable

---

## 🚀 Usage

Clone the repository:

```bash
git clone https://github.com/The-TO/holbertonschool-interview.git
cd holbertonschool-interview
```

Each folder contains the solution and, when available, a `*-main.py` test file.
For example:

```bash
cd nqueens
./0-nqueens.py 4
```

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

---

## 🎯 Learning objectives

- Break a problem down before writing any code
- Analyze time and space complexity
- Choose the right data structure for the job
- Write clean, readable and well-documented Python

---

## 👤 Author

**Théo** — Software development student at Holberton School
GitHub: [@The-TO](https://github.com/The-TO)

> 🚧 Work in progress — new challenges are added as the curriculum goes on.