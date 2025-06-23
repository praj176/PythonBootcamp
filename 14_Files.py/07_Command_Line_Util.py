'''
A command-line utility is a Python script you run from the terminal, like built-in commands, that takes arguments and performs tasks like automation, file handling, or system checks.
| Module     | Purpose                             |
| ---------- | ----------------------------------- |
| `sys`      | Access raw command-line arguments   |
| `argparse` | Parse arguments in a clean way      |
| `click`    | Build modern, user-friendly tools   |
| `typer`    | Even simpler and modern CLI builder |

eg. pip install pandas → pip is a command-line utility
'''
# greet.py
import argparse

parser = argparse.ArgumentParser(description="Greets the user")
parser.add_argument('--name', type=str, help='Your name')
args = parser.parse_args()

print(f"Hello, {args.name}!")
