def naive_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    for i in range(N - M + 1):
        j = 0
        while j < M:
            if main_string[i + j] != pattern[j]:
                break
            j += 1
        if j == M:
            return i
    return -1