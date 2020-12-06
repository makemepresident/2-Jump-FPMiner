class TreeNode:

    def __init__(self, children=None, count=0):
        if children == None:    
            self.children = dict()
        else:
            self.children = children
        self.count = count

    def getChildren(self):
        return self.children

    def getCount(self):
        return self.count

    def increment(self):
        self.count += 1

    def add(self, child_key):
        if(child_key in self.children.keys()):
            self.children[child_key].increment()
        else:
            self.children[child_key] = TreeNode(count=1)

        return self.children[child_key]


class DnaSequenceMiner:
    def __init__(self, data_string=''):
        self.data_string = data_string

    def setDataSet(self, dataset):
        self.data_string = dataset

    def buildSequenceList(self, node, sublist, substring, depth, min_sup):
        if node.getCount() < min_sup:
            return
        elif depth < 1:
            sublist.append((substring, node.getCount()))
            return        
        else:
            for key in node.getChildren().keys():
                self.buildSequenceList(node.getChildren()[key], sublist, substring+key, depth-1, min_sup)

    def getSequencesOfN(self, length=1, string=None, min_sup=0):
        if(string == None):
            string = self.data_string
        if length < 1 or len(string) < length:
            return []

        root = TreeNode(count=min_sup)

        for i in range(0, 1+len(string)-length):
            current_node = root

            for j in range(i, i+length):
                current_node = current_node.add(string[j])

        result = []

        self.buildSequenceList(root, result, '', length, min_sup)

        return result
        