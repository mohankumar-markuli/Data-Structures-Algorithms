/*

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

*/

function nQueens(n, board, row) {

    if (row === n) {
        console.log(board);
        return true; // solution found
    }

    // place queen in a row
    for (let col = 0; col < n; col++) {
        if (isSafe(board, row, col)) {
            board[row][col] = 'Q'; // place queen

            const result = nQueens(n, board, row + 1); // move to next row

            if (result) return true; // solution found

            board[row][col] = '.'; // backtrack
        }

    }
}

function isSafe(board, row, col) {
    // check column
    let r = row;
    let c = col;

    while (r--) {
        if (board[r][c] === 'Q') return false;
    }

    r = row;
    while (r-- && c--) {
        if (board[r][c] === 'Q') return false;
    }

    r = row;
    c = col;
    while (r-- && c++ < board.length) {
        if (board[r][c] === 'Q') return false;
    }

    return true; // safe to place queen
}

var solveNQueens = function (n) {
    const board = Array(n);
    for (let i = 0; i < n; i++) {
        board[i] = Array(n).fill('.'); // initialize the board with '.'
    }

    nQueens(n, board, 0);
}

solveNQueens(4);