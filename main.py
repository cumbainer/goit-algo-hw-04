import timeit

from boyer_moore import boyer_moore_search
from kmp import kmp_search
from naive import naive_search
from rabin_karp import rabin_karp_search
from texts import text1, text2

ALGORITHMS = {
    "Naive": naive_search,
    "Boyer-Moore": boyer_moore_search,
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp_search,
}

PATTERNS = {
    "text1": {
        "existing": "Лінійний або послідовний пошук",
        "fake": "цього підрядка точно немає у статті XYZ_123",
    },
    "text2": {
        "existing": "розгорнутий зв’язний список",
        "fake": "цього підрядка точно немає у статті XYZ_123",
    },
}

TEXTS = {"text1": text1, "text2": text2}

NUMBER = 1000


def measure(fn, text, pattern):
    return timeit.timeit(lambda: fn(text, pattern), number=NUMBER) / NUMBER


def main():
    results = {}
    for text_name, text in TEXTS.items():
        results[text_name] = {}
        for pattern_kind, pattern in PATTERNS[text_name].items():
            results[text_name][pattern_kind] = {}
            for algo_name, fn in ALGORITHMS.items():
                avg_seconds = measure(fn, text, pattern)
                results[text_name][pattern_kind][algo_name] = avg_seconds

    header = f"{'Text':<7} {'Pattern':<10} {'Algorithm':<13} {'Avg time (µs)':>15}"
    print(header)
    print("-" * len(header))
    for text_name, by_kind in results.items():
        for pattern_kind, by_algo in by_kind.items():
            for algo_name, seconds in by_algo.items():
                print(f"{text_name:<7} {pattern_kind:<10} {algo_name:<13} {seconds * 1e6:>15.2f}")

    print("\nFastest algorithm per scenario:")
    for text_name, by_kind in results.items():
        for pattern_kind, by_algo in by_kind.items():
            winner = min(by_algo, key=by_algo.get)
            print(f"  {text_name} / {pattern_kind:<8}: {winner}")

    print("\nFastest algorithm per text (sum of existing + fake):")
    for text_name, by_kind in results.items():
        totals = {algo: sum(by_kind[k][algo] for k in by_kind) for algo in ALGORITHMS}
        winner = min(totals, key=totals.get)
        print(f"  {text_name}: {winner}  (totals: " +
              ", ".join(f"{a}={t * 1e6:.2f}µs" for a, t in totals.items()) + ")")

    print("\nOverall fastest algorithm across both texts and both pattern kinds:")
    grand = {algo: 0.0 for algo in ALGORITHMS}
    for by_kind in results.values():
        for by_algo in by_kind.values():
            for algo, sec in by_algo.items():
                grand[algo] += sec
    winner = min(grand, key=grand.get)
    print(f"  {winner}  (totals: " +
          ", ".join(f"{a}={t * 1e6:.2f}µs" for a, t in grand.items()) + ")")

    return results


main()
