class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counts = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int i = 0; i < nums.length; i++) {
            counts.put(nums[i], counts.getOrDefault(nums[i], 0) + 1);
        }
        
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }


        int[] res = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i > 0 && index < k; i--) {
            for (int n : freq[i]) {
                res[index] = n;
                if (index == k) {
                    return res;
                }
                index++;
            }
        }
        return res;
    }
}
