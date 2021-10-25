class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):  # 맨 위에 데이터 넣기
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현 - 맨 위의 데이터 뽑기
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):     # 맨 위의 데이터 보기
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # isEmpty 기능 구현 - 스택이 비었는지 안 비었는지 여부 반환해주기
    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop())