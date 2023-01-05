import node as ND
import utils as UTL


class BDD:

    def __init__(self):
        parsedData = UTL.parseExp()
        self.asciis: list[str] = parsedData[0]
        self.orders: list[str] = parsedData[1]
        self.vals = [False for _ in range(len(self.asciis))]
        self.root = ND.Node(self.asciis[0])
        self.construct(self.root, 0)

    def calcLogic(self, exp1: bool, and0Or1: int, exp2: bool) -> bool:
        if and0Or1 == 0:
            return exp1 and exp2
        elif and0Or1 == 1:
            return exp1 or exp2

    def expExcute(self):
        res = False
        for ord in self.orders:
            x = [*ord]
            notFlag = False
            curr = True
            for i in range(len(x)):
                if x[i] == '!':
                    notFlag = True
                    continue
                if notFlag:
                    curr = self.calcLogic(
                        curr, 0, not self.vals[self.asciis.index(x[i])])
                    notFlag = False
                else:
                    curr = self.calcLogic(
                        curr, 0, self.vals[self.asciis.index(x[i])])
            res = self.calcLogic(res, 1, curr)
        return res

    def setVar(self, position, value):
        self.vals[position] = value
        return

    def construct(self, curr: ND.Node, pos):
        if ((curr.asci == '0') or (curr.asci == '1')):
            return

        for i in range(pos, len(self.vals)):
            self.setVar(i, False)
        val0 = self.expExcute()
        for i in range(pos, len(self.vals)):
            self.setVar(i, True)
        val1 = self.expExcute()
        if val0 != val1:
            if curr.asci == self.asciis[-1]:
                if val0:
                    curr.appendChild('1', 0)
                else:
                    curr.appendChild('0', 0)
                if val1:
                    curr.appendChild('1', 1)
                else:
                    curr.appendChild('0', 1)
                return
            curr.appendChild(self.asciis[pos+1], 0)
            curr.appendChild(self.asciis[pos+1], 1)
            self.setVar(pos, False)
            self.construct(curr.left, pos+1)
            self.setVar(pos, True)
            self.construct(curr.right, pos+1)
        elif val0 == val1:
            if val0:
                curr.asci = '1'
            else:
                curr.asci = '0'
            return
        return 0

    def printGraph(self, myRoot: ND.Node):
        if ((myRoot.asci == '0') or (myRoot.asci == '1')):
            print("Node: ", myRoot.asci, "\n")
            return
        print("Node: ", myRoot.asci, "\n")
        self.printGraph(myRoot.left)
        self.printGraph(myRoot.right)
