class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def pretty_print(head):
    temp = head
    while temp:
        if temp.next:
            print(temp.val, end=' -> ')
        else:
            print(temp.val)
        temp = temp.next


def head_from_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0], None)

    temp = None
    prev = head

    for i in range(1, len(lst)):
        val = lst[i]
        temp = ListNode(val, None)
        prev.next = temp
        prev = temp

    return head


def rearrange(head):
    def reverse(start, end=None):
        if not start:
            return None

        cur = start
        prev = end
        while cur != end:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

    if not head:
        return None

    dummy = ListNode('dummy', head)

    cur = head
    prev = dummy
    while cur:
        # go the next ' ' or None
        end = cur
        while end and end.val != ' ':
            end = end.next

        # reverse [cur, end)
        prev.next = reverse(cur, end)

        # if you reached the end: stop!
        if not end:
            break

        # adjust pointers (skip space): cur ends on 'H' and end finishes on ' '
        prev = cur.next
        cur = end.next

    return dummy.next


head = head_from_list(['H', 'e', 'y', ' ', 'W', 'o', 'r', 'l', 'd'])
pretty_print(rearrange(head))
