import concurrent.futures
from urllib.parse import urlparse

# class HtmlParser:
#    def getUrls(self, url: str) -> list[str]: ...

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        # Extract the target hostname
        target_hostname = urlparse(startUrl).hostname
        
        visited = {startUrl}
        
        # Helper function for the thread pool to execute
        def fetch_urls(url):
            return htmlParser.getUrls(url)
            
        # Initialize ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # Keep a set of running futures
            futures = {executor.submit(fetch_urls, startUrl)}
            
            while futures:
                # Wait for at least one thread to finish fetching its URLs
                done, futures = concurrent.futures.wait(
                    futures, 
                    return_when=concurrent.futures.FIRST_COMPLETED
                )
                
                for future in done:
                    new_urls = future.result()
                    for next_url in new_urls:
                        # Only process unvisited URLs that match the target hostname
                        if next_url not in visited and urlparse(next_url).hostname == target_hostname:
                            visited.add(next_url)
                            # Submit the new URL to the thread pool and track its future
                            futures.add(executor.submit(fetch_urls, next_url))
                            
        return list(visited)