## Advanced-Graphs

### This project contains python implementations of 2 advanced shortest path graph algorithms.

#### 1.Bidirectional Dijkstra
#### This algorithm was tested against the following networks:
- Dolphin social network: 62 nodes and 159 edges
- E-mail network: 1133 nodes and 5451 edges
- Internet - 22963nodes and 48436 edges
- caidaRouterLevel graph - 192244 nodes 	609066 edges
#### Reference for the datasets above: https://www.cc.gatech.edu/dimacs10/archive/clustering.shtml
#### The performance of the algorithm is 71seconds.
#### The input format:
- The first line contains two integers n and m — the number of nodes and edges in the network, respectively. 
- The nodes are numbered from 1 to n. Each of the following m lines contains three integers u, v and l describing a directed edge (u,v) of length l from the node number u to the node number v.
- The next line contains an integer q — the number of queries for computing the distance. 
- Each of the following q lines contains two integers u and v — the numbers of the two nodes to compute the distance from u to v.
#### Constraints: 
- 1≤ n ≤1000000
- 1 ≤ m ≤2000000
- 1 ≤ u,v ≤n
- 1 ≤ l ≤ 1000
- 1 ≤ q ≤ 1000
##### File : bidirec_dijkstra.py

#### 2. A* algorithm

Algorithm performance : 3.46seconds
#### Input format
- The first line contains two integers n and n — the number of nodes and edges in the network, respectively. 
- The nodes are numbered from 1 to n. Each of the following n lines contains the coordinates x and y of the corresponding node. 
- Each of the following m lines contains three integers u, v and l describing a directed edge (u, v) of length l from the node number u to the node number v.
- The next line contains an integer q — the number of queries for computing the distance. 
- Each of the following 𝑞 lines contains two integers u and v — the numbers of the two nodes to compute the distance from u to v.
#### Constraints:
- 1 ≤ n ≤ 11 000
- 1 ≤ m ≤ 30 000
- −109 ≤ x,y ≤109
- 1 ≤ u,v ≤n
- 0 ≤ l ≤ 100000
##### File A_star.py
