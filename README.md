# 🧠 Holberton School — Interview Preparation

> Classic algorithmic interview challenges, solved step by step in Python.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Code style](https://img.shields.io/badge/code%20style-pycodestyle-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Status](https://img.shields.io/badge/status-work%20in%20progress-orange)

---

## 📖 Description & objectives

This repository gathers the **algorithmic challenges** I solved as part of the
[Holberton School](https://www.holbertonschool.com/) curriculum to prepare for
**technical interviews**. Each folder is a self-contained problem focusing on a
classic problem-solving pattern.

**Objectives:**

- Break a problem down before writing any code
- Analyze time and space complexity
- Choose the right data structure for the job
- Write clean, readable and well-documented Python

---

## 📂 Features — the challenges

| Project | Description | Key concepts |
| ------- | ----------- | ------------ |
| [`pascal_triangle`](./pascal_triangle) | Generate Pascal's triangle up to `n` rows | Lists, nested loops |
| [`lockboxes`](./lockboxes) | Determine whether all locked boxes can be opened using the keys found inside them | Graph traversal (BFS/DFS) |
| [`minimum_operations`](./minimum_operations) | Compute the fewest *Copy All* / *Paste* operations needed to get exactly `n` characters | Prime factorization |
| [`log_parsing`](./log_parsing) | Read logs from `stdin` and print running statistics (total file size, status code counts) | Stream processing, `Ctrl+C` handling |
| [`utf8_validation`](./utf8_validation) | Check whether a list of integers represents a valid UTF-8 encoding | Bitwise operations, encoding |
| [`nqueens`](./nqueens) | Find every way to place `N` non-attacking queens on an `N×N` chessboard | Backtracking, recursion |

---

## 🛠️ Technologies

| Tool | Usage |
| ---- | ----- |
| **Python 3** | Language used for every solution |
| **pycodestyle** | Linter (PEP 8 style checks) |
| **Git & GitHub** | Version control, branch strategy |

---

## ✅ Requirements

- **OS:** Ubuntu 20.04 LTS or macOS
- **Python:** 3.8 or higher
- **Linter:** `pycodestyle` 2.x — `pip install pycodestyle`
- No external library needed: only the Python standard library is used

---

## ⚙️ Installation

```bash
git clone https://github.com/The-TO/holbertonschool-interview.git
cd holbertonschool-interview
```

Make sure the scripts are executable:

```bash
chmod +x */*.py
```

---

## 🚀 Usage

Each folder contains the solution and, when available, a `*-main.py` test file.

**Example — N Queens:**

```bash
cd nqueens
./0-nqueens.py 4
```

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

**Example — Pascal's triangle:**

```bash
cd pascal_triangle
./0-main.py
```

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

---

## 📝 Code standards

- **Style:** [PEP 8](https://peps.python.org/pep-0008/), checked with `pycodestyle`
- **Documentation:** every module and function has a docstring following
  [PEP 257](https://peps.python.org/pep-0257/)

```bash
pycodestyle */*.py
```

---

## 🌿 Branch strategy

| Branch | Purpose |
| ------ | ------- |
| `main` | Stable, validated solutions |
| `dev` | Work in progress on new challenges |
| `test` | Testing solutions before merging into `main` |

Commit messages follow the [Conventional Commits](https://www.conventionalcommits.org/) style
(`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`).

---

## 🙏 Acknowledgements

- [Holberton School](https://www.holbertonschool.com/) for the project subjects
- My peers for the code reviews and debugging sessions

---

## 👤 Author

**Théo** — Software development student at Holberton School
GitHub: [@The-TO](https://github.com/The-TO)

## 📄 License

This project is licensed under the MIT License — see [`LICENSE`](./LICENSE).

> 🚧 Work in progress — new challenges are added as the curriculum goes on.