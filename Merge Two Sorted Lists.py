from typing import Optional

"""Вам даны заголовки двух отсортированных связанных списков list1 и list2. Объедините два списка в один
отсортированный список. Список должен быть составлен путем соединения узлов первых двух списков. Возвращает заголовок
объединенного связанного списка."""


# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}"


# def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     merged = ListNode(0)
#     result = merged
#
#     while l1 and l2:
#         if l1.val < l2.val:
#             merged.next = ListNode(l1.val)
#             l1 = l1.next
#         else:
#             merged.next = ListNode(l2.val)
#             l2 = l2.next
#
#         merged = merged.next
#
#     while l1:
#         merged.next = ListNode(l1.val)
#         l1 = l1.next
#         merged = merged.next
#     while l2:
#         merged.next = ListNode(l2.val)
#         l2 = l2.next
#         merged = merged.next
#
#     return result.next
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    current = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2.next
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return dummy.next


data1 = ListNode([1, 2, 4])
data2 = ListNode([1, 3, 4])
data3 = mergeTwoLists(data1, data2)
print(data3)
