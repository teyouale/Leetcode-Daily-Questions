from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        root = [i for i in range(n)]
        email_group = defaultdict(list)
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                root[rootY] = rootX
        for i in range(n):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                if email not in email_group:
                    email_group[email] = i
                else:
                    union(i, email_group[email])
        components = defaultdict(list)
        for email,group in email_group.items():
            components[find(group)].append(email)
        
        merged_accounts = []
        for group,emails in components.items():
            name = accounts[group][0]
            merged_accounts.append([name,*(sorted(emails))])
        return merged_accounts
