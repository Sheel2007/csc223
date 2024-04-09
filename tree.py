from binarytree import Node, tree

# --------------- pg. 282 ---------------

# Define the nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

# Build the tree structure
A.left = B
A.right = C
C.left = D
D.right = E

# Print the tree
print(A)

A = Node("F")
B = Node("G")
C = Node("H")
D = Node("I")
E = Node("J")

# Build the tree structure
A.left = B
A.right = C
C.left = D
D.right = E

print(A)

# --------------- pg. 284 ---------------
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
eleven = Node(11)
twelve = Node(12)

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
four.left = eight
four.right = nine
six.left = ten
six.right = eleven
seven.right = twelve


print(one)


# Define the nodes
amar = Node("Amar")
janak = Node("Janak")
raj = Node("Raj")
pallav = Node("Pallav")
rudraksh = Node("Rudraksh")
deepak = Node("Deepak")
ridhiman = Node("Ridhiman")
tanush = Node("Tanush")
sanjay = Node("Sanjay")
kuvam = Node("Kuvam")
kunsh = Node("Kunsh")

# Build the tree structure
amar.left = janak
amar.right = raj
janak.left = pallav
pallav.left = rudraksh
pallav.right = deepak
raj.left = ridhiman
raj.right = tanush
ridhiman.left = sanjay
tanush.left = kuvam
tanush.right = kunsh

# Print the tree with color
print(amar)
