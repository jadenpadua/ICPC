class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indeces;
        for(int i = 0; i < nums.size()-1; i++) {
            for(int j = i + 1; j <nums.size(); j++) {
                int currentSum = nums[i] + nums[j];
                if(currentSum == target) {
                    indeces.push_back(i);
                    indeces.push_back(j);
                    return indeces;
                }
            }
        }
        
        return {};
    }
    
    
};
