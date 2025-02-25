# TC: O(N)
# SC:O(D) where D is the diameter of the tree at any given level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=collections.deque()
        
        q.append(root)
        
        res=[]
        while q:
            qLen=len(q)
            rightNode=None
            
            for i in range(qLen):
                node=q.popleft()
                if node:
                    rightNode=node
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightNode:
                res.append(rightNode.val)
        return res