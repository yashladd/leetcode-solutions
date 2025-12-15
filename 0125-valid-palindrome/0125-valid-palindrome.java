class Solution {
    public boolean isPalindrome(String s) {
        String st = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return st.equals(new StringBuilder(st).reverse().toString());
    }
}