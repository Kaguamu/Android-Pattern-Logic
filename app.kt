object AndroidPattern {
    private val skip = Array(10) { IntArray(10) }

    init {
        skip[1][3] = 2; skip[3][1] = 2
        skip[4][6] = 5; skip[6][4] = 5
        skip[7][9] = 8; skip[9][7] = 8
        skip[1][7] = 4; skip[7][1] = 4
        skip[2][8] = 5; skip[8][2] = 5
        skip[3][9] = 6; skip[9][3] = 6
        skip[1][9] = 5; skip[9][1] = 5
        skip[3][7] = 5; skip[7][3] = 5
    }

    fun isValidPattern(seq: List<Int>, minLen: Int = 4): Boolean {
        if (seq.size < minLen) return false
        if (seq.any { it !in 1..9 }) return false
        val used = BooleanArray(10)
        var prev = seq[0]
        used[prev] = true
        for (i in 1 until seq.size) {
            val cur = seq[i]
            if (used[cur]) return false
            val middle = skip[prev][cur]
            if (middle != 0 && !used[middle]) return false
            used[cur] = true
            prev = cur
        }
        return true
    }

    fun matches(stored: List<Int>, attempt: List<Int>): Boolean {
        return stored == attempt && isValidPattern(attempt)
    }

}

