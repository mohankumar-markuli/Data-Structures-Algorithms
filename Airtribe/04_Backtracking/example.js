function numberOnetoN(n) {
    if (n === 0) return;
    // console.log(n);
    numberOnetoN(n - 1);

    // Backtracking step
    console.log(n);
}

numberOnetoN(5);
