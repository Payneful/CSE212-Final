# Create two sets/"carts"
cart_1 = set()
cart_2 = set()

# Add 3 items to each set/"cart"
cart_1.add('bananas')
cart_1.add('apples')
cart_1.add('donuts')

cart_2.add('skittles')
cart_2.add('chocolate')
cart_2.add('popsicles')

# Print out each set/"cart"
print(f'cart1: {cart_1}')
print(f'cart2: {cart_2}')

# Print out same values
cart_same = cart_1 & cart_2
print(f'Same values: {cart_same}')

# Print out different values
cart_different = cart_1 ^ cart_2
print(f'Different values: {cart_different}')

# Add both carts together
cart_together = cart_1 | cart_2
print(f'All values: {cart_together}')