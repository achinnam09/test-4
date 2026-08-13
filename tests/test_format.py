from quotebot.format import as_table


def test_table_has_headers():
    output = as_table({"EUR": 0.92, "GBP": 0.79})
    assert "currency" in output and "rate" in output


def test_table_respects_limit():
    rates = {"C{}".format(i): float(i) for i in range(30)}
    lines = as_table(rates, limit=5).splitlines()
    assert len(lines) == 7
