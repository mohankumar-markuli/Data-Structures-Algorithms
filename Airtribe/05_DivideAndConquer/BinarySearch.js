const a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const key = 15;

function binarySearch(arr, key) {
    let s = 0;
    let e = arr.length - 1;

    while (s <= e) {
        let mid = Math.floor((s + e) / 2);

        if (key === arr[mid]) {
            return mid;
        }

        if (key < arr[mid]) {
            e = mid - 1;
        } else {
            s = mid + 1;
        }
    }

    return -1;
}

console.log(binarySearch(a, key));