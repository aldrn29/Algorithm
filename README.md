## 그래프
정점과 간선으로 이루어진 자료구조
              
#### 그래프의 탐색
첫 정점에서부터 그래프에 존재하는 모든 정점들을 모두 한번씩 방문하는 것
- 그래프의 탐색 방법: 너비 우선 탐색(BFS), 깊이 우선 탐색(DFS) 

## BFS, DFS
- 너비 우선 탐색(BFS: Breadth First Search)  
너비를 우선으로 하여 최단 경로 탐색을 수행, 큐(Queue) 사용
- 깊이 우선 탐색(DFS: Depth First Search)    
깊이를 우선으로 하여 최단 경로 탐색을 수행, 스택(Stack) 혹은 재귀함수 사용

<br><br>  

## 알고리즘

#### 그리디(Greedy)
정렬, 탐색 등과 같이 정해진 구현 방식이 있는 알고리즘이 아닌 현재 상황에서 최적의 방향을 구하는 가장 단순한 형태의 알고리즘  

#### 브루트 포스(Brute Force)   
가능한 모든 경우에 대해 모든 방법을 찾아보는 완전탐색알고리즘
- 선형구조: 순차탐색
- 비선형구조: BFS, DFS   

#### 백트래킹(Backtracking)
DFS의 과정에서 반복되거나 불필요한 과정을 제외하면서 모든 경우의 수를 찾아 진행하는 일종의 트리 탐색 알고리즘 

#### 다익스트라(Dijkstra)
하나의 정점에서 다른 모든 정점으로 가는 짧은 경로를 찾아 진행하는 다이나믹 프로그래밍을 활용한 대표적인 최단 경로 탐색 알고리즘

#### 동적 계획법
한 가지 문제에 대해서, 단 한 번만 풀도록 만들어주는 알고리즘
Optimal Substructure에서 효과를 발휘 : 답을 구하기 위해 이미 했던 똑같은 계산을 계속 반복하는 문제 구조
