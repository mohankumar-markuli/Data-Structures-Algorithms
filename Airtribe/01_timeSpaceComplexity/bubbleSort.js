// Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, 
// compares adjacent elements and swaps them if they are in the wrong order.

// The pass through the list is repeated until the list is sorted. 
// The algorithm gets its name from the way smaller elements "bubble" to the top of the list (beginning) 
// while larger elements sink to the bottom (end).


function bubbleSort(arr) {
    const n = arr.length

    for (let iteration = 0; iteration < n - 1; iteration++) {
        let madeSwap = false;
        for (let i = 0; i < n; i++) {

            if (i + 1 < n && arr[i] > arr[i + 1]) {

                madeSwap = true;
                let temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
            }
        }
        if (!madeSwap) break;
        console.log({ iteration, arr })
    }
    return arr
}

const arr = [5, 4, 2, 1, 3];
const result = bubbleSort(arr);
console.log(result)
