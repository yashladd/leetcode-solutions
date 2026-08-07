class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_cnt = defaultdict(int)

        for cp in cpdomains:
            cnt, domain = cp.split(" ")
            cnt = int(cnt)

            queue = deque(domain.split("."))

            while queue:
                visit_cnt[".".join(list(queue))] += cnt
                queue.popleft()

        return [f"{cnt} {domain}" for domain, cnt in visit_cnt.items()]
        