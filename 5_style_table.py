from rich.console import Console
from rich.table import Table

console = Console()

# Create a styled table
table = Table(title="User Data")

table.add_column("Name", justify="right", style="cyan", no_wrap=True)
table.add_column("Age", justify="center", style="magenta")
table.add_column("Balance", justify="right", style="green")

table.add_row("Alice", "30", "$153.75")
table.add_row("Bob", "25", "$89.12")
table.add_row("Charlie", "35", "$240.50")

# Print the table with styling
console.print(table)
