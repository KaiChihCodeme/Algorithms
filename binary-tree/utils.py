from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def list_to_tree(o_list):
    # [3,9,20,null,null,15,7]
    q = deque([TreeNode(o_list[0])])
    index = 0
    tree_node = q[0]
    
    while len(q) > 0:
        cur_node = q.popleft()
        
        if index+2 > len(o_list)-1:
            break
        
        left_node_val = o_list[index+1]
        right_node_val = o_list[index+2]
        
        cur_node.left = TreeNode(left_node_val)
        cur_node.right = TreeNode(right_node_val)
        
        print(cur_node.val, cur_node.left.val, cur_node.right.val)
        
        q.append(cur_node.left)
        q.append(cur_node.right)
        
        index += 2
        
    return tree_node

# debug
# print(list_to_tree([3,9,20,None,None,15,7]))
        