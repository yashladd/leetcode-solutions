class Solution {
    public int numBusesToDestination(int[][] routes, int source, int target) {
        if (source == target) return 0;

        // 1. Map each stop to the buses that visit it
        Map<Integer, List<Integer>> stopsToBuses = new HashMap();
        for (int bus = 0; bus < routes.length; bus++) {
            for (int stop : routes[bus]) {
                stopsToBuses.computeIfAbsent(stop, k -> new ArrayList()).add(bus);
            }
        }

        // 2. Initialize BFS
        Queue<int[]> q = new LinkedList<>();
        Set<Integer> visitedBuses = new HashSet<>();
        
        if (!stopsToBuses.containsKey(source)) return -1;
        
        for (int busIdx : stopsToBuses.get(source)) {
            q.add(new int[]{busIdx, 1}); // {bus_index, count_of_buses_taken}
            visitedBuses.add(busIdx);
        }

        // 3. Perform BFS
        while (!q.isEmpty()) {
            int[] hopInfo = q.poll();
            int currentBus = hopInfo[0];
            int busCount = hopInfo[1];

            for (int stop : routes[currentBus]) {
                if (stop == target) return busCount;

                // Add all unvisited buses passing through this stop
                for (int nextBus : stopsToBuses.get(stop)) {
                    if (!visitedBuses.contains(nextBus)) {
                        visitedBuses.add(nextBus);
                        q.add(new int[]{nextBus, busCount + 1});
                    }
                }
            }
        }

        return -1;
    }
}