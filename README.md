# Calculator

A simple Python calculator application built with unit tests and continuous integration using GitHub Actions.  
This project demonstrates Python development, testing, and CI/CD practices.

---

## Features

- **Core functions**: addition, subtraction, multiplication, division  
- **Extra functions**: power, modulo, floor division, absolute value, square root  
- **Automated tests**: written with `pytest`  
- **Continuous Integration**: runs tests automatically on every push with GitHub Actions  

---

## Project Structure

calc/ # calculator library code
└── calculator.py
tests/ # pytest test suite
├── conftest.py
└── test_calculator.py
.github/workflows/ # GitHub Actions CI configuration
└── ci.yml
main.py # optional GUI calculator (Tkinter)
requirements.txt # project dependencies
README.md # project documentation

yaml
Copy code

---

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/AnvithAnvi/Calculator.git
cd Calculator

python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows PowerShell

pip install -r requirements.txt
Running Tests
Run all automated tests with:

bash
Copy code
pytest -q
You should see all tests pass.
GitHub Actions also runs these tests automatically on Python 3.10, 3.11, and 3.12 whenever code is pushed.

Running the Calculator
You can launch the optional interactive calculator:

bash
Copy code
python main.py
This will open a simple calculator window (requires Python with Tk support).

Use the on-screen buttons to enter numbers and operations.

Press = to calculate.

Press C to clear.

Continuous Integration
This project uses GitHub Actions for CI.
Every push and pull request triggers the workflow defined in .github/workflows/ci.yml, which:

Installs dependencies

Runs all unit tests across multiple Python versions



License
This project is provided for educational purposes.

yaml
Copy code

---

✅ This version is safe to paste straight into `README.md`.  

Want me to also give you a **LICENSE file (MIT)** so your repo looks even more professional?




Ask ChatGPT
