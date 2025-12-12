import java.util.*;

class Solution {

    private record TaskEntry(int remainingCount, int timeAvailable) {} 

    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> cnt = new HashMap<>();
        for (char t : tasks) {
            cnt.put(t, cnt.getOrDefault(t, 0) + 1);
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int count : cnt.values()) {
            maxHeap.add(count);
        }

        Deque<TaskEntry> coolingQueue = new ArrayDeque<>();
        
        int time = 0;

        while (!maxHeap.isEmpty() || !coolingQueue.isEmpty()) {
            time++;

            if (!maxHeap.isEmpty()) {
                int currCnt = maxHeap.poll();
                currCnt--;
                
                if (currCnt > 0) {
                    int nextAvailable = time + n;
                    coolingQueue.addLast(new TaskEntry(currCnt, nextAvailable));
                }
            }

            if (!coolingQueue.isEmpty() && coolingQueue.peekFirst().timeAvailable() <= time) {
                TaskEntry readyTask = coolingQueue.removeFirst();
                
                maxHeap.add(readyTask.remainingCount());
            }
        }

        return time;
    }
}