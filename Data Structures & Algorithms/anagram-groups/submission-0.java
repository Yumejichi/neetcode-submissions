class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for (String s : strs) {
            int[] count = new int[26];
            for (int i = 0; i < s.length(); i++) {
                int letter = s.charAt(i) - 'a';
                count[letter]++;
            }

            String key = Arrays.toString(count);
            if (!result.containsKey(key)) {
                result.put(key, new ArrayList<>());
            }            
            result.get(key).add(s);
        }
        return new ArrayList<>(result.values());
    }
}
