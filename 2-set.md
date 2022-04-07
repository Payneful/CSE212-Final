# **Set**
Sets are a type of data structure in Python. When storing data to a set it is unordered and unchangeable, but it also does not allow for any duplicate values. This is good when you want only unique values or entries.
# Mutability
Since sets are unordered it makes it difficult to find information in the traditional manner. Sets can appear in different orders everytime you use it, so you cannot use an index to look up values in the set. There are a couple different ways you can create a set.
# Functions of Sets
To create a set you can use two different ways like so:
```python
cart = {'orange', 'apple', 'carrot', 'banana', 'onion'}
```
or by using the set() with a list of values you might want to get unique values from like so:
```python
letters = set('abcadscklekdl')
```
To find the size of a set you would use the size function. To do this in python you would use len. like so:
```python
size = len(set)
```
When you use the push operation, which is .append in python, it adds the data to the stack. Like so:
```python
stack.append(value)
```
If you wanted to remove an arbitrary element from the set you have you can use:
```python
number = set.pop()
```
You can remove a value from the set by simply using the remove function in python like so:
```python
set.remove(value)
```
You can also check if a value is or is not in a list by using the in function and not in function in python which would return a true or false value like so:
```python
print(value in set)
print(value not in set)
```
There are some other functions you can use between two sets. For these I will use the following as the two sets.
```python
a = set('asdfjkl')
b = set('aelekfc')
```
You may also use different signs on two variables to do different things like "-" which would check what values are in the first variable but not second like so:
```python
print(a-b)
# outputs {'s','d','j'}
```
Theres also the "|" which would show values in both variables like so:
```python
print(a|b)
# outputs {'a','s','d','f','j','k','l','e','c'}
```
Then theres the "&" which would show what values are the same in both like so:
```python
print(a&b)
# outputs {'a','f','k','l'}
```
Lastly theres the "^" which would show values in the variables but not if they are in both like so:
```python
print(a^b)
# outputs {'s','d','j','e','c'}
```
# Time Complexity
When checking if a value is in a set it would be O(1). When adding items to a set it would be O(1). If you want to join together two sets it would be O(n). If you wish to check the difference between two sets using "-" then it would be O(n). Creating a set is O(1) since you put in data and it doesnt have to make any changes to the data itself to make it work.
# Example Code
Here is an example of how you might use a stack and the different methods you could use for this situation.
```python
# Create the set
s = set()

# Set with yellow is created but is unordered
y = set('yellow')

# Set with blue is created but is unordered
b = set('blue')

# Add an a to y set
y.add('a')

# Put two sets together outputs {'yellowbluea'}, but it will be unsorted
c = y | b

# You can also create a set with curly brackets if it is not empty
marbles = {'blue', 'orange', 'green', 'white', 'black', 'purple'}
```

# Practice Problem
Create 2 sets which will be our shopping carts. Add 3 different items to each set. Print each set out. Check what values are the same and which ones are different and print those out. Then add both sets together and print it out.

[solution to problem](https://github.com/payneful/CSE212-Final/solutions/set-solution.py)

### Other Tutorials: 
[Stack](https://github.com/payneful/CSE212-Final/blob/main/1-stack.md)
<br>
[Tree](https://github.com/payneful/CSE212-Final/blob/main/3-tree.md)