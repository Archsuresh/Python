from stack import Stack

def ismatch(p1,p2):
    if p1=="(" and p2==")":
        return True
    if p1=="{" and p2=="}":
        return True
    if p1=="[" and p2=="]":
        return True
    else:
        return False
    
def is_paren_balanced(paren_string):
    s=Stack()
    isbalanced=True
    index=0

    while index<len(paren_string) and isbalanced:
        paren=paren_string[index]

        if paren in "{[(":
            s.push(paren)
        else:
            if s.isempty():
                isbalanced=False
            else:
                top=s.pop()
                if not ismatch(top,paren):
                    isbalanced=False

        index+= 1

    if s.isempty() and isbalanced:
        return True
    else:
        return False


print(is_paren_balanced("(){}["))
                    
