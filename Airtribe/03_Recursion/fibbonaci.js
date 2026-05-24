function fibbonaci(n) {
    if (n == 0) return 0;
    if (n == 1) return 1;

    const prev = fibbonaci(n - 1);
    const prev2 = fibbonaci(n - 2);

    const cur = pre + pre2;

    return cur;

}

console.log(fibbonaci(10));