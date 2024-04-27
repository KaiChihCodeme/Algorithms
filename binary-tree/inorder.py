import utils

def inorder(root):
    if root is None:
        return

    res = []
    
    return process(root, res)
    
    
def process(root, res):
    if root.left:
        process(root.left, res)
        
    res.append(root.val)
        
    if root.right:
        process(root.right, res)
        
    return res
        
    
root_list = [3,9,20,None,None,15,7]
root = utils.list_to_tree(root_list)
print(inorder(root))
    
