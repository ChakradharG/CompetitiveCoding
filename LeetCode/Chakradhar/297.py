# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        order = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is not None:
                order.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                order.append(None)
        
        while len(order) > 1 and order[-1] is None:
            order.pop()
        print(order)
        
        return ','.join(map(str, order))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        order = deque([])
        for val in data.split(','):
            if val == 'None':
                order.append(None)
            else:
                order.append(int(val))
        print(order)

        root = order.popleft()
        if root is None:
            return None
        else:
            root = TreeNode(root)
        q = deque([root])
        while q:
            node = q.popleft()
            if not order:
                break
            left = order.popleft()
            if left is not None:
                node.left = TreeNode(left)
                q.append(node.left)
            if not order:
                break
            right = order.popleft()
            if right is not None:
                node.right = TreeNode(right)
                q.append(node.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))