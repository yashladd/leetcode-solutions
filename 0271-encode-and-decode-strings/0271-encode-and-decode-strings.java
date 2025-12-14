public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            // Format: Length + "#" + Content
            // Example: ["Hello", "World"] -> "5#Hello5#World"
            sb.append(s.length()).append("#").append(s);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            // 1. Find the delimiter '#' starting from current index 'i'
            int delimiterIndex = s.indexOf('#', i);
            
            // 2. Parse the length from the substring before the delimiter
            int length = Integer.valueOf(s.substring(i, delimiterIndex));
            
            // 3. Extract the string content using the length
            // Content starts after the delimiter (#)
            int contentStart = delimiterIndex + 1;
            int contentEnd = contentStart + length;
            
            String str = s.substring(contentStart, contentEnd);
            res.add(str);
            
            // 4. Move the pointer 'i' to the next segment
            i = contentEnd;
        }
        return res;
    }
}