# **Tree**
Trees are a non-linear data structure in Python. When used properly you traverse through a tree from lowest to highest number values in the tree. Lowest values being on bottom left and highest on the bottom right. The top number is marked as a Root node and each node under has a parent node. Here is an example of the layout of a tree in python:

![Tree](https://github.com/Payneful/CSE212-Final/blob/main/pictures/pythonTree.png)
# Traversal
We traverse through trees by checking the values on the child trees. each parent can have 2 children, but they wont always if it is the end of that line of the tree. If we have a value of 10 and the root is 8 then we would look at the right child. Otherwise if the value was 4 and the root was 8 then you would look at the left child and so on. 
# Functions of Sets
## Insert
This is not a simple task since you have to find the correct location it goes by traversing the tree first like so:
```python
def insert(self, data):
	if self.root is None:
		self.root = BST.Node(data)
	else:
		self._insert(data, self.root)

def _insert(self, data, node):
	if data < node.data:
		if node.left is None:
			node.left = BST.Node(data)
		else:
			self._insert(data, node.left)
	elif data >= node.data:
		if node.right is None:
			node.right = BST.Node(data)
		else:
			self._insert(data, node.right)
```
## Traverse Forward
This does not take a lot to code, but since we do have to search through each value we have to use recursion like this:
```python
def __iter__(self):
	yield from self._traverse_forward(self.root)

def _traverse_forward(self, node):
	if node is not None:
		yield from self._traverse_forward(node.left)
		yield node.data
		yield from self._traverse_forward(node.right)
```
We use the yield to get the values from the node we have currently and we use recursion to traverse the tree.
# Time Complexity
When we use trees we take more time to do operations since we have to find the proper location for the data and where it might be. When inserting values into the tree it is in O(log n) time since you have to go through the tree but when you figure out when a value is higher or lower it excludes the upper or lower section of the tree. This decreases out time from being O(n) to O(log n). Sometimes however our tree will not be balanced and then we will have to search through every value and this would be O(n). When you wish to remove a value from the tree it would be O(log n) since we use recursive search to find the value. When looking for a value in the tree it is the same as removing in which it would be O(log n). If you want to traverse the tree forward or backward then it would be O(n) since we have to go through each of the values. finding the height would also be O(n) since we use recursive and have to go through each side to find the height. Finding the size however would be O(1) since we have this maintained in a balanced tree.
# Example Code
```python
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new data value with its parent
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
        else:
            self.data = data

    # Prints out the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(5)
root.insert(3)
root.insert(8)
root.insert(1)
root.insert(4)
root.insert(2)
root.insert(7)
root.insert(9)
root.PrintTree()
```
When the above code is executed, the result produced will be the same as the image at the top of the page. Its output should beL
```python
1,2,3,4,5,7,8,9
```
# Practice Problem
Create a tree with the values 1, 4, 5, 6, 9

[Possible Solution](https://github.com/payneful/CSE212-Final/blob/main/solution/tree-solution.py)

### Other Tutorials: 
[Stack](https://github.com/payneful/CSE212-Final/blob/main/1-stack.md)
<br>
[Set](https://github.com/payneful/CSE212-Final/blob/main/2-set.md)