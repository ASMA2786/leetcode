class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res={}
        for s in strs:
            key=''.join(sorted(s))
            if key not in res:
                res[key]=[]
            res[key].append(s)
        return list(res.values())