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


def intersection_auxillary(head1, head2):
    pass


interection_list = head_from_list(['c1', 'c2', 'c3'])
head1 = head_from_list(['a1', 'a2'])
head1.next.next = interection_list
head2 = head_from_list(['b1', 'b2', 'b3'])
head2.next.next.next = interection_list

pretty_print(head1)
pretty_print(head2)
