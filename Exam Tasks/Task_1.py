
"""
Task 1

The script in this task prints an invoice to the console terminal. To make it seem more "Professional" formatting is required.
"""

"""
First the appropriate strings from the task is needed to be given to a variable

"""

title = "invoice"
invoice = "invoice no: "
amnt_label = "amount due: "
descr_label = "description"
itms_lable = "items"
cost_label = "cost"
ttl_label = "total"

name = "jane doe"
invoice_nr = "12345"
addrs_label = "14 main road"
amount_due = "4000"

description_of_label = "jumping castle"
items = "2"
cost = "2000"
total = "4000"


"""
Now I need to write the correct print statements    
"""

# This prints the invoice title
print(title.upper().center(60))
print()

# This prints the second part, name, invoice no, address and amount due
print(name + (invoice + invoice_nr).upper().rjust(52))
print(addrs_label.ljust(24) + (amnt_label + amount_due).upper().rjust(35))
print()

# This prints the description, items, cost, total
print(descr_label.upper().ljust(16) + itms_lable.upper().rjust(8) + cost_label.upper().rjust(12) + ttl_label.upper().rjust(12))
print("-" * 60)

# This prints the description of the item bought, how many, the cost of one item and the total cost of two times
print(description_of_label.title().ljust(16) + items.rjust(8) + (cost + ".00").rjust(12) + (total + ".00").rjust(24))
print("-" * 60)

# This prints the totcal cost
print(ttl_label.title().ljust(48) + (total + ".00").rjust(12))
print("-" * 60)