class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_num = defaultdict(int)
        topk= defaultdict(int)
        for n in nums:
            if n in counter_num:
                counter_num[n]+=1
            else:
                counter_num[n]=1
            if counter_num[n] > min(topk.values(),default=0) or len(topk)<k:
                topk[n]= counter_num[n]
                # print(f"len(topk): {len(topk)}, k: {k}, topk: {topk}")
                if len(topk)>k:
                    min_key = min(topk, key=topk.get)
                    del topk[min_key]
                # topk.append(n)
        return list(topk.keys())