import click

from .client import RateClient
from .format import print_conversion, print_rates


@click.group()
@click.version_option("1.0.0")
def main():
    """quotebot command line interface."""


@main.command()
@click.option("--base", default="USD", help="Base currency")
def rates(base):
    """Print the latest exchange rates."""
    print_rates(RateClient().latest(base), base)


@main.command()
@click.option("--amount", type=float, required=True)
@click.option("--base", default="USD")
@click.option("--to", "to_currency", required=True)
def convert(amount, base, to_currency):
    """Convert an amount between two currencies."""
    result = RateClient().convert(amount, base, to_currency)
    print_conversion(amount, base, to_currency, result)


if __name__ == "__main__":
    main()
