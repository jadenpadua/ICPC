class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minElement = INT_MAX;
        int maxProfit = INT_MIN;
        int currentProfit;
        for (int i = 0; i < prices.size(); i++) {
            currentProfit = prices[i] - minElement;
            maxProfit = max(maxProfit, currentProfit);
            minElement = min(minElement, prices[i]);
        }
        
        return (maxProfit > 0) ? maxProfit : 0;
        
    }
};
