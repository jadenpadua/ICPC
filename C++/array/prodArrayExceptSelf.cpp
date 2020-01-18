class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector <int> output;
        int currentProduct = 1;
        
        for (int i = 0; i < nums.size(); i++) {
            vector<int> temp = nums;
            temp.erase(temp.begin()+i);
            for (auto x: temp) {
                currentProduct = currentProduct * x;
            }
            output.push_back(currentProduct);
    
            currentProduct = 1;
        }
        
        return output;
        
    return {1};
     
    }
};
