

class Node:
    def __init__(
        self, asci,
        parent=None,
        desision=-1,
        left=None,
        right=None
    ):

        self.left = left
        self.right = right
        self.asci = asci
        self.parent = parent
        self.desision = desision

    def appendChild(
        self,
        desision: int,
        childascii: str
    ):
        if desision == 0:
            self.left = Node(childascii, self, 0)
        elif desision == 1:
            self.right = Node(childascii, self, 1)
        return


class BDD:

    def __init__(self):
        self.root = Node(self.getVars()[0])
        self.construct(self.root, 0)
        self.vals = [0, 0, 0, 0]
        self.asciis = ['a', 'b', 'c', 'd']

    def expExcute(self):
        # excute the returned expression
        # an array of values is passed then excuted
        return True

    def setVar(self, position, value):
        self.vals[position] = value
        return

    def construct(self, curr: Node, pos):
        if (curr.asci == '0' | curr.asci == '1'):
            return
        self.setVar(pos, 0)
        val0 = self.expExcute()
        self.setVar(pos, 1)
        val1 = self.expExcute()
        if val0 != val1:
            curr.appendChild(self.asciis[pos+1], 0)
            curr.appendChild(self.asciis[pos+1], 1)
            self.setVar(pos, 0)
            self.construct(curr.left, pos+1)
            self.setVar(pos, 1)
            self.construct(curr.right, pos+1)
        elif val0 == val1:
            if val0:
                curr.asci = '1'
            else:
                curr.asci = '0'
            return
        return 0
