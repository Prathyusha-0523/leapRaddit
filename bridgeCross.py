class State:
    def __init__(self, left, right):
        self.left = left  
        self.right = right  
        self.time = 0
        self.umbrella_left = True  
        self.path = []

    def copy(self):
        
        new_state = State(self.left.copy(), self.right.copy())
        new_state.time = self.time
        new_state.umbrella_left = self.umbrella_left
        new_state.path = self.path.copy()
        return new_state

    def is_goal(self):
        return len(self.left) == 0 and self.time <= 60

    def get_next_states(self):
        next_states = []
        side = self.left if self.umbrella_left else self.right

        for i in range(len(side)):
            for j in range(i, len(side)):
                move = [side[i]]
                if i != j:
                    move.append(side[j])
                move_time = max(move)

                new_state = self.copy()
                new_state.time += move_time
                new_state.umbrella_left = not self.umbrella_left

                if self.umbrella_left:
                    for p in move:
                        new_state.left.remove(p)
                        new_state.right.append(p)
                else:
                    for p in move:
                        new_state.right.remove(p)
                        new_state.left.append(p)

                direction = "→" if self.umbrella_left else "←"
                new_state.path.append((direction, move.copy(), new_state.time))
                next_states.append(new_state)
        return next_states


class BridgeCrossing:
    def __init__(self):
        people = [5, 10, 20, 25]
        self.initial_state = State(people, [])

    def bfs(self):
        from collections import deque
        queue = deque([self.initial_state])
        visited = set()

        while queue:
            current = queue.popleft()
            key = (tuple(sorted(current.left)), current.umbrella_left, current.time)
            if key in visited or current.time > 60:
                continue
            visited.add(key)

            if current.is_goal():
                return current.path, current.time

            queue.extend(current.get_next_states())

        return None, -1

    def dfs(self):
        stack = [self.initial_state]
        visited = set()

        while stack:
            current = stack.pop()
            key = (tuple(sorted(current.left)), current.umbrella_left, current.time)
            if key in visited or current.time > 60:
                continue
            visited.add(key)

            if current.is_goal():
                return current.path, current.time

            stack.extend(current.get_next_states())

        return None, -1



bc = BridgeCrossing()

print("BFS Solution")
path, total_time = bc.bfs()
if path:
    print("they can catch the train")
else:
    print("No solution found within 60 minutes.")

print("DFS Solution")
path, total_time = bc.dfs()
if path:
    print("They can catch the train ")
else:
    print("No solution found within 60 minutes.")
