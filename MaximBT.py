 class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        while(len(nums) != 1):
            root = max(nums)
            ind = nums.index(root)
            r = TreeNode(root)
            r.right = constructMaximumBinaryTree(nums[ind:])
            r.left = constructMaximumBinaryTree(nums[:ind])
        
        return r