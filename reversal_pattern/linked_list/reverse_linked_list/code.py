class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next  # store the next node
        curr.next = prev  # reverse the link
        prev = curr  # move prev forward
        curr = nxt  # move the current node forward

    return prev
