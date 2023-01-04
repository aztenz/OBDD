import node as ND
import utils as utils



class BDD:

    def __init__(self):
        self.vals = [False, False, False, False]
        self.asciis = ['a', 'b', 'c', 'd']
        self.root = ND.Node(self.asciis[0])
        self.construct(self.root, 0)

    def expExcute(self):
        #defining the expression here
        a = utils.calcLogic(self.vals[0], 0, self.vals[1])
        b = utils.calcLogic(not self.vals[0], 0, self.vals[2])
        c = utils.calcLogic(self.vals[1], 0, self.vals[3])
        d = utils.calcLogic(self.vals[1], 0, self.vals[2])
        aOrb = utils.calcLogic(a, 1, b)
        cOrd = utils.calcLogic(c, 1, d)
        return utils.calcLogic(aOrb, 1, cOrd)

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