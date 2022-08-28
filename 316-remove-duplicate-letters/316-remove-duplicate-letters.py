class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        st = []
        sc = defaultdict(int)
        for c in s:
            if sc[c] != 0:
                count[c] -= 1
                continue
            while st and count[st[-1]] > 0 and c < st[-1]:
                p = st.pop()
                sc[p] -= 1
            st.append(c)
            sc[c] += 1
            count[c] -= 1
        return "".join(st)