# quotebot

Fetch currency exchange rates and print them as a table.

## Install

```bash
pip install -r requirements.txt
pip install -e .
```

## Use

```bash
quotebot rates --base USD
quotebot convert --amount 25 --base USD --to EUR
```

## Test

```bash
pytest
```
