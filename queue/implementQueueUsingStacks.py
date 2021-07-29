class MyQueue:

    container = [0] * 100
    queue_top = 0
    queue_bottom = 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = [0] * 100
        self.queue_top = 0
        self.queue_bottom = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.container[self.queue_bottom] = x
        self.queue_bottom += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp = self.container[self.queue_top]
        self.container[self.queue_top] = 0
        self.queue_top += 1
        return temp

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        temp = self.container[self.queue_top]
        return temp

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.queue_top == self.queue_bottom:
            return True
        else:
            return False

# 问题 实现队列，
# 边缘 判断队列满了，队列空了

# 实现方案 队列特性 先入先出，使用两个变量来标识队头，队尾

# 直接实现即可

# 反馈
# 当前队列 没有充分利用空间，要以使用环形队列来实现充分利用空间

if __name__ == "__main__":
    # print("hello")
    # ["MyQueue", "push", "push", "peek", "pop", "empty"]
    # [[], [1], [2], [], [], []]
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)



    # print(myQueue.peek(),myQueue.pop(),myQueue.empty())
    print(myQueue.peek(),myQueue.pop(),myQueue.empty())