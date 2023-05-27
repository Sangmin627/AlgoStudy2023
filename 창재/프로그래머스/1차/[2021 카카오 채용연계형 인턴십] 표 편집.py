class Node:
    def __init__(self, idx, next=None, prev=None):
        self.idx = idx
        self.prev = prev
        self.next = next


# 링크드 리스트 추가
def add(head, idx):
    node = head
    while node.next:
        if node.next.idx > idx:
            break
        node = node.next

    new_node = Node(idx)

    if node.next:
        node.next.prev = new_node
        new_node.next = node.next

    node.next = new_node
    new_node.prev = node



# 링크드 리스트 삭제
def delete(head, idx):
    node = head
    while node.idx != idx:
        node = node.next

    node.prev.next = node.next
    node.next.prev = node.prev


# 링크드 리스트 초기화
def init_Node(n):
    node = Node(0)
    head = node
    for i in range(1, n):
        add(head, i)

    return head


def solution(n, k, cmd):
    node = init_Node(n - 2)  # 초기화

    # 모든 노드 출력
    while node.next:
        print(node.idx)
        node = node.next
    print(node.idx)

    answer = ''

    memo = ['O'] * (n - 2)
    print("memo : ", memo)

    current = k
    remove_stack = []

    for c in cmd:
        list_c = list(c)
        print(list_c)
        if list_c[0] == "D":
            current = D(list_c[2], current)

    print(current)
    return answer


def U(node, X, current):
    return current - int(X)


def D(node, X, current):
    return current + int(X)


def C(node, remove_stack, current):
    remove_stack.append(current)

    return current + 1


cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
solution(8, 2, cmd)
