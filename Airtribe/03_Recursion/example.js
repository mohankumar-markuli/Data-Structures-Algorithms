function printNtoOne(n) {
    if (n < 1) return;
    console.log(n);
    printNtoOne(n - 1);

    console.log("going back from  ", n);
}

printNtoOne(5);