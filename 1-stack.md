# **Stack**
Stacks are a type of data structure in Python. When storing data to a stack you put the data you want to add to the top of the stack. Like a stack of pancakes. If you wanted the next pancake in the stack instead of the current then you would take the first pancake off to get to the second. That brings us to LIFO.
# LIFO or Last In First Out
Stacks use data in a specific order. That is that the last data added to the stack will be the first to come off the stack to be used or disposed of. We use the push and pop operations to do this.
## Functions of Stacks
To find the size of a stack you would use the size function. To do this in python you would use len. like so:
```python
size = len(stack)
```
When you use the push operation, which is .append in python, it adds the data to the stack. Like so:
```python
stack.append(value)
```
If you wanted to remove the top value of the stack you would use the pull function. In python it would be pop like so:
```python
number = stack.pop()
```
You can also loop through a stack by using a for loop in python and doing whatever you want with the data given. You could choose to print each of the values in the stack like so:
```python
for value in stack:
    print(value)
```
# Time Complexity
The time complexity for each is similiar when using a stack. When you push or pull data by using the append or pop function it is O(1) time. If you want the use and use the len function it is in O(1) time. What makes the difference is when you loop through all the data you have in the stack. This makes it O(n) time since you will go through each value and that will change the time based on the size of the stack which is n.
# Example Code
Here is an example of how you might use a stack and the different methods you could use for this situation.
```python
# Create the stack
stack = []

# Add to the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# print the size of the stack
print(len(stack))

# Remove one value from the stack and print it
print(stack.pop())

# print the stack in 2 different ways
print(stack)

for value in stack:
    print(value)
```

# Practice Problem
Create a stack and add these three prices to it: 12.99, 6.37, and 4.33. Print the size of their price list. Then remove the last price entered into the stack and print it. Then add each price left in the stack together and print it out.

[solution to problem](https://github.com/payneful/CSE212-Final/blob/main/solution/stack-solution.py)

### Other Tutorials: 
[Set](https://github.com/payneful/CSE212-Final/blob/main/2-set.md)
<br>
[Tree](https://github.com/payneful/CSE212-Final/blob/main/3-tree.md)