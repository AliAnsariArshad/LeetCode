class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        le = len(self.arr)
        self.arr.sort()
        if le == 1:
            return self.arr[0]
        if le == 2:
            return (self.arr[0] + self.arr[1]) /2

        if le % 2 != 0:
            return self.arr[le // 2]
        else:
            return (self.arr[(le // 2) - 1] + self.arr[(le // 2)]) / 2



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(10)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(2)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(5)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(0)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(6)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(1)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(0)
param_2 = obj.findMedian()
print(param_2)
obj.addNum(0)
param_2 = obj.findMedian()
print(param_2)