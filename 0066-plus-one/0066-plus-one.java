class Solution {
    public int[] plusOne(int[] digits) {

        int [] res = Arrays.copyOf(digits, digits.length);
        for (int i = res.length -1 ; i >= 0 ; i--) {
            if (res[i] < 9) {
                res[i] += 1;
                return res;
            }
            res[i] = 0;
        }

        int [] allNinesRes = new int[res.length + 1];
        allNinesRes[0] = 1;
        return allNinesRes;
        
    }
}