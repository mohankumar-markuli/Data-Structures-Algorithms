function bubbleSort(arr) {
    const n = arr.length


    for(let iteration=0; iteration<n-1;iteration++){
    let madeSwap = false;
        for(let i=0;i<n;i++){

            if(i+1 < n && arr[i]>arr[i+1]){

                madeSwap = true;
                let temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            }
        }
        if(!madeSwap) break;
        console.log({iteration,arr})
    }
    return arr
}

const arr = [5, 4, 2, 1, 3];
const result = bubbleSort(arr);
console.log(result)
