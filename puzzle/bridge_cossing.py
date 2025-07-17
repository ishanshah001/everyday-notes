def min_crossing_time(times):
    times.sort()
    n = len(times)

    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return times[0]
    if n == 2:
        return times[1]
    if n == 3:
        return times[0] + times[1] + times[2]

    # Strategy 1: Fastest person returns
    # Send two slowest, fastest returns each time
    strategy1 = times[0] + 2 * times[1] + times[-1]

    # Strategy 2: Both fastest go together, slowest return with one
    strategy2 = 2 * times[0] + times[-2] + times[-1]

    # Choose the better of the two, and recurse on the remaining people
    return min(strategy1, strategy2) + min_crossing_time(times[:-2])

print(min_crossing_time([1, 2, 5, 10]))        # Output: 17
print(min_crossing_time([1, 2, 5, 8]))         # Output: 15
print(min_crossing_time([1, 4, 5, 8, 9, 12]))  # Output: 40
print(min_crossing_time([1, 3,6, 8, 12]))