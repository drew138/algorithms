# problem: https://leetcode.com/problems/design-underground-system/
# Runtime: 320 ms, faster than 16.26% of Python3 online submissions for Design Underground System.
# Memory Usage: 24.7 MB, less than 41.99% of Python3 online submissions for Design Underground System.


class UndergroundSystem:

    def __init__(self):
        self.stationsIn = {}
        self.stationsOut = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.stationsIn[id] = (id, stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        a, b, c = self.stationsIn[id]
        d, e = self.stationsOut.get(b+stationName, (0, 0))
        self.stationsOut[b+stationName] = d - c + t, e + 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        a, b = self.stationsOut.get(startStation+endStation, (0, 0))
        if b == 0:
            return None
        return a / b


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
