#User function Template for python3

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        from collections import defaultdict
        g = defaultdict(list)
        u = set()
        for w in alien_dict:
            s = set(w)
            for x in s:
                u.add(x)
                
        prev = alien_dict[0]
        for curr in alien_dict[1:]:
            i, j = 0, 0 
            while i < len(prev) and j < len(curr) and prev[i] == curr[j]:
                i += 1
                j += 1
            if i < len(prev) and j < len(curr):
                g[prev[i]].append(curr[j])
            prev = curr
            
        
        vis = {}
        path = {}
        stk = []
        def dfs(node):
            vis[node] = 1
            
            path[node] = 1
            
            for nei in g[node]:
                if nei not in vis:
                    if dfs(nei):
                        return True
                        
                elif nei in path:
                    return True
                    
            del path[node]
            stk.append(node)
            return False
        
        for al in u:
            if al not in vis:
                dfs(al)
                
        
        return ''.join(stk[::-1])
    
        
        
            
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends