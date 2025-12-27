class Solution {

    void rec(String curr, List<String> res) {

        
    }
    public List<String> generatePossibleNextMoves(String currentState) {

        List<String> res = new ArrayList<>();

        for (int i = 0; i < currentState.length() - 1; i++) {
            if (currentState.charAt(i) == '+' && currentState.charAt(i+1) == '+') {
                String nextState = currentState.substring(0, i) + "--" + currentState.substring(i+2, currentState.length());
                res.add(nextState);
            }
        }

        return res;
        
    }
}