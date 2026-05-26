#Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель,
# використовуючи з'єднувачі, у порядку, який призведе до найменших витрат.
# Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
import heapq
from heapq import heapify


# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

#NAIVE the most optimal approach. Can do better? Yes, with heaps
def link_cables(cables):
    if len(cables) < 2:
        return 0
    cables = quicksort(cables, 0, len(cables) - 1)
    current = cables[0]
    total_cost = 0
    for i in range(1, len(cables)):
        current += cables[i]
        total_cost += current
    return total_cost

def quicksort(arr, start, end):
    if start >= end:
        return arr

    pivot_val = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[end] = arr[end], arr[i]

    quicksort(arr, start, i - 1)
    quicksort(arr, i + 1, end)
    return arr

v = link_cables([1, 12, 5, 10, 5, 3, 5])
print(f"Link cables without heaps best: {v}")



def link_cables_heap(cables):
    heapify(cables)
    total_sum = 0
    while len(cables) != 1:
        min_elements_sum = heapq.heappop(cables) + heapq.heappop(cables)
        total_sum += min_elements_sum
        heapq.heappush(cables, min_elements_sum)
    return total_sum

result = link_cables_heap([1, 12, 5, 10, 5, 3, 5])
print(f"Link cables without heaps best: {result}")
