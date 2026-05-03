class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] numbers = new int[26];
        for (int i = 0; i < s.length(); i++) {
            numbers[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < t.length(); i++) {
            numbers[t.charAt(i) - 'a']--;
        }

        for (int i = 0; i < 26; i++) {
            if (numbers[i] != 0) {
                return false;
            }
        }
        return true;
    }
}
