class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.size() == 0) {
            return false;
        }
        unordered_set<int> unique;
        for (const int &i: nums) {
            unique.insert(i);
        }
        
        return (unique.size() == nums.size()) ? false : true;
    }
};
