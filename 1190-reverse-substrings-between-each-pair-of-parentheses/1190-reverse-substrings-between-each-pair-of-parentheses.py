class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []#0,2
        # example case
        # s = "(u(love)i)"
        lenn = len(s)
        for i in range(lenn):

            # Push the index of the current
            # opening bracket
            if (s[i] == '('):
                st.append(i)

            # Reverse the substring starting
            # after the last encountered opening
            # bracket till the current character
            elif (s[i] == ')'):
                # i = 7
                temp = s[st[-1]:i + 1]
                # s[2:8]
                # (love)
                s = s[:st[-1]] + temp[::-1] + s[i + 1:]
                # s = s[:2] + evol + s[8:]
                st.pop()

        # To store the modified string
        res = ""
        for i in range(lenn):
            if s[i] not in ["(",")"]: res += s[i]
        return res