import bcrypt
from rich import panel
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import sys
console = Console()

def hasher(value):    
    try:
        hashed = bcrypt.hashpw(bytes(value, encoding="UTF-8"), bcrypt.gensalt(10))

        console.print(Panel(hashed.decode()), style="green")
    except KeyboardInterrupt:
        print("\n")
        console.print(Panel(Text("bye"), style="yellow"))
        print("\n")
    except Exception as e:
        print("\n")
        console.print(Panel(Text(f"Error: {e}", style="white"), style="on red"))
        print("\n")

if __name__ == "__main__":
    try:
        value = sys.argv[1] if len(sys.argv) > 1 else input("Value to hash: ")
        hasher(value)
    except KeyboardInterrupt:
        print("\n")
        console.print(Panel(Text("bye"), style="yellow"))
        print("\n")
    except Exception as e:
        print("\n")
        console.print(Panel(Text(f"Error: {e}", style="white"), style="on red"))
        print("\n")
if __name__ == "__init__":
    value = sys.argv[1] if len(sys.argv) > 1 else input("Value to hash: ")
    hasher(value)