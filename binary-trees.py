class Node:
    def __init__(self,data):
        self.data = data
        self.left_node = None
        self.right_node = None
        
    def __repr__(self):
        return f"Data:{self.data}->Left Node:{self.left_node}->Right Node:{self.right_node}"

n1 = Node(20)
print(n1)