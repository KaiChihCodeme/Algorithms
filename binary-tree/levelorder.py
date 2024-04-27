import utils
from collections import deque

def levelorder(root):
    if root is None:
        return

    res = []
    q = deque([root])
    tmp = []
    tmp_q = deque()
    
    while len(q) > 0:
        cur_node = q.popleft()
        tmp.append(cur_node.val)
        
        if cur_node.left:
            tmp_q.append(cur_node.left)
            
        if cur_node.right:
            tmp_q.append(cur_node.right)
            
        if len(q) == 0:
            res.append(tmp)
            tmp = []
            q = tmp_q
            tmp_q = deque()
            
    return res

    # or
    # res = []
    # q = deque([root])
    
    # while q:
    #     tmp = []
    #     for _ in range(len(q)):
    #         cur_node = q.popleft()
    #         tmp.append(cur_node.val)
            
    #         if cur_node.left:
    #             q.append(cur_node.left)
                
    #         if cur_node.right:
    #             q.append(cur_node.right)
                
    #     res.append(tmp)
        
    # return res
    
root_list = [3,9,20,None,None,15,7]
root = utils.list_to_tree(root_list)
print(levelorder(root))
    
