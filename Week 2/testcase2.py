

# start = 1
# goals = [7]
# DFS_path = [1, 2, 5, 7]
# A_Star_path = [1, 3, 4, 5, 7]

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
	[0, 0, 4, 3, -1, -1, -1, -1],
	[0, 4, 0, -1, -1, 12, 5, -1],
	[0, 3, -1, 0, 7, 10, -1, -1],
	[0, -1, -1, 7, 0, 2, -1, -1],
	[0, -1, 12, 10, 2, 0, -1, 5],
	[0, -1, 5, -1, -1, -1, 0, 16],
	[0, -1, -1, -1, -1, 5, 16, 0]]
    heuristic = [0, 14, 12, 11, 6, 4, 11, 0]
    start = 1
    goals = [7]
    try:
        if mymodule.A_star_Traversal(cost, heuristic, start, goals)==[1, 3, 4, 5, 7]:
            print("Test Case 1 for A* Traversal PASSED")
        else:
            print("Test Case 1 for A* Traversal FAILED")
    except Exception as e:
        print("Test Case 1 for A* Traversal FAILED due to ",e)


    try:
        if mymodule.DFS_Traversal(cost,start, goals)==[1, 2, 5, 7]:
            print("Test Case 2 for DFS Traversal PASSED")
        else:
            print("Test Case 2 for DFS Traversal FAILED")
    except Exception as e:
        print("Test Case 2 for DFS Traversal FAILED due to ",e)         

testcase(mymodule)