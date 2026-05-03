class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String s : strs) {
            res.append(s.length()).append("#").append(s);

        }
        return res.toString();

    }

    public List<String> decode(String str) {
        List<String> ans = new ArrayList<>();
        int i = 0; // should be the first number of the length of the first string
        while (i < str.length()) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            // set the length as the number readed:
            int len = Integer.valueOf(str.substring(i, j));
            ans.add(str.substring(j + 1, j + 1 + len));
            i = j+1+len;

        }

        return ans;
    }
}
