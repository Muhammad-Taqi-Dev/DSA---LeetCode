class Solution {
public:
    int maxArea(vector<int>& height) {
        int l  = 0;
        int r = height.size()-1;
        int area = 0;
        while(l<r){
            int containerheight = min(height[r] , height[l]);
            int width = r - l;
            area = max(area, width * containerheight);
            if(height[l] > height[r]){
                r--;
            }
            else{
                l++;
            }
        }
        return area;
    }
};