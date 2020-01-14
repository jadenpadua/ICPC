#include <unordered_map>
#include <string>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> umap;
        vector<int> indeces;
  
         for(int i = 0; i < nums.size(); i++) {
            int currentSum = target - nums[i];
            if (umap.find(currentSum) != umap.end()) {
                indeces.push_back(umap[currentSum]);
                indeces.push_back(i);
                return indeces;
            }
            else {
                umap[nums[i]] = i;
            }
         }
        return {};
     }
    
};
