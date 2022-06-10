class Node:
    def __init__(self, row, col, value):
        self.id = "{} {}".format(row, col)
        self.row = row
        self.col = col
        self.value = value
        self.distanceFromStart = float("inf")
        self.estimatedDistanceToEnd = float("inf")
        self.cameFrom = None
        
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)
    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhatanDistance(startNode, endNode)

    nodesToVisit = MinHeap([ startNode ])
    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.remove()
        if currentMinDistanceNode == endNode:
            break
            
        neighbors = getNeighborNodes(currentMinDistanceNode, nodes)
        for neighbor in neighbors:
            if neighbor.value == 1:
                continue
            tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart + 1
            if tentativeDistanceToNeighbor >= neighbor.distanceFromStart:
                continue
            neighbor.cameFrom = currentMinDistanceNode
            neighbor.distanceFromStart = tentativeDistanceToNeighbor
            neighbor.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhatanDistance(neighbor, endNode)

            if not nodesToVisit.containsNode(neighbor):
                nodesToVisit.insert(neighbor)
            else:
                nodesToVisit.update(neighbor)
    return reconstructPath(endNode)
    
def initializeNodes(graph):
    nodes = []
    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))
    return nodes

def calculateManhatanDistance(currentNode, endNode):
    return abs(currentNode.row - endNode.row) + abs(currentNode.col - endNode.col)

def getNeighborNodes(node, nodes):
    neighbors = []

    numRows = len(nodes)
    numCols = len(nodes[0])
    row = node.row
    col = node.col
    # down, up, left, right
    if row < numRows - 1: neighbors.append(nodes[row + 1][col])
    if row > 0: neighbors.append(nodes[row - 1][col])
    if col > 0: neighbors.append(nodes[row][col - 1])
    if col < numCols - 1: neighbors.append(nodes[row][col + 1])
    return neighbors
    
def reconstructPath(endNode):
    if not endNode.cameFrom: return []
    currentNode = endNode
    path = []
    while currentNode is not None:
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.cameFrom
    return path[::-1]
class MinHeap:
    def __init__(self, array):
        self.nodesPositionInHeap = {node.id: idx for idx, node in enumerate(array)}
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIndex = (len(array) - 2) // 2
        for currentIndex in reversed(range(firstParentIndex + 1)):
            self.siftDown(currentIndex, len(array) - 1, array)
        return array
        
    def siftDown(self, currentIndex, endIndex, heap):
        childOneIndex = currentIndex * 2 + 1
        while childOneIndex <= endIndex:
            childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
            if (
                childTwoIndex != -1
                and heap[childTwoIndex].estimatedDistanceToEnd < heap[childOneIndex].estimatedDistanceToEnd
            ):
                indexToSwap = childTwoIndex
            else:
                indexToSwap = childOneIndex
            if heap[indexToSwap].estimatedDistanceToEnd < heap[currentIndex].estimatedDistanceToEnd:
                self.swap(currentIndex, indexToSwap, heap)
                currentIndex = indexToSwap
                childOneIndex = currentIndex * 2 + 1
            else:
                return
                
    def siftUp(self, currentIndex, heap):
        parentIndex = (currentIndex - 1) // 2
        while currentIndex > 0 and heap[currentIndex].estimatedDistanceToEnd < heap[parentIndex].estimatedDistanceToEnd:
            self.swap(currentIndex, parentIndex, heap)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2
            
    def isEmpty(self):
        return len(self.heap) == 0

    def remove(self):
        if self.isEmpty(): return
            
        self.swap(0, len(self.heap) - 1, self.heap)
        removedNode = self.heap.pop()
        del self.nodesPositionInHeap[removedNode.id]
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return removedNode

    def insert(self, node):
        self.heap.append(node)
        self.nodesPositionInHeap[node.id] = len(self.heap) - 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        self.nodesPositionInHeap[heap[i].id] = j
        self.nodesPositionInHeap[heap[j].id] = i
        heap[i], heap[j] = heap[j], heap[i]

    def containsNode(self, node):
        return node.id in self.nodesPositionInHeap

    def update(self, node):
        self.siftUp(self.nodesPositionInHeap[node.id], self.heap)
