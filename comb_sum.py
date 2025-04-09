class Solution:
    def find(self,target,nums):
        if(len(nums)==1):
            if((target % nums[0]) != 0):
                return None
            else:
                return [{nums[0]:target/nums[0]}]
        current_ans = []
        for i, val in enumerate(nums):
            freq = 0.0
            while(freq * val < target):
                this_ans = {val:freq}
                ans = self.find(target - (freq * val), nums[:i] + nums[i+1:])
                if(ans != None):
                    for each_dict in ans:
                        current_ans.append(this_ans | each_dict)
                freq +=1
        return current_ans
    def combinationSum(self, candidates: list[int], target: int):
        ans = self.find(target, candidates)
        if(ans is None):
            return []
        new_dict = dict()
        for a in ans:
            key = ""
            for c in candidates:
                key = key +  "_"+  str(a.get(c,0.0))
            new_dict[key] = a
        mid_ans= list(new_dict.values() )
        ret = []
        for m in mid_ans:
            m_ret = []
            for k,v in m.items():
                if v > 0:
                    m_ret = m_ret + [k] * int(v)
            if(len(m_ret)):
                ret.append(m_ret)
        return ret


        