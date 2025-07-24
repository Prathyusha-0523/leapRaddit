from collections import deque

class RabbitLeapGame:
    def __init__(self):
        self.start = ['G', 'G', 'G', '-', 'B', 'B', 'B']
        self.goal = ['B', 'B', 'B', '-', 'G', 'G', 'G']

    def get_next_states(self, state):
        next_states = []
        for i in range(len(state)):
            val = state[i]
            if val == '-':
                continue
            if val == 'G':
                
                if i + 1 < len(state) and state[i + 1] == '-':
                    new_state = state[:]
                    new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                    next_states.append(new_state)
                elif i + 2 < len(state) and state[i + 1] == 'B' and state[i + 2] == '-':
                    new_state = state[:]
                    new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                    next_states.append(new_state)
            elif val == 'B':
                
                if i - 1 >= 0 and state[i - 1] == '-':
                    new_state = state[:]
                    new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                    next_states.append(new_state)
                elif i - 2 >= 0 and state[i - 1] == 'G' and state[i - 2] == '-':
                    new_state = state[:]
                    new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                    next_states.append(new_state)
        return next_states

    def bfs(self):
        visited = set()
        queue = deque()
        queue.append((self.start, [self.start]))

        while queue:
            current, path = queue.popleft()
            state_key = tuple(current)

            if state_key in visited:
                continue
            visited.add(state_key)

            if current == self.goal:
                return path

            next_states = self.get_next_states(current)
            for ns in next_states:
                queue.append((ns, path + [ns]))

        return None

    def dfs(self):
        visited = set()
        stack = []
        stack.append((self.start, [self.start]))

        while stack:
            current, path = stack.pop()
            state_key = tuple(current)

            if state_key in visited:
                continue
            visited.add(state_key)

            if current == self.goal:
                return path

            next_states = self.get_next_states(current)
            for ns in next_states:
                stack.append((ns, path + [ns]))

        return None

    def print_solution(self, solution, method_name):
        if solution:
            print("Goal found")
        else:
            print("Goal not found")


game = RabbitLeapGame()
bfs_result = game.bfs()
game.print_solution(bfs_result, "BFS")

dfs_result = game.dfs()
game.print_solution(dfs_result, "DFS")
