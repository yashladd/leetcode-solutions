class Solution {
    public record Task(int enqTime, int processingTime, int idx) {}

    public int[] getOrder(int[][] tasks) {
        
        int n = tasks.length;
        int[][] indexedTasks = new int[n][3];

        for (int i = 0; i < n; i++) {
            indexedTasks[i][0] = tasks[i][0];
            indexedTasks[i][1] = tasks[i][1];
            indexedTasks[i][2] = i;
        }

        Arrays.sort(indexedTasks, (a, b) -> Integer.compare(a[0], b[0]));

        // Min Heap (PriorityQueue) for available tasks:
        // 1. Sort by shortest processingTime (a[1])
        // 2. Break ties by smallest original index (a[2])
        PriorityQueue<int[]> processingQueue = new PriorityQueue<>((a, b) -> {
            if (a[1] != b[1]) {
                return Integer.compare(a[1], b[1]);
            }
            return Integer.compare(a[2], b[2]);
        });

        int[] result = new int[n];
        long time = 0;
        int taskIndex = 0;
        int resultIndex = 0;

        while (resultIndex < n) {
            
            // Phase 1: Add all available tasks to the processing queue
            while (taskIndex < n && indexedTasks[taskIndex][0] <= time) {
                processingQueue.add(indexedTasks[taskIndex]);
                taskIndex++;
            }

            // Phase 2: Process the next task if the CPU is not idle
            if (!processingQueue.isEmpty()) {
                int[] currentTask = processingQueue.poll();
                
                // Add index to result
                result[resultIndex++] = currentTask[2]; 
                
                // Update time: CPU available time = current time + processing time
                time += currentTask[1];
            } 
            
            // Phase 3: Handle Idle Time
            else if (taskIndex < n) {
                // If the CPU is idle, jump time to the enqueue time of the next available task
                time = indexedTasks[taskIndex][0];
            }
        }

        return result;
    }
}