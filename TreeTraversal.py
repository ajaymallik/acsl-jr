
class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val


"""
inorder tree traversal
"""
def inorder(root):

	if root:
		# Recurse left 
		inorder(root.left)

		# Print the value of the node
		print(root.val, end=" "),

        #Recurse Right
		inorder(root.right)



if __name__ == "__main__":
	root = Node(4)
	root.left = Node(2)
	root.right = Node(5)
	root.left.left = Node(1)
	root.left.right = Node(3)

	# Function call
	print("Inorder traversal: ")
	inorder(root)
