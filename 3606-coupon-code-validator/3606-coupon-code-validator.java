
class Solution {

    // Define the valid business line priorities (Hint 3)
    private static final Map<String, Integer> PRIORITY_MAP = new HashMap<>();
    static {
        PRIORITY_MAP.put("electronics", 0);
        PRIORITY_MAP.put("grocery", 1);
        PRIORITY_MAP.put("pharmacy", 2);
        PRIORITY_MAP.put("restaurant", 3);
    }

    // A simple container class to hold valid data and its sort keys
    private static class Coupon {
        String code;
        String businessLine;

        public Coupon(String code, String businessLine) {
            this.code = code;
            this.businessLine = businessLine;
        }
    }

    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        
        int n = code.length;
        List<Coupon> validCoupons = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String currentCode = code[i];
            String currentBusiness = businessLine[i];
            
            // Validation Rule 3: isActive[i] is true
            if (!isActive[i]) {
                continue;
            }

            // Validation Rule 2: businessLine[i] is one of the four categories
            if (!PRIORITY_MAP.containsKey(currentBusiness)) {
                continue;
            }
            
            // Validation Rule 1: code[i] is non-empty AND consists only of alphanumeric and underscores
            if (currentCode == null || currentCode.isEmpty()) {
                continue;
            }
            
            // Validation Rule 1 (cont): Check character set
            // The regex "\\w+" is equivalent to "[a-zA-Z0-9_]+"
            // We use .matches("...") to check if the *entire* string conforms to the pattern.
            if (!currentCode.matches("^[a-zA-Z0-9_]+$")) {
                 continue;
            }
            
            // If all checks pass, it's a valid coupon
            validCoupons.add(new Coupon(currentCode, currentBusiness));
        }

        // Custom Sorting: 1. Business Line Priority, 2. Code Lexicographically
        validCoupons.sort((c1, c2) -> {
            int priority1 = PRIORITY_MAP.get(c1.businessLine);
            int priority2 = PRIORITY_MAP.get(c2.businessLine);

            // 1. Sort by Priority (Ascending)
            if (priority1 != priority2) {
                return Integer.compare(priority1, priority2);
            }

            // 2. Sort by Code Lexicographically (Ascending)
            return c1.code.compareTo(c2.code);
        });
        
        // Final Mapping to List<String> of codes
        List<String> result = new ArrayList<>();
        for (Coupon c : validCoupons) {
            result.add(c.code);
        }

        return result;
    }
}