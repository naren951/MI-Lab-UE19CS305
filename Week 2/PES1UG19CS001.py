"""
You can create any other helper funtions.
Do not modify the given functions
"""
import heapq

def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    # TODO
    # path=[]
    # li=[]
    # visited=[False]*(len(cost)+1)
    # fscore=[-1] *(len(cost))
    
    # heapq.heappush(li,[heuristic[start_point],start_point,[start_point],0]) 
    
    # while(len(li)!=0):
    # 	n=heapq.heappop(li)
    # 	print(n,"hello")
    # 	node = n[1]
    	
    # 	A_star_path_till_node = n[2]
    	
    # 	node_cost = n[3]

    # 	if visited[node]==False:
    # 		visited[node]=True

    # 	for i in range(1,len(cost)):
    		
    # 		if (cost[node][i]>0) and  (visited[i]==0)  :
    # 			total_cost_till_node = node_cost + cost[node][i]
    # 			estimated_total_cost = total_cost_till_node +heuristic[i]
    			
    # 			if fscore[i] ==-1 :
    # 				fscore[i]=estimated_total_cost
    # 				a=A_star_path_till_node
    # 				a.append(i)
    # 				print(fscore)
    				
    # 				print(a,"hello1\n")
    				
    # 				heapq.heappush(li,[estimated_total_cost ,i,a,total_cost_till_node])
    # 			elif estimated_total_cost < fscore[i]:
    # 				fscore[i]=estimated_total_cost
    # 				a=A_star_path_till_node
    # 				print(fscore)
    # 				for j in ((li)):
    # 					if j[1] == i:
    # 						j[0] = estimated_total_cost
    # return path
    visited = []
    path = [start_point]
    queue = [[0+heuristic[start_point], path]]
    while len(queue) > 0: 
        temp = queue.pop(0)
        curr_cost = temp[0]
        curr_path = temp[1]
        node = curr_path[len(curr_path)-1]
        curr_cost = curr_cost - heuristic[node]
        if node in goals:
            return curr_path
        visited.append(node)
        children=[]
        for i in range(len(cost)):
            if cost[node][i] not in [0, -1]:
                children.append(i)
        for i in children:
            new_curr_path = curr_path + [i]
            new_path_cost = curr_cost + cost[node][i] + heuristic[i]
            if i not in visited and new_curr_path not in [i[1] for i in queue]:
                queue.append((new_path_cost, new_curr_path))
                queue = sorted(queue, key=lambda x: (x[0], x[1]))
            elif new_curr_path in [i[1] for i in queue]:
                for index in range(len(queue)):
                    if queue[index][1] == path:
                       i=index
                       break
                queue[i][0] = min(queue[i][0], new_path_cost)
                queue = sorted(queue, key=lambda x: (x[0], x[1]))
    return list()
global path

def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    # TODO
    path=[]
    visited=[]
    start = start_point
    DFS(visited,path,cost,goals,start)
    return path


def DFS(visited,path,cost,goals,start):
    if start not in visited:
        visited.append(start)
        path.append(start)
        if start in goals:
            return -1
        else:
            for i in range(1,len(cost[start])):
                if(cost[start][i]!=-1 and cost[start]!=0):
                    check=DFS(visited,path,cost,goals,i)
                    if(check==-1):
                        return -1
            path.pop()
