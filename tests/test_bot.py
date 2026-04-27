from bot.service import add_expense, total

def test_total():
    add_expense("Test", 5)
    assert total() >= 5
