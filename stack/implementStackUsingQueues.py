class MyStack:
    container = []
    stack_top = -1

    def __init__(self):
        self.container = [0] * 100
        self.stack_top = -1
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.container[self.stack_top + 1] = x
        self.stack_top += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return None
        element = self.container[self.stack_top]
        self.container[self.stack_top] = None
        self.stack_top -= 1
        return element

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return None
        element = self.container[self.stack_top]
        return element

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack_top == -1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# 问题本身，使用队列实现栈
# 栈的特点：先入后出，使用一个标识栈顶，一个容器来装载数据
# 边缘：到栈底需要标识

# 解决问题方案
# 利用特点进行实现，从 -1 来标识

# 实现
# 没有问题

# 反思

if __name__ == "__main__":
    print("HelloWorld")

    # obj = MyStack()
    # obj.push(1)
    # param_2 = obj.pop()
    # param_3 = obj.push(2)
    # param_5 = obj.top()
    # param_4 = obj.empty()
    # print(param_2,param_3,param_4,param_5)

    w = range(5)
    print(range(5))
    print(type(w))
    print(w)
    # ["MyStack", "push", "pop", "push", "top"]
    # [[], [1], [], [2], []]