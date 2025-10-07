# android_pattern.py

from typing import List

# Precomputed skip matrix: skip[a][b] = node that is between a and b and must be visited first (0 for none)
_skip = [[0]*10 for _ in range(10)]

def _build_skip_matrix():
    # Horizontal and vertical middle skips
    _skip[1][3] = _skip[3][1] = 2
    _skip[4][6] = _skip[6][4] = 5
    _skip[7][9] = _skip[9][7] = 8
    _skip[1][7] = _skip[7][1] = 4
    _skip[2][8] = _skip[8][2] = 5
    _skip[3][9] = _skip[9][3] = 6
    # Diagonals
    _skip[1][9] = _skip[9][1] = 5
    _skip[3][7] = _skip[7][3] = 5
    # Others are zero (no required middle)
_build_skip_matrix()

def is_valid_pattern(seq: List[int], min_len: int = 4) -> bool:
    """
    Validate an Android-style unlock pattern.
    seq: list of nodes (1..9)
    min_len: minimum allowed pattern length
    """
    if not isinstance(seq, list) or any(not isinstance(x, int) or x < 1 or x > 9 for x in seq):
        return False
    n = len(seq)
    if n < min_len:
        return False

    used = [False]*10
    prev = seq[0]
    used[prev] = True

    for cur in seq[1:]:
        if used[cur]:
            # cannot reuse a node
            return False
        middle = _skip[prev][cur]
        if middle != 0 and not used[middle]:
            # moving from prev to cur requires middle already visited
            return False
        used[cur] = True
        prev = cur
    return True

def pattern_match(stored: List[int], attempt: List[int]) -> bool:
    """Check attempt matches stored pattern exactly (same sequence) and is valid."""
    return stored == attempt and is_valid_pattern(attempt)

# Basic tests
if _name_ == "_main_":
    tests = [
        ([1,2,3,6], True),       # OK
        ([1,3,2,5], False),      # 1->3 invalid because 2 not visited yet
        ([1,5,9], False),        # too short (min 4)
        ([2,4,1,3], True),       # 1->3 allowed because 2 visited earlier
        ([1,9,5,3], False),      # 1->9 invalid if 5 not visited yet
        ([1,5,9,3], True),       # valid
        ([1,2,1], False),        # reuse node
    ]
    for seq, expected in tests:
        print(f"{seq} -> {is_valid_pattern(seq)} (expected {expected})")
