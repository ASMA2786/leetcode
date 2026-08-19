class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict={}
        for i in range(len(s)-9):
            req=s[i:i+10]
            if req in dict:
                dict[req]+=1
            else:
                dict[req]=1
        arr=[]
        for req in dict:
            if dict[req]>1:
                arr.append(req)
        return arr