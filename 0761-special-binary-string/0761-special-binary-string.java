class Solution {

    public String makeLargestSpecial(String s) {
        /**
        
        1 1 0 0 1 0 1 0 1 1 1 0 0 0
        
         */

        int cnt = 0, l = 0;
        List<String> specialSubs = new ArrayList<>();

        for (int r = 0; r < s.length(); r++) {
            int add = s.charAt(r) == '1' ? 1 : -1;
            cnt += add;
            if (cnt == 0) {
                specialSubs.add("1" + makeLargestSpecial(s.substring(l+1, r)) + "0");
                cnt = 0;
                l = r + 1;
            }
        }

        StringBuilder sb = new StringBuilder();
        specialSubs.sort(Comparator.reverseOrder());
        for (String x: specialSubs) {
            sb.append(x);
        }
        return sb.toString();        
    }
}