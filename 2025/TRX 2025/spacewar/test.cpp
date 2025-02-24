#include <iostream>
#include <vector>
#include <bitset>

bool askInput(std::vector<std::vector<int>>& battlefield) {
    int row, column, troops;
    
    std::cout << "Caesar, the legions await your command. Specify the sector where our forces should deploy.\n";
    std::cout << "Row [1-25] (-1 to check win): ";
    std::cin >> row;
    if (row == -1) return false;
    
    std::cout << "Column [1-25]: ";
    std::cin >> column;
    
    std::cout << "Troops [1-25]: ";
    std::cin >> troops;
    
    if (row > 0 && row <= 25 && column > 0 && column <= 25) {
        if (troops > 0 && troops <= 25) {
            if (battlefield[row - 1][column - 1] != 0) {
                std::cout << "The battlefield is overrun with alien forces, Dominus. There's no room for additional troops.\n";
                return false;
            } else {
                battlefield[row - 1][column - 1] = troops;
                return true;
            }
        } else {
            std::cout << "Your decision to deploy all our troops was a trap. The aliens detonated a bomb, and our legions were obliterated.\n";
            return true;
        }
    } else {
        std::cout << "You attempted to reinforce Saturn, but its fragile alliance with Mars has shattered. Our forces were annihilated.\n";
        return true;
    }
}
bool checkWin(const std::vector<std::vector<int>>& board) {
    for (const auto& row : board) {
        for (const auto& cell : row) {
            if (cell == 0) {
                return false;
            }
        }
    }
    return isValid(board);
}
bool isValid(const std::vector<std::vector<int>>& board) {
    int size = 25;
    
    for (int i = 0; i < size; ++i) {
        std::bitset<26> rowCheck, colCheck;
        for (int j = 0; j < size; ++j) {
            if (board[i][j] > 0) {
                if (rowCheck[board[i][j]]) return false;
                rowCheck.set(board[i][j]);
            }
            if (board[j][i] > 0) {
                if (colCheck[board[j][i]]) return false;
                colCheck.set(board[j][i]);
            }
        }
    }
    
    for (int k = 0; k < size; k += 5) {
        for (int m = 0; m < size; m += 5) {
            std::bitset<26> boxCheck;
            for (int n = 0; n < 5; ++n) {
                for (int ii = 0; ii < 5; ++ii) {
                    int value = board[k + n][m + ii];
                    if (value > 0) {
                        if (boxCheck[value]) return false;
                        boxCheck.set(value);
                    }
                }
            }
        }
    }
    return true;
}
void play(std::vector<std::vector<int>>& board) {
    while (true) {
        if (!isValid(board)) {
            std::cout << "A miscalculation, Darius. The aliens exploit our weaknesses." << std::endl;
            return;
        }

        if (!askInput(board)) break;
    }
    if (checkWin(board)){
        std::cout << "Victory is ours, Caesar! The aliens have been vanquished." << std::endl;
    }
    else{
        std::cout << "A miscalculation, Darius. The aliens exploit our weaknesses." << std::endl;
    }
}