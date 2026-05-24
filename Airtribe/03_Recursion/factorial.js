function factorial(n) {
    if (n == 0) return 1;

    const prev = factorial(n - 1);
    const cur = n * prev;
    return cur;
}

console.log(factorial(5));