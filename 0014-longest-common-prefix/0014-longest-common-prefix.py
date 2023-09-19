class Solution:
    def longestCommonPrefix(self, list: List[str]) -> str:
        ans = ""

        sortedList = sorted(list)
        first = sortedList[0]
        last = sortedList[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans