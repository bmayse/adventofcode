class Node:
    def __init__(self, starting_value, left, right):
        self.value = starting_value
        self.left = left
        self.right = right

    def apply_then_find_next_node(self, steps, value_operation):
        self.value = value_operation(self.value)
        cur = self
        while steps != 0:
            if steps > 0:
                if cur.right is None:
                    return None
                cur = cur.right
                steps -= 1
            else:
                if cur.left is None:
                    return None
                cur = cur.left
                steps += 1
        return cur
