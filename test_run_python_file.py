from functions.run_python_file import run_python_file


print("--- main.py ---")
print(run_python_file("calculator", "main.py"))

print("--- main.py with argument ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("--- tests.py ---")
print(run_python_file("calculator", "tests.py"))

print("--- outside working directory ---")
print(run_python_file("calculator", "../main.py"))

print("--- nonexistent file ---")
print(run_python_file("calculator", "nonexistent.py"))

print("--- non-Python file ---")
print(run_python_file("calculator", "lorem.txt"))
