class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # 1. Parse and store data WITH the original index
        # We group by name to reduce comparisons
        name_to_info = collections.defaultdict(list)
        
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            # Store: (time, amount, city, original_index)
            name_to_info[name].append((int(time), int(amount), city, i))
            
        # Use a set to store INDICES of invalid transactions to handle duplicates correctly
        invalid_indices = set()
        
        for name, info_list in name_to_info.items():
            # Sort by time (optional, but good practice)
            # info_list.sort() 
            
            for i in range(len(info_list)):
                time1, amount1, city1, idx1 = info_list[i]
                
                # Rule 1: Amount > 1000
                if amount1 > 1000:
                    invalid_indices.add(idx1)
                
                # Rule 2: Conflict within 60 mins in different city
                # We check against all other transactions for this name
                for j in range(len(info_list)):
                    if i == j: continue
                    time2, amount2, city2, idx2 = info_list[j]
                    
                    if city1 != city2 and abs(time1 - time2) <= 60:
                        invalid_indices.add(idx1)
                        invalid_indices.add(idx2)
                        
        # 3. Build the final result using the original list and invalid indices
        return [transactions[i] for i in invalid_indices]