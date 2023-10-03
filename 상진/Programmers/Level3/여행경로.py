import copy

def solution(tickets):
    global answer
    stack = ["ICN"]
    tickets.sort()
    size = len(tickets)
    visited = [0] * size

    def back(start):
        global answer
        if len(stack) == size + 1:
            if not answer:
                answer = copy.deepcopy(stack)
                return

        for i in range(size):
            start, next = tickets[i]
            if start == stack[-1] and not visited[i]:
                stack.append(next)
                visited[i] = 1
                back(next)
                visited[i] = 0
                stack.pop()

    answer = []
    back("ICN")
    return answer