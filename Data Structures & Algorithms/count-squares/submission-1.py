class CountSquares:

    def __init__(self):
        self.points = []
        self.points_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points.append((x,y))
        self.points_map[(x,y)] += 1        

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point
        for x,y in self.points:
            if abs(px - x) != abs(py - y) or (x == px and y == py):
                continue
            diag = self.points_map[(x,y)]
            if (x,py) in self.points_map and (px,y) in self.points_map:
                count += self.points_map[(x,py)] * self.points_map[(px,y)]
        return count