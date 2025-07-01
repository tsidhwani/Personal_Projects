class FlowNode:
    def __init__(self, text, leftNode=None, rightNode=None):
        self.text = text # question or final answer
        self.leftNode = leftNode #if yes
        self.rightNode = rightNode # if no

    def is_leaf(self): #node is leaf if it has no children
        return self.leftNode is None and self.rightNode is None

class FlowTree:
    def __init__(self):
        self.root = None
    
    def add_root(self, rootNode):
        self.root = rootNode

    def traverse(self):
        curr = self.root
        while curr:
            if curr.is_leaf():
                print(curr.text)
                break
            else:
                print(curr.text)
                userInput = input("Enter yes or no: ").strip().lower()
                if userInput == "yes":
                    curr = curr.leftNode   #follows yes path
                elif userInput == "no":
                    curr = curr.rightNode
                else:
                    print("Please enter either yes or no.")
        

    
