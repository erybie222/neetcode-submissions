class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        window = {}

        res = (-1, -1)
        minLength = float('inf')
        
        for c in t:
            t_dict[c] = t_dict.get(c, 0 ) + 1

        need, have = len(t_dict), 0
        l , r = 0 , 0

        while r < len(s):
            if s[r] in t_dict:
                window[s[r]] = window.get(s[r], 0) + 1

                if window[s[r]] == t_dict[s[r]]:
                    have += 1
                
                while have == need:
                    if r - l + 1 <= minLength:
                        res = (l, r)
                        minLength = r - l + 1
                    if s[l] in t_dict:
                        window[s[l]] = window.get(s[l], 0) - 1
                        if window[s[l]] < t_dict[s[l]]:
                            have -= 1
                    l += 1
            r += 1
        if res != (-1, -1):
            return s[res[0] : res[1] +1]
        else:
            return ""


                