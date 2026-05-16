# Sorting Algorithm Benchmark

**Array size:** 1,000,000
**Input type:** random uniform
**Environment:** 14 cores (M4 pro) / macOS / 24GB RAM / Python 3.14

| Algorithm            | Description / Usage | Run 1 (s) | Run 2 (s) | Run 3 (s) | Avg (s) |
|----------------------|---------------------|-:|---:|---:|---:|
| Bubble sort (100k)   | O(n^2)              |  | | | |
| Selection sort(100k) | O(n^2)              | 133.672s |126.260s | 132.197s| 130.710s |
| Insertion sort(100k) | O(n^2)              | 156.016s | 146.304s|149.060s | 150.460s|
| Merge sort (1mil)    | O(nlogn)            | 2.636s | 2.678s| 2.659s| 2.657s|
| Quick sort (1mil)    | O(nlogn)            | 1.329s | 1.267s| 1.293s| 1.296s|
| Timsort              | O(nlogn)            |  0.112s| 0.124s| 0.127s| 0.121s|
| Bucket sort          | O(nlogn)            | 0.584s |0.592s | 0.617s|0.570s |

## Notes

- Each run uses a freshly generated random array (same seed scheme across algos for fairness).
- O(n²) algos skipped at 1M — benchmarked separately at smaller n.
- Avg = mean of 3 runs. Std dev not meaningful at n=3.
- The experiment was run on [-300k, 300k] int range

## Insertion sort results
1. It can be the fastest algorithm when the size of array is very small. 
I did the test between quicksort and insertion sort on different array sizes - and the result is:
The insertion sort performed better at arrays with size < 30 elements. Otherwise - quicksort was always better

2. Its adaptive, so it performs better when data is partially sorted

## Quicksort results
Quicksort sorting time was reduced from avg ~1.2 sec to 28.7 sec when i **reduced the arr elements range 
to [-500, 500] (from -300k, 300k)**

If make to even less - [-100, 100] - the avg sorting time is way higher - **137.174sec**. There must be some exponential graph here relation-wise

So here the consequence is:
1) Quicksort is good when the **data distribub
2) Quicksort is good when there are memory restrictions. Because it does sorting in place and worst Space Complexion 
is O(logn)


## Mergesort results

1. Merge sort is pretty stable. Its performance kept the same throughout all range changing experiments.
Well, mergesort is stable (keeps the original order the same after sorting) - which makes it the mest sorting algorithm where
constant stability is required

2. Mergesort is adaptive. So when its already known that data is partially sorted - mergesort will be a good option

## Timsort
Well its obvious that this is the best sorting algorithm, because it was created by considering done mistakes
It divides the array into groups (runs), does each run sorting by using **insertion sort**, and then does the merge by the **Merge Sort** 

## Bucketsort
This is a base algorithm for Radix Sort, which is used haavily in many different systems, like Postgres, TimeScaleDB, and more

Is kinda more "engineer" sort, which allows parallel sorting and external sorting 
It is good when:
1. Data range is evenly distributed across known range
2. floating point numbers. Incredible performance here
