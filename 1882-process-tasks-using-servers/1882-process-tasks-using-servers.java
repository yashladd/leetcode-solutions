import java.util.PriorityQueue;

class Solution {

    public record Server(int wt, int idx) { }

    public record Next(long nextAvail, int idx) { } // long to avoid overflow

    public int[] assignTasks(int[] servers, int[] tasks) {
        int N = tasks.length;

        PriorityQueue<Server> available = new PriorityQueue<>((a, b) -> {
            if (a.wt != b.wt) return Integer.compare(a.wt, b.wt);
            return Integer.compare(a.idx, b.idx);
        });

        PriorityQueue<Next> nextAvailable = new PriorityQueue<>((a, b) -> {
            int cmp = Long.compare(a.nextAvail, b.nextAvail);
            if (cmp != 0) return cmp;
            // tie-break isn't strictly required for correctness, but makes behavior deterministic
            return Integer.compare(a.idx, b.idx);
        });

        int[] res = new int[N];

        for (int i = 0; i < servers.length; i++) {
            available.add(new Server(servers[i], i));
        }

        long time = 0;
        int resIdx = 0;

        while (resIdx < N) {
            // task resIdx arrives at second resIdx
            time = Math.max(time, (long) resIdx);

            // move all servers that became free by 'time' back to 'available'
            while (!nextAvailable.isEmpty() && nextAvailable.peek().nextAvail <= time) {
                Next s = nextAvailable.poll();
                available.add(new Server(servers[s.idx], s.idx));
            }

            if (available.isEmpty()) {
                // jump time to the next server release
                time = Math.max(time, nextAvailable.peek().nextAvail);
                continue;
            }

            Server s = available.poll();
            res[resIdx] = s.idx;

            long nextTime = time + (long) tasks[resIdx];
            nextAvailable.add(new Next(nextTime, s.idx));

            resIdx++;
        }

        return res;
    }
}
