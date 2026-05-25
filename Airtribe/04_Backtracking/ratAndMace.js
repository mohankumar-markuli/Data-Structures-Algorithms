const board = [
    [0, 1, 0],
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
];

function ratAndMace(row, col, n, m, board, path) {

    if (row === n || col === m) return;
    if (board[row][col] === 1) return; // mark as visited

    if (row === n - 1 && col === m - 1) {
        console.log(path);
        return;
    }

    // down
    ratAndMace(row + 1, col, n, m, board, path + 'D');

    // right
    ratAndMace(row, col + 1, n, m, board, path + 'R');

}

ratAndMace(0, 0, board.length, board[0].length, board, '');