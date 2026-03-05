import pytest
from inventory import add_item, remove_item, get_item_count

def test_add_item(empty_inventory):
    result = add_item(empty_inventory, "automobile")
    assert result["item"] == ["automobile"]

def test_add_item_empty(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory,"")

def test_add_item_number(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, 3301)

def test_add_item_capacity(empty_inventory):
    empty_inventory["capacity"] = 2
    add_item(empty_inventory, "BMW")
    add_item(empty_inventory, "Audi")
    with pytest.raises(ValueError):
        add_item(empty_inventory, "Merc")

def test_add_item_locked(empty_inventory):
    empty_inventory["locked"] = True
    result = add_item(empty_inventory, "Jeep")
    assert result["item"] == []
