class Solution {
    public String[] sortFeatures(String[] features, String[] responses) {
        int n = features.length;
        Map<String, Integer> respCnt = new HashMap<>();
        for (String s: features) {
            respCnt.put(s, 0);
        }

        int N = responses.length;

        for (int i = 0; i < N; i ++) {
            // Set<String> res = responses[i].split(" ").stream().collect(Collectors.toSet());
            Set<String> res = Arrays.stream(responses[i].split(" ")).collect(Collectors.toSet());
            // Set<String> res1 = new HashSet<>(Arrays.asList(responses[i].split(" ")));
            for (String s: res) {
                respCnt.put(s, respCnt.getOrDefault(s, 0) + 1);
            }
            
        }
        
        Arrays.sort(features, (a, b) -> respCnt.get(b) - respCnt.get(a));

        return features;


        
    }
}