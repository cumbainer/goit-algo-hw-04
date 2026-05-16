import gc
import random
import sys
import time

Array = list[int]


def get_list(size=1_000_000, arr_min=-300_000, arr_max=300_000):
    return [random.randint(arr_min, arr_max) for i in range(size)]


def bubble_sort(arr: Array):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t


def insertion_sort(arr: Array):
    n = len(arr)
    for i in range(n):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def quick_sort(arr: list):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(arr) - 1)


def mergesort(arr: list[int]):
    def merge(left_arr, right_arr):
        sorted_list = []
        l, r = 0, 0
        while l != len(left_arr) or r != len(right_arr):
            if l == len(left_arr):
                sorted_list.append(right_arr[r])
                r += 1
            elif r == len(right_arr):
                sorted_list.append(left_arr[l])
                l += 1
            elif left_arr[l] <= right_arr[r]:
                sorted_list.append(left_arr[l])
                l += 1
            else:
                sorted_list.append(right_arr[r])
                r += 1

        return sorted_list

    def divide(array, start, end):
        mid = (start + end) // 2
        if start == end:
            return [array[start]]

        left = divide(array, start, mid)
        right = divide(array, mid + 1, end)
        return merge(left, right)

    return divide(arr, 0, len(arr) - 1)


def bucketsort(arr: list[int]) -> list[int]:
    n = len(arr)
    lo, hi = min(arr), max(arr)
    if lo == hi:
        return arr[:]
    span = hi - lo + 1

    def bucket_idx(x):
        return (x - lo) * n // span

    def do_insertion_sort(a):
        for i in range(1, len(a)):
            tmp = a[i]
            j = i
            while j > 0 and tmp < a[j - 1]:
                a[j] = a[j - 1]
                j -= 1
            a[j] = tmp

    buckets = [[] for _ in range(n)]
    for x in arr:
        buckets[bucket_idx(x)].append(x)

    out = []
    for b in buckets:
        do_insertion_sort(b)
        out.extend(b)
    return out

def heapsort(arr:list[int]):
    pass



def benchmark(sort_fn, size=100_000, runs=3):
    sys.setrecursionlimit(10 ** 6)
    times = []
    for i in range(runs):
        arr = get_list(size=size, arr_min=-300_000, arr_max=300_000)
        expected = sorted(arr)

        gc.collect()
        gc.disable()
        t0 = time.perf_counter()
        sort_fn(arr)
        t1 = time.perf_counter()
        gc.enable()

        elapsed = t1 - t0
        assert arr == expected, f"Run {i + 1}: sort broken"
        times.append(elapsed)
        print(f"Run {i + 1}: {elapsed:.7f}s")

    avg = sum(times) / len(times)
    print(f"Avg: {avg:.7f}s | Min: {min(times):.7f}s | Max: {max(times):.7f}s")
    return times

# 0.0000093s - q
# 0.0000071s - i

def main():
    benchmark(bubble_sort)


main()
