import bcrypt
import pyperclip
from rich import panel
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich import box
import sys
console = Console()

def hasher(value):    
    try:
        hashed = bcrypt.hashpw(bytes(value, encoding="UTF-8"), bcrypt.gensalt(10))

        console.print(Panel(hashed.decode(), box=box.SQUARE), style="green")
        pyperclip.copy(hashed.decode())
        return hashed
    except KeyboardInterrupt:
        print("\n")
        console.print(Panel(Text("bye"), style="yellow", box=box.SQUARE))
        print("\n")
    except Exception as e:
        print("\n")
        console.print(Panel(Text(f"Error: {e}", style="white"), style="on red", box=box.SQUARE))
        print("\n")

if __name__ == "__main__":
    try:
        value = sys.argv[1] if len(sys.argv) > 1 else input("Value to hash: ")
        hasher(value)
    except KeyboardInterrupt:
        print("\n")
        console.print(Panel(Text("bye"), style="yellow", box=box.SQUARE))
        print("\n")
    except Exception as e:
        print("\n")
        console.print(Panel(Text(f"Error: {e}", style="white"), style="on red", box=box.SQUARE))
        print("\n")