from bot.service import add_expense, total, by_category

def test_total():
    add_expense("Test", 5)
    assert total() >= 5

def test_category():
    add_expense("Food", 10, "food")
    result = by_category("food")
    assert len(result) > 0
