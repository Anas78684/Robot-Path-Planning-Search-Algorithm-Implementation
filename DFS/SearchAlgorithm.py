# Implementation of AIP Assignment in BFS State
from collections import deque
import nodeBuilding as nb
import openpyxl


excel_file_path = './map16x22.xlsx'

class BasicNode:
    def __init__(self, rowNumber, cellNumber, value):
        self.rowNumber = rowNumber
        self.cellNumber = cellNumber
        self.value = value
        self.next_nodes = []
        self.next_locations = []

class Node:
    visited = []
    nodeHolder = {}
    keyHolder = []
    
    recursiveCounter = 0
    def nodePlanner(row, cell, value):
        key = f"{row}:{cell}"
        nodeValue = BasicNode(row, cell, value)
        nodeValue.next_locations = [f'{row-1}:{cell}',f'{row+1}:{cell}',f'{row}:{cell-1}',f'{row}:{cell+1}']
        
        Node.nodeHolder[key] = nodeValue
        
        return nodeValue

    def nodeChecking(rowNumber, cellNumber):
        checker = f"{rowNumber}:{cellNumber}"
        if checker in Node.keyHolder:
            retrieve = Node.nodeHolder[checker]
            return retrieve
        return None

    def nodeAppending():
        for key, value in Node.nodeHolder.items():
            for locations in Node.nodeHolder[key].next_locations:
                if locations in Node.nodeHolder:
                    Node.nodeHolder[key].next_nodes.append(Node.nodeHolder[locations])
                

    def nodeCreation(file_path):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        startNode = None; goalNode = None
        for index, row in enumerate(sheet.iter_rows(min_row=1, values_only=True), start = 1):
            for col_num, value in enumerate(row, start=1):
                #if value != 0:
                node = Node.nodePlanner(index, col_num, value)
                #print(len(Node.nodeHolder))
                if value == 'start':
                    startNode = node
                if value == 'goal':
                    goalNode = node
              
        return startNode, goalNode       

   
    
    def traversal(traverse, nodeToFind, visited = [], non_visited = [], path = []):
        returnFlag = False; foundPath = []
        if traverse in Node.visited:
            #print(f"Here is the printing of the {traverse.value} that seem to be already in the visited section")
            return non_visited, returnFlag, foundPath
        #print(f"This Node: {traverse.value}")
        Node.visited.extend([traverse])
        
        i = 0; j = 0; flag = 0
        if traverse.next_nodes:
            while i < len(traverse.next_nodes):
                if traverse.next_nodes[i].value == 0:
                    
                    i = i + 1
                    continue
                while j < len(visited):
                    if visited[j] == traverse.next_nodes[i]:
                        flag = 1
                        break
                    j = j + 1
                if flag == 0:
                    print(f"Appending {traverse.next_nodes[i].value} in the non visited.")
                    non_visited.append((traverse.next_nodes[i], path + [traverse]))
                    
                    #non_visited.extend([traverse.next_nodes[i]])
                    localPath = path + [traverse]
                    #print(f"Unknowable Path: {path}")
                    plotList = []
                    for paths in localPath:
                        gets = (paths.rowNumber - 1, paths.cellNumber - 1)
                        print(f"Coords is {gets}")
                        plotList.append(gets)
                    data = nb.read_excel(excel_file_path)
                    #print(f"Plotting is {plotList}")
                    nb.plot_grid(data, plotList)
                #print(f"Node to find is {nodeToFind.value} and Current Value is {traverse.value} and its nodes are {len(traverse.next_nodes)}")
                if traverse.value == nodeToFind.value:
                    returnFlag = True
                    foundPath = path + [traverse]
                i = i + 1; j = 0; flag = False
            return non_visited, returnFlag, foundPath
        else:
            if traverse.value == nodeToFind.value:
                returnFlag = True
                foundPath = path + [traverse]
            return non_visited, returnFlag, foundPath
    
    def makeTraversal(traverse, nodeToFind):
        #print(f"Starting Traverse is: {nodeToFind.value}")
        non_visited = deque([(traverse, [])])
        traverse, path = non_visited.pop()
        non_visited, returnFlag, foundPath = Node.traversal(traverse, nodeToFind, Node.visited, non_visited, path)

        while len(non_visited)>0:
            traverse, path = non_visited.pop()
            non_visited, returnFlag, foundPath = Node.traversal(traverse, nodeToFind,Node.visited, non_visited, path)
            #for paths in path:  
                #print(f"Path is {traverse.value} and Value is {paths.value}")
            
            if returnFlag == True:
                print(f"The path to {nodeToFind.value} is: ")
                finalPlotPath = []
                for found in foundPath:
                    plotPoints = (found.rowNumber - 1, found.cellNumber - 1)
                    finalPlotPath.append(plotPoints)
                    print(f"->{found.rowNumber}:{found.cellNumber}")
                data = nb.read_excel(excel_file_path)
                print(f"Plotter => {finalPlotPath}")
                nb.final_plot_grid(data, finalPlotPath)
                return
            print(f"Here printing the length of the non visited {len(non_visited)}")

            

        

index = 1
checkThese = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    
start, goal =  Node.nodeCreation(excel_file_path)
Node.nodeAppending()
# for check in checkThese:
#     retrievedNode = Node.nodeChecking(check, index)
#     if retrievedNode:
#         print(f"Row is {retrievedNode.rowNumber} Cell is {retrievedNode.cellNumber} Data Val is {retrievedNode.value}")
#         for next in retrievedNode.next_nodes:
#             print(f"and its attached nodes Row is {next.rowNumber} and Cell Number is {next.cellNumber} and the Value is {next.value}")
        
#print(f"The Start Node Is {start.rowNumber} : {start.cellNumber} and value is {start.value} and its appended nodes are {start.next_locations}")
#print(f"The Goal Node Is {goal.rowNumber} : {goal.cellNumber} and value is {goal.value} and its appended nodes are {goal.next_locations}")
#print(Node.nodeHolder)
Node.makeTraversal(traverse=start, nodeToFind=goal)
#Node.simpleTraversal(start)