# Mathematical Syntax Validator using Pushdown Automata (PDA)

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Course](https://img.shields.io/badge/Course-CSE3217-orange)

## 📌 Project Overview
This project is developed for the **CSE 3217 - Automata Theory** course. It implements a **Pushdown Automaton (PDA)** to validate the syntax of mathematical expressions containing arithmetic operators (`+`, `*`), operands (`n`), and nested parentheses `( )`.

Unlike simple Finite Automata (DFA/NFA), this model utilizes a **stack memory** to handle recursive structures and operator precedence, demonstrating the parsing logic used in compiler design.

## 🚀 Features
* **PDA Simulation:** Implements a stack-based LL(1) parsing algorithm.
* **Graphical User Interface (GUI):** User-friendly interface built with `tkinter` to input expressions and view results.
* **Step-by-Step Visualization:** Displays the stack status and current input character for every step of the parsing process.
* **Infinite Loop Protection:** Handles grammar recursion programmatically by converting Left-Recursive rules to Right-Recursive rules.
* **JFLAP Integration:** Includes the original `.jff` model file designed in JFLAP.

## 🛠️ Technologies Used
* **Python 3.x:** Core logic and GUI.
* **Tkinter:** Standard Python GUI library (no external installation required).
* **JFLAP:** Used for the theoretical modeling of the automaton.

## 📂 Project Structure

```text
CSE3217-PDA-Project/
│
├── main.py                  # Entry point to run the application
├── model.jff                # JFLAP PDA Model File
├── README.md                # Project Documentation
│
├── backend/                 # Logic Layer
│   ├── __init__.py
│   └── validator.py         # PDA Algorithm & Grammar Rules
│
└── frontend/                # Presentation Layer
    ├── __init__.py
    └── gui.py               # GUI Implementation
