DFS_path = [1, 2, 3, 4, 7]
A_star_path = [1, 5, 3, 6, 7]

import sys
import importlib
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--SRN', required=True)

args = parser.parse_args()
subname = args.SRN


try:
   mymodule = importlib.import_module(subname)
except:
    print("Rename your written program as YOUR_SRN.py and run python3.7 SampleTest.py --SRN YOUR_SRN ")
    sys.exit()



def testcase(mymodule):
    cost = [[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 3, -1, -1, 2, 0, -1], 
	[0, -1, 0, 5, 10, -1, -1, -1], 
	[0, -1, -1, 0, 2, -1, 1, -1], 
	[0, -1, -1, -1, 0, -1, -1, 4], 
	[0, -1, -1, 1, -1, 0, 4, -1], 
	[0, -1, -1, -1, -1, -1, 0, 3], 
	[0, -1, -1, -1, -1, -1, -1, 0]]
    heuristic = [0, 7, 9, 4, 2, 5, 3, 0]
    start = 1
    goals = [7]
    try:
        if mymodule.A_star_Traversal(cost, heuristic, start, goals)==A_star_path:
            print("Test Case 1 for A* Traversal PASSED")
        else:
            print("Test Case 1 for A* Traversal FAILED")
    except Exception as e:
        print("Test Case 1 for A* Traversal FAILED due to ",e)


    try:
        if mymodule.DFS_Traversal(cost,start, goals)==DFS_path:
            print("Test Case 2 for DFS Traversal PASSED")
        else:
            print("Test Case 2 for DFS Traversal FAILED")
    except Exception as e:
        print("Test Case 2 for DFS Traversal FAILED due to ",e)         

testcase(mymodule)