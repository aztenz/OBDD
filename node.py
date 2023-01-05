class Node:
    def __init__(
        self, asci,
        parent=None,
        decision=-1,
        left=None,
        right=None
    ):

        self.left = left
        self.right = right
        self.asci = asci
        self.parent = parent
        self.decision = decision

    def appendChild(
        self,
        childascii: str,
        decision: int
    ):
        if decision == 0:
            self.left = Node(childascii, self, 0)
        elif decision == 1:
            self.right = Node(childascii, self, 1)
        return
