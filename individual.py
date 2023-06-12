import numpy as np

class Individual:
    def __init__(self, points, order=None):
        self.points = points
        self.order = order if order is not None else np.random.permutation(len(points))

    def score(self):
        total_distance = 0
        for i in range(len(self.order)):
            start = self.order[i]
            end = self.order[(i + 1) % len(self.order)]
            x1, y1 = self.points[start]
            x2, y2 = self.points[end]
            distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            total_distance += distance
        return total_distance