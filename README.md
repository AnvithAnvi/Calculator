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
