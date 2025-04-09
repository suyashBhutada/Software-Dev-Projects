class Solution:
    x = set()
    x = defaultdict(int)

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        main_array  = []
        sum_after_delay = 0
        for i in range(n):
            if(i == 0):
                main_array.append([1])
            else:
                main_array.append([])
        days = 1
        while(days <= n):
            last = main_array.pop()
            sum_after_delay -= len(last)
            new_to_add = len(main_array[delay])
            new = [1] * new_to_add
            sum_after_delay += new_to_add
            main_array = [new] + main_array
            days += 1 
        return sum_after_delay



