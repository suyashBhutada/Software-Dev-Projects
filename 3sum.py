class Solution:
    def search_sorted(self,sorted_num_tup, target, remove_index ):
        l = 0
        r = len(sorted_num_tup) -1
        ret_val = set()
        while(l<r):
            if(sorted_num_tup[l][0] == remove_index):
                l +=1
                continue
            if(sorted_num_tup[r][0]==remove_index):
                r -=1
                continue
            c_sum =sorted_num_tup[l][1] + sorted_num_tup[r][1]
            if(c_sum == target):
                ret_val.add(tuple([l,r]))
                l += 1
            elif(c_sum >target):
                r -=1
            else:
                l+= 1
        
        return ret_val

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        x = [tuple([i,nums[i]]) for i in range(len(nums))]
        sorted_num_tup = sorted(x, key=lambda tup: tup[1])
        ans = []
        for i in range(len(nums)):
            nums_i = nums[i]
            target = -1 * nums_i
            ret = self.search_sorted(sorted_num_tup,target,i)
            if len(ret):
                for xi in ret:
                    val = tuple([nums[i], sorted_num_tup[xi[0]][1],sorted_num_tup[xi[1]][1]])
                    ans.append(val)
        

        retans = []
        for a in range(len(ans)):
            ispresent = False
            for b in range(a):
                if(set(ans[a]) == set(ans[b])):
                    ispresent = True
                    break
            if not ispresent:
                retans.append(list(ans[a]))
        return retans
    
print(Solution().threeSum([0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]))
