def isbalanced(root):

    def check(root):
        print(root)   
        if 2 * root < len(tree1):
            left = check(2 * root)
        else:
            left = 0

        if 2 * root + 1 < len(tree1):
            right = check(2 * root + 1)
        else:
            right = 0
        
        if left == -1 or right == -1 or not left or not right:
            return -1
        
        return max(left, right) + 1

    return check(root) != -1


tree = [0, 3, 9, 20, None, None, 15, 7]
tree1 = [0, 1, 2, 2, 3, 3, None, None, 4, 4]
print(isbalanced(1))