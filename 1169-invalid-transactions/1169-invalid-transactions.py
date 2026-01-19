class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        name_to_info = collections.defaultdict(list)
        
        # 1. Parse and store with original index
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            name_to_info[name].append((int(time), int(amount), city, i))
            
        invalid_indices = set()
        
        for name, info_list in name_to_info.items():
            # 2. Sort by time to enable early breaking (Optimization)
            info_list.sort(key=lambda x: x[0])
            
            for i in range(len(info_list)):
                time1, amount1, city1, idx1 = info_list[i]
                
                # Rule 1: Amount > 1000
                if amount1 > 1000:
                    invalid_indices.add(idx1)
                
                # Rule 2: Conflict check with pruning
                # We only need to check 'next' items. If we find a conflict, we mark BOTH.
                for j in range(i + 1, len(info_list)):
                    time2, amount2, city2, idx2 = info_list[j]
                    
                    # OPTIMIZATION: Stop checking if time diff exceeds 60
                    if time2 - time1 > 60:
                        break
                    
                    if city1 != city2:
                        invalid_indices.add(idx1)
                        invalid_indices.add(idx2)
                        
        return [transactions[i] for i in invalid_indices]