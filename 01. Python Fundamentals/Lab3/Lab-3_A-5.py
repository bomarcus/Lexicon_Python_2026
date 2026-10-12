# Lab-3_A-4

# Create a shipping rule based on order total and whether the customer is a member.
#  Use and/or.


order_total = 600
is_member = True

if order_total > 200 and not is_member or order_total > 100 and is_member:
    print("Shipping!")
