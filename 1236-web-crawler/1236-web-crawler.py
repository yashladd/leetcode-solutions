class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        q = deque([startUrl])
        vis = set([startUrl])

        def get_hostname(u):
            # u = u.split("//")
            return u.split("/")[2]

        def same_hostname(u):
            return get_hostname(u) == get_hostname(startUrl)

        while q:
            currUrl = q.popleft()

            urls = htmlParser.getUrls(currUrl)

            for u in urls:
                if u not in vis and same_hostname(u):
                    vis.add(u)
                    q.append(u)

        return list(vis)