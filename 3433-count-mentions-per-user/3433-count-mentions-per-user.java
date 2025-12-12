class Solution {
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {

        Collections.sort(events, (List<String> a, List<String>  b) -> {
            int timeA = Integer.parseInt(a.get(1));
            int timeB = Integer.parseInt(b.get(1));
            if (timeA != timeB) return Integer.compare(timeA, timeB);
            return a.get(0).equals("OFFLINE") ? -1 : 1;
        });

        System.out.println(events);

        int[] nextAvailable = new int[numberOfUsers];
        int[] mentions = new int[numberOfUsers];


        for (List<String> e: events) {
            String type = e.get(0);
            int ts = Integer.parseInt(e.get(1));
            if (type.equals("OFFLINE")) {
                int id = Integer.parseInt(e.get(2));
                nextAvailable[id] = ts + 60;
            } else {
                String mention = e.get(2);
                if (mention.equals("ALL")) {
                    for (int id = 0; id < numberOfUsers; id++) {
                        mentions[id] += 1;
                    }
                } else if (mention.equals("HERE")) {
                    for (int id = 0; id < numberOfUsers; id++) {
                        if (nextAvailable[id] <= ts) mentions[id] += 1;
                    } 
                } else {
                    List<Integer> ids = Arrays.stream(e.get(2).split(" "))
                                        .map((String s) -> Integer.parseInt(s.substring(2)))
                                        .collect(Collectors.toList());
                    for (int id: ids) {
                        System.out.println(id);
                        mentions[id]++;
                    }
                }
            }
        }
        return mentions;
    }
}