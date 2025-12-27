class Solution {
    public boolean canWinNim(int n) {
        /**
        8  1, 7 L   2, 6 L  3, 5 L

        7   1, 6   2, 5  3, 4 W

        6   1, 5 L  2, 4 W   3, 3 L  Win


        5   3, 2 L    1, 4 W   2, 3 L   Win


        4   1, 3
            3, 1 ---> Lose

            2, 2  Lose

            3, 1  L 

        3  3,0 W
        
        2 W

        1 W


         */

        return (n % 4) != 0;
        
    }
}