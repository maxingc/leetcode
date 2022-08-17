# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    ## 双指针 证明过程：https://leetcode.cn/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
    def detectCycle(self, head: ListNode) -> ListNode:

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                ans = head
                while ans!=slow:
                    ans = ans.next
                    slow = slow.next
                return ans
        return None

    ## 哈希表
    def detectCycle2(self, head: ListNode) -> ListNode:

        lookup = set()
        lookup.add(head)

        cur = head

        while cur:
            if cur.next in lookup:
                return cur.next
            lookup.add(cur.next)
            cur = cur.next

        return None