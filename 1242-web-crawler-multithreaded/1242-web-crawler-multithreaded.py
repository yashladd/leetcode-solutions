import threading
from concurrent.futures import ThreadPoolExecutor

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # 1. Helper to extract hostname
        def get_hostname(url):
            # Split by "/" and take the 3rd element (index 2)
            # e.g. "http://example.com/foo" -> ["http:", "", "example.com", "foo"]
            return url.split('/')[2]

        target_hostname = get_hostname(startUrl)
        
        # 2. Thread-safe structures
        visited = {startUrl}
        lock = threading.Lock()
        
        # We start with the startUrl in our queue
        queue = [startUrl]
        
        # Use a ThreadPool to manage concurrency
        # 10-20 workers is usually a good balance for I/O tasks like this
        with ThreadPoolExecutor(max_workers=16) as executor:
            
            while queue:
                # Submit tasks for all URLs in the current level
                # This runs htmlParser.getUrls() in parallel
                futures = [executor.submit(htmlParser.getUrls, url) for url in queue]
                
                next_queue = []
                
                # Collect results as they finish
                for future in futures:
                    found_urls = future.result()
                    
                    for url in found_urls:
                        # Check hostname matches
                        if get_hostname(url) == target_hostname:
                            # Critical section: Check and add to visited
                            with lock:
                                if url not in visited:
                                    visited.add(url)
                                    next_queue.append(url)
                
                # Move to the next level
                queue = next_queue
                
        return list(visited)