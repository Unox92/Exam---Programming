"""
Task 1
"""
"""

title = "invoice"
    name = "jane doe"
    invoice_label = "invoice no:"
    amount_label = "amount due:"
    invoice_no = 12345
    address = "14 main road"
    amount_due = 4000
    header1 = "description"
    header2 = "items"
    header3 = "cost"
    header4 = "total"
    item_desc = "jumping castle"
    item_qty = 2
    item_cost = 2000
    item_total = 4000
    total_label = "total"

    # Title centered and uppercased using formatting methods
    print(title.upper().center(64))
    print()

    # Left/right blocks (name/address on left, invoice/amount on right)
    left_width = 32
    right_width = 32

    # Name line: capitalize words via title()
    left_name = name.title()
    right_invoice = f"{invoice_label.upper():<12}{invoice_no:>8}"
    print(f"{left_name:<{left_width}}{right_invoice:>{right_width}}")

    # Address + amount due
    left_addr = address
    right_amount = f"{amount_label.upper():<12}{amount_due:>8.2f}"
    print(f"{left_addr:<{left_width}}{right_amount:>{right_width}}")
    print()

    # Headers
    print(f"{header1.upper():<20}{header2.upper():>8}{header3.upper():>12}{header4.upper():>12}")
    line = "-" * 64
    print(line)

    # Item row: title-case description, numeric formatting with 2 decimals
    print(f"{item_desc.title():<20}{item_qty:>8}{item_cost:>12.2f}{item_total:>12.2f}")
    print(line)

    # Total row (right-aligned total)
    print(f"{total_label.title():<20}{'':>8}{'':>12}{amount_due:>12.2f}")
    print(line)