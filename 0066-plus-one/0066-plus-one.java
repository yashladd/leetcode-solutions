class Solution {
    public int[] plusOne(int[] digits) {

        int n = digits.length;

        int car = 0;

        List<Integer> res = new ArrayList<>();

        for (int i = n-1; i >=0 ; i--) {
            int dig = digits[i];
            if (i == n-1) {
                dig += 1;
            }
            dig += car;
            int curr = dig % 10;
            car = (int) dig/10;

            res.add(curr);
        }

        if (car != 0) {
            res.add(car);
        }

        Collections.reverse(res);

        return res.stream().mapToInt(i -> i).toArray();
        
    }
}