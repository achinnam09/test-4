from rich.console import Console
from tabulate import tabulate

console = Console()


def as_table(rates, limit=20):
    rows = sorted(rates.items())[:limit]
    return tabulate(rows, headers=["currency", "rate"], floatfmt=".4f")


def print_rates(rates, base="USD"):
    console.print("[bold]Rates for {}[/bold]".format(base))
    console.print(as_table(rates))


def print_conversion(amount, base, to, result):
    console.print("{} {} = [bold]{} {}[/bold]".format(amount, base, result, to))
