class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        left = None if self.left is None else self.left.val
        right = None if self.right is None else self.right.val
        return '(D:{}, L:{}, R:{})'.format(self.val, left, right)

def rangeSumBST(root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        sum = 0 
        
        if root: 
    
            # First recur on left child 
            sum += printInorder(root.left) 
    
            # then print the data of node
            if L <= root.val <= R: 
                sum += root.val
    
            # now recur on right child 
            sum += printInorder(root.right)

        return sum  
  


root = TreeNode(24)

a = TreeNode(15)

root.left = a

b = TreeNode(33)

root.right = b 

c = TreeNode(30)

b.left = c

d = TreeNode(21)

a.right = d

e = TreeNode(12)

a.left = e

print(rangeSumBST(root, 3, 6))