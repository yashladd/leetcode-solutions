class Solution {
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        // 1. Sort events: 
        // - By timestamp ascending
        // - If tie, process OFFLINE before MESSAGE
        Collections.sort(events, (a, b) -> {
            int timeA = Integer.parseInt(a.get(1));
            int timeB = Integer.parseInt(b.get(1));
            if (timeA != timeB) return Integer.compare(timeA, timeB);
            
            // "OFFLINE" should come before "MESSAGE"
            // We return -1 if a is OFFLINE, 1 if a is MESSAGE (assuming b is the other)
            return a.get(0).equals("OFFLINE") ? -1 : 1;
        });

        int[] mentions = new int[numberOfUsers];
        int[] onlineUntil = new int[numberOfUsers]; // Stores the time a user comes back online

        for (List<String> event : events) {
            String type = event.get(0);
            int time = Integer.parseInt(event.get(1));

            if (type.equals("OFFLINE")) {
                int id = Integer.parseInt(event.get(2));
                // User is offline for 60 units, back online at time + 60
                onlineUntil[id] = time + 60;
            } else {
                // MESSAGE Event
                String mentionStr = event.get(2);
                
                if (mentionStr.equals("ALL")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        mentions[i]++;
                    }
                } else if (mentionStr.equals("HERE")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        // User is online if current time >= the time they are back online
                        if (time >= onlineUntil[i]) {
                            mentions[i]++;
                        }
                    }
                } else {
                    // Handle specific ids like "id0 id1 id0"
                    // We split by space and process each token
                    String[] ids = mentionStr.split(" ");
                    for (String s : ids) {
                        // Skip the first 2 chars "id" and parse the rest
                        int id = Integer.parseInt(s.substring(2));
                        mentions[id]++;
                    }
                }
            }
        }
        
        return mentions;
    }
}