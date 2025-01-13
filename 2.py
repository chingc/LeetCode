"""https://leetcode.com/problems/add-two-numbers/"""


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        head = None
        tail = None
        carry = 0

        while l1 or l2:
            a = 0
            b = 0

            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next

            total = a + b + carry

            if total > 9:
                carry = 1
                total %= 10
            else:
                carry = 0

            if not head:
                head = ListNode(val=total)
                tail = head
            else:
                tail.next = ListNode(val=total)
                tail = tail.next

        if carry:
            tail.next = ListNode(val=1)

        return head
