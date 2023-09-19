class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dx1 = points[1][0] - points[0][0]
        dx2 = points[2][0] - points[1][0]
        dy1 = points[1][1] - points[0][1]
        dy2 = points[2][1] - points[1][1]

        return dx1 * dy2 != dx2 * dy1