def brackets(input_str):
    stack_str = []
    for char in input_str:
        if char == "{" or char == "[" or char == "(" or char == "<":
            stack_str.append(char)
        elif char == "}" or char == "]" or char == ")" or char == ">":
            if len(stack_str) == 0:
                return False
            top_stack_element = stack_str.pop()
            if not compare_with_top_stack_element(top_stack_element, char):
                return False
    if len(stack_str) != 0:
        return False
    return True

def compare_with_top_stack_element(opening_char, closing_char):
    if opening_char == "{" and closing_char =="}":
        return True
    elif opening_char == "[" and closing_char =="]":
        return True
    elif opening_char == "(" and closing_char ==")":
        return True
    elif opening_char == "<" and closing_char ==">":
        return True
    return False

input_brackets = input("Enter strings, using opening and closing these brackets (),{}, [],<>  : ")
is_correct =  brackets(input_brackets)
print("brackets are in correct sequence = ", "Yes" if is_correct else "NO")

# sample input with brackets ("(12<3{456(.768)}>)"))