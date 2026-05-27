# 🧮 Python Terminal Calculator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Level](https://img.shields.io/badge/Level-Beginner-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A clean, beginner-friendly Python calculator that runs in the terminal. Built as a portfolio project to practice **functions**, **loops**, **conditionals**, and **input validation**.

---

## ✨ Features

- ➕ Addition, ➖ Subtraction, ✖️ Multiplication, ➗ Division
- 🔄 Continuous loop — calculate as many times as you want
- 🛡️ Input validation — handles letters, symbols, and empty input gracefully
- ❌ Division-by-zero protection with a friendly error message
- 🚪 Type `exit` at any prompt to quit safely
- 🎨 Clean, formatted terminal output

---

## 📸 Preview

```
========================================
   🧮  PYTHON CALCULATOR  🧮
========================================
  Operations: +  -  *  /
  Type 'exit' at any prompt to quit.
========================================

  New Calculation
────────────────────────────────────────
  Enter first number:  12
  Enter operator (+, -, *, /): *
  Enter second number: 7
────────────────────────────────────────
  12 * 7 = 84
────────────────────────────────────────
```

---

## 📁 Project Structure

```
python-calculator/
│
├── calculator.py       # Main application
├── README.md           # Project documentation
├── requirements.txt    # Dependencies (none — pure Python!)
└── .gitignore          # Files Git should ignore
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher — [Download Python](https://www.python.org/downloads/)
- No external libraries needed!

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/your-username/python-calculator.git

# 2. Navigate into the project folder
cd python-calculator

# 3. Run the calculator
python calculator.py
```

### Run in VS Code

1. Open VS Code and go to **File → Open Folder** — select the `python-calculator` folder
2. Open `calculator.py` in the editor
3. Press **`Ctrl + \`` ** (backtick) to open the integrated terminal
4. Type `python calculator.py` and press **Enter**

---

## 🏗️ How It's Built

The project is structured around six clear sections, each serving one purpose:

| Section | Purpose |
|---|---|
| `add / subtract / multiply / divide` | Pure math functions, one job each |
| Display helpers | All `print` logic in one place |
| Input functions | Validate user input before using it |
| `calculate()` | Routes operator to the right function |
| `main()` | The main loop tying everything together |
| `if __name__ == "__main__"` | Python entry-point best practice |

---

## 🔮 Future Improvements

- [ ] Add exponentiation (`**`) and modulo (`%`) operators
- [ ] Store and display a **calculation history**
- [ ] Build a **GUI version** using `tkinter`
- [ ] Add **unit tests** with `pytest`
- [ ] Support **chained calculations** (use previous result as next input)
- [ ] Add a **scientific mode** (sqrt, sin, cos, log)

---

## 🧠 Concepts Practiced

- Python functions and docstrings
- `while` loops and `break`
- `if / elif / else` conditionals
- `try / except` for error handling
- f-strings for formatted output
- Input validation patterns
- `__name__ == "__main__"` entry point

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your Name](https://linkedin.com/in/your-profile)

---

> Built with ❤️ and Python — a beginner portfolio project.