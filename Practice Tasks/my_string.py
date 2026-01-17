"""
I will create a string with my name on it, convert the string to title case, centeredt text and width of 30 * as fill
"""

my_string = "fredrik fjeldstad"

print(my_string)

title_string = my_string.title()

print(title_string)

centered_string = title_string.center(30, "*")

print(centered_string)

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

