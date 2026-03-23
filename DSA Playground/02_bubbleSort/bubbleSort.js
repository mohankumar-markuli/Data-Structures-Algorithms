function bubbleSort(arr) {
    const n = arr.length

    for (let itr = 0; itr < n - 1; itr++) {
        let swapflag = false;

        for (let i = 0; i < n; i++) {

            if (i + 1 < n && arr[i] > arr[i + 1]) {

                let temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                swapflag = true;
            }
        }
        if (!swapflag) break;
    }
    return arr;
}

const collection = [64, 34, 25, 12, 22, 11, 90];
const result = bubbleSort(collection);

console.log(result);