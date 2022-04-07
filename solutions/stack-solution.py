# Create a stack
stack = []

# Add 12.99, 6.37, and 4.33 to the stack
stack.append(12.99)
stack.append(6.37)
stack.append(4.33)

# Print the size
print(f"Size of Stack: {len(stack)}")

# Remove the last value entered
print(f"price: {stack.pop()}")

# Add stack values and print it out
print(f"Sum of the Stack: {sum(stack)}")