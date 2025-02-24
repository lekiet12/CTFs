#include <iostream>
#include <vector>
#include <bitset>

using namespace std;

const int SIZE = 25;
const int SUBGRID = 5;

// Kiểm tra một con số có hợp lệ hay không
bool isValid(vector<vector<int>> &board, int row, int col, int num) {
    bitset<SIZE + 1> rowCheck, colCheck, boxCheck;

    for (int i = 0; i < SIZE; i++) {
        if (board[row][i] == num) return false; // Trùng trong hàng
        if (board[i][col] == num) return false; // Trùng trong cột
    }

    // Kiểm tra trong ô 5x5
    int boxRow = (row / SUBGRID) * SUBGRID;
    int boxCol = (col / SUBGRID) * SUBGRID;

    for (int i = 0; i < SUBGRID; i++) {
        for (int j = 0; j < SUBGRID; j++) {
            if (board[boxRow + i][boxCol + j] == num) return false;
        }
    }
    return true;
}

// Hàm tìm vị trí trống tiếp theo
bool findEmptyCell(vector<vector<int>> &board, int &row, int &col) {
    for (row = 0; row < SIZE; row++) {
        for (col = 0; col < SIZE; col++) {
            if (board[row][col] == 0) return true;
        }
    }
    return false;
}

// Giải Sudoku bằng Backtracking
bool solveSudoku(vector<vector<int>> &board) {
    int row, col;
    if (!findEmptyCell(board, row, col)) return true; // Nếu không còn ô trống, Sudoku đã được giải

    for (int num = 1; num <= SIZE; num++) {
        if (isValid(board, row, col, num)) {
            board[row][col] = num;
            if (solveSudoku(board)) return true;
            board[row][col] = 0; // Quay lui nếu không hợp lệ
        }
    }
    return false;
}

// Hàm in bảng Sudoku
void printBoard(const vector<vector<int>> &board) {
    for (const auto &row : board) {
        for (int num : row) {
            cout << (num == 0 ? "." : to_string(num)) << " ";
        }
        cout << endl;
    }
}

int main() {
    vector<vector<int>> board(SIZE, vector<int>(SIZE, 0)); // Bảng Sudoku 25x25 (chưa có input)

    // TODO: Nhập bảng Sudoku vào đây (hoặc đọc từ file)
    
    if (solveSudoku(board)) {
        cout << "Sudoku đã được giải:\n";
        printBoard(board);
    } else {
        cout << "Không thể giải Sudoku!\n";
    }

    return 0;
}
