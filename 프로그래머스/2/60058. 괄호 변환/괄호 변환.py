def is_valid(s):
    """Check if the string is a valid parenthesis string."""
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    return not stack


def split_uv(s):
    """Split the string into balanced strings u and v."""
    left_count, right_count = 0, 0
    for i, char in enumerate(s):
        if char == '(':
            left_count += 1
        else:
            right_count += 1
        
        if left_count == right_count:
            return s[:i+1], s[i+1:]


def reverse_parenthesis(s):
    """Reverse the parenthesis of the given string."""
    return ''.join([')' if char == '(' else '(' for char in s])


def solution(p):
    # Base case
    if not p:
        return ""
    
    u, v = split_uv(p)
    
    if is_valid(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse_parenthesis(u[1:-1])


# Test the solution
test_string = "(()))("
solution(test_string)
