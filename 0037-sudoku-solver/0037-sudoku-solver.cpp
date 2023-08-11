class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        solve(board);
    }
    
    bool isValid(int r, int c, char ch, vector<vector<char>>& b) {
        for(int i = 0; i < 9; i++) {
            if(b[i][c] == ch)
                return false;
            if(b[r][i] == ch)
                return false;
            
            if(b[3 * (r/3) + i/3][3 * (c/3) + i%3] == ch)
                return false;
        }
        
        return true;
    }
    
    bool solve(vector<vector<char>>& b) {
        for(int i = 0; i < b.size(); i++) {
            for(int j = 0; j < b[0].size(); j++) {
                if(b[i][j] == '.'){
                    for(char c = '1'; c <= '9'; c++){
                        if(isValid(i, j, c, b)){
                            b[i][j] = c;
                            if(solve(b) == true){
                                return true;
                            } else {
                                b[i][j] = '.';
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
};