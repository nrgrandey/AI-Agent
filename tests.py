from functions.run_python import run_python_file
import os


print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["5", "3"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))
