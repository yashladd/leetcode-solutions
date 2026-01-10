class Solution {
    // 1. Helper Record to store position and arrival time
    record Car(int position, double time) {}

    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        Car[] cars = new Car[n];

        // 2. Build the Car objects with calculated time
        for (int i = 0; i < n; i++) {
            double timeToTarget = (double)(target - position[i]) / speed[i];
            cars[i] = new Car(position[i], timeToTarget);
        }

        // 3. Sort by position (start -> end)
        Arrays.sort(cars, (a, b) -> Integer.compare(a.position(), b.position()));

        int fleets = 0;
        double maxTime = 0.0; // The time of the slowest car (bottleneck) found so far

        // 4. Iterate Backwards (from closest to target -> furthest)
        for (int i = n - 1; i >= 0; i--) {
            double currentTime = cars[i].time();

            // If this car takes LONGER than the fleet ahead, it can't catch up.
            // It becomes the new bottleneck (new fleet leader).
            if (currentTime > maxTime) {
                maxTime = currentTime;
                fleets++;
            }
            // Else: currentTime <= maxTime. 
            // This car is faster than the one ahead, so it catches up and joins that fleet.
            // We do nothing (count doesn't change, maxTime doesn't change).
        }

        return fleets;
    }
}