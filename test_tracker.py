from tracker import calculate_total

def test_calculate_total(): #normal_case
    expenses = [
        {"name" : "Coffee", "amount" : 150},
        {"name" : "Book" , "amount": 500},
        {"name" : "Chocolate", "amount" : 50}
    ]
    assert calculate_total(expenses) == 700

def test_empty_list(): #empty_list
    assert calculate_total([]) == 0

def test_single_expense(): #single_item
    expenses = [
        {"name" : "Book", "amount" : 500}
    ]
    assert calculate_total(expenses) == 500

