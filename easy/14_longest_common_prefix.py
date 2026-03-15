class Solution(object):
    def longestCommonPrefix(self, strs):
        new = ""
        if new in strs or strs[0][0] != strs[-1][0]:
            return new
        if len(strs) == 1:
            return strs[0]
        for i in range(1, len(strs)):
            wrd = strs[i]
            flag = 0
            for char in wrd:
                if flag == len(strs[0]):
                    break
                if wrd.startswith(new + strs[0][flag]) and i <= 1:
                    new += strs[0][flag]
                    flag += 1
                elif not wrd.startswith(new) and new != "":
                    for i in new:
                        if not wrd.startswith(new) and new != "":
                            new = new[:-1]
                else:
                    break
        return new