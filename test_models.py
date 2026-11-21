from models import Order, MENU

def test_line_total():
    o = Order()
    o.add_item(MENU["1"], 2)           # 45 x 2
    assert o.calculate_total() == 90

def test_quantity_zero_rejected():
    o = Order()
    try:
        o.add_item(MENU["1"], 0)
        assert False
    except ValueError:
        pass

def test_unavailable_rejected():
    o = Order()
    try:
        o.add_item(MENU["6"], 1)
        assert False
    except ValueError:
        pass

def test_remove_and_reset():
    o = Order()
    o.add_item(MENU["1"], 1)
    o.add_item(MENU["2"], 1)
    o.remove_item("1")
    assert len(o.items) == 1
    o.reset()
    assert o.calculate_total() == 0

if __name__ == "__main__":
    test_line_total(); test_quantity_zero_rejected()
    test_unavailable_rejected(); test_remove_and_reset()
    print("All tests passed!")