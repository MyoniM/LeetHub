class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
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
                temp = s[st[-1]:i + 1]
                s = s[:st[-1]] + temp[::-1] + s[i + 1:]
                del st[-1]

        # To store the modified string
        res = ""
        for i in range(lenn):
            if (s[i] != ')' and s[i] != '('):
                res += (s[i])
        return res