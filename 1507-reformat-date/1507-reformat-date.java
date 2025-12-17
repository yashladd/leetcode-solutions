class Solution {
    public String reformatDate(String date) {
    Map<String, String> mon = Map.ofEntries(
    Map.entry("Jan", "01"), Map.entry("Feb", "02"), Map.entry("Mar", "03"),
    Map.entry("Apr", "04"), Map.entry("May", "05"), Map.entry("Jun", "06"),
    Map.entry("Jul", "07"), Map.entry("Aug", "08"), Map.entry("Sep", "09"),
    Map.entry("Oct", "10"), Map.entry("Nov", "11"), Map.entry("Dec", "12")
);
        String[] d = date.split(" ");
        String day = d[0].substring(0, d[0].length() -2);
        String month = mon.get(d[1]);
        String year = d[2];
        if (day.length() == 1) {
            day = "0" + day;
        }
        return String.format("%s-%s-%s", year, month, day);
    }
}