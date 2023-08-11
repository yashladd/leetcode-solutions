class Solution {
public:
    vector<vector<string>> ans;
    
    bool isSafe(int row, int col, set<int> &r, set<int> &nd, set<int> &pd) {
        return (r.find(row) != r.end() || nd.find(row-col) != nd.end() || pd.find(row+col) != pd.end());
    }
    
    void solve(int col, vector<string> &board, set<int> &r, set<int> &nd, set<int> &pd){
        if(col >= board.size()){
            ans.push_back(board);
            return;
        }
        for(int row = 0; row < board.size(); row++){
            if(!isSafe(row, col, r, nd, pd)){
                board[row][col] = 'Q';
                r.insert(row);
                nd.insert(row-col);
                pd.insert(row + col);
                solve(col + 1, board, r, nd, pd);
                board[row][col] = '.';
                r.erase(row);
                nd.erase(row-col);
                pd.erase(row+col);
            }
        }
    }
    
    vector<vector<string>> solveNQueens(int n) {
        
        vector<string> board(n);
        string s(n, '.');
        for(int i = 0; i < n; i++)
            board[i]  = s;
        
        set<int> r;
        set<int> nd;
        set<int> pd;
        
        solve(0, board, r, nd, pd);
        
        return ans;
    }
};