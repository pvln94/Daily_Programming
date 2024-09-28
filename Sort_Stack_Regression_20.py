def sort_stack(stack):
    if len(stack) == 0:
        return
    top = stack.pop()
    sort_stack(stack)
    insert_in_sorted_order(stack, top)

def insert_in_sorted_order(stack, element):
    if len(stack) == 0 or stack[-1] <= element:
        stack.append(element)
        return
    top = stack.pop()
    insert_in_sorted_order(stack, element)
    stack.append(top)

input_stack = list(map(int, input().split()))

sort_stack(input_stack)

print(input_stack)
