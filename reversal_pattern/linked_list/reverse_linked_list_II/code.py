class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    start = prev.next
    end = start.next

    for _ in range(right - left):
        temp = start.next
        start.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next
