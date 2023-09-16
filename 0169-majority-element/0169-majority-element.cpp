class Solution {
public:
    int majorityElement(vector<int>& A) {
        int count = 1;
        int majority_element = A[0];
        for (int i = 1 ; i < A.size(); i++){
            if (count == 0){
                majority_element = A[i];
                count++;
            } else if (A[i] == majority_element){
                count++;
            } else {
                count--;
            }
        }
        return majority_element;
    }
};



