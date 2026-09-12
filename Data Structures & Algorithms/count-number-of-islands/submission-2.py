class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Cond: An empty grid
        # if not grid:
        #     return 0

        # Obtain the n*n matrix of the grid 
        rows, cols = len(grid), len(grid[0])
        # Tracks the visited elements (prevent backtracking)
        visited = set()
        # Tracks number of islands in the grid
        islands = 0

        # Breadth-First Search
        def bfs(row, col):
            q = collections.deque()
            visited.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                # Operations to take at current element
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                # Iterating through the operations and validating
                # if it is a path that can be taken
                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c) not in visited):
                        
                        q.append((r, c))
                        visited.add((r, c))


        # Iterate through all the elements in grid and checking
        # to evaluate when it is an island not visited (or accounted for)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands