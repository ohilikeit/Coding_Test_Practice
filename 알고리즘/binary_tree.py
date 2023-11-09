'''
기본적인 트리 구현 / 순회(전위 순회, 중위 순회, 후위 순회, 레벨 순회)

용어 정리
    - 노드(Node): 트리를 구성하는 각각의 요소
    - 간선(Edge): 트리를 구성하기 위해 노드와 노드를 연결하는 선
    - 깊이(Depth): 루트 노드에서 해당 노드까지 도달하는 데 사용하는 간선의 개수, 루트 노드의 깊이는 0
    - 레벨(Level): 노드의 깊이+1
    - 노드의 분지 수, 노드의 차수(Degree): 노드의 자식 수
    - 트리의 분지 수, 트리의 차수(Degree of tree): 해당 트리 내 모든 노드의 분지 수 중 최댓값
    - 높이(Height): 루트 노드에서 해당 노드까지 도달하는데 지나간 정점의 개수, 노드 중 가장 높이가 높은 노드의 높이를 트리의 높이라고 함
    - 루트 노드(Root Node): 트리 구조에서 최상위에 있는 노드
    - 단말 노드(Terminal Node, Leaf Node): 하위에 다른 노드가 연결되어 있지 않은 노드
    - 내부 노드, 비단말 노드(Internal Node): 단말 노드를 제외한 모든 노드로 루트 노드를 포함
    - 부모 노드(Parent Node): 부모 자식 관계에서 상위 계층에 있는 노드로, 상위 계층에 있을수록 노드의 깊이와 레벨이 낮음
    - 자식 노드(Childe Node): 부모 자식 관계에서 하위 계층에 있는 노드
    - 형제 노드: 부모가 동일한 노드
    - 조상 노드: 한 노드의 부모노드부터 루트노드까지 가는 경로에 존재하는 모든 노드
    - 후손 노드: 한 노드를 루트로 하는 서브트리에 있는 모든 노드
'''
class Node(object):
    def __init__(self, item):
        self.item = item              # 루트(노드)가 갖는 값을 저장하는 변수 
        self.left = self.right = None # 루트의 자식노드들

class BinaryTree(object):
    # 빈 root만을 가지고 Node 원소로 초기화 시켜준다. 
    def __init__(self):
        self.root = None

    def preorder(self):
        '''
        전위순회
            - 루 / 왼 / 오
            - 자식 노드 확인 전에 서브 트리의 루트를 먼저 확인한 후 자식 노드를 확인하는 방법
            - 자기 자신을 먼저 출력하고 자식 노드를 호출한다. 
            - 왼쪽 노드부터 확인 
        '''
        def _preorder(node):
            print(node.item, end=' ')
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)
        
    def inorder(self):
        '''
        중위순회
            - 왼 / 루 / 오
            - 왼쪽 자식 노드, 루트 노드, 오른쪽 자식 노드 순으로 값 확인하는 방식
            - 자식 노드 확인하고 밑에 자손 노드들이 있다면 자손 노드들도 동일한 방식으로 확인 
        '''
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.item, end=' ')
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
    
    def postorder(self):
        '''
        후위순회
            - 왼 / 오 / 루
            - 자식 노드 모두 확인 후에 루트 노드 확인하는 순회 방법
            - 자식 노드의 자식 노드가 모두 존재하면 동일한 방식으로 모두 확인 
        '''
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.item, end = ' ')
        _postorder(self.root)
    
    def levelorder(self):
        '''
        레벨순회
            - 각 레벨마다 노드를 탐색하는 방법
            - 큐를 통해 구현 
        '''
        from collections import deque
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.item, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

BT = BinaryTree()
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N7 = Node(7)
N8 = Node(8)

BT.root = N1
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.left = N6
N3.right = N7
N4.left = N8

print('preorder')
BT.preorder()

print('\ninorder')
BT.inorder()

print('\npostorder')
BT.postorder()

print('\nlevelorder')
BT.levelorder()