

def validParant(self,ST):

    stack=[]
    for c in ST:
        if c =="{[(":
            stack.append(c)
        elif c in ')]}':
             if not stack:
                 return False
        top = stack.pop()
        if c=='}' and top!='{':
            return False
        elif c== "]" and top!='[':
            return False
        elif c==")" and top!= '(':
            return False
    return not stack
