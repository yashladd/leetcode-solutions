class Solution {
    /**
     * 

                      0     1    0                    0 1 0
                                                      1 0 2


               [1    ,2]    [0,  2]       [1,2]   
              [0,2]  [1,0]  [1,2] [2,0]   



                0            1               2

               [1,2]       [0,2]           [1,0]
             [0,2] [1,0]  0,1 1,0



              f(2)= 3 x 


 

      * @param n
     * @return
     */

    public static final long MOD = 1000_000_007;

    public int numOfWays(int n) {
        long aba = 6, abc = 6;
        for (int i = 2; i <= n; i++) {
            long prevAba = aba;
            long prevAbc = abc;
            aba = (3 * prevAba + 2 * prevAbc) % MOD;
            abc = (2 * prevAba + 2 * prevAbc) % MOD;
        }
        return (int) ((aba + abc) % MOD);
    }
}