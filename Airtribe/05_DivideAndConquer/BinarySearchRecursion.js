function binarySearchRec(arr, key, s, e) {
    const mid = Math.floor((s + e) / 2);

    if (s > e) return -1;

    if (arr[mid] === key) return mid;
    if (key < arr[mid]) return binarySearchRec(arr, key, s, mid - 1);
    return binarySearchRec(arr, key, mid + 1, e);
}

const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const key = 2;
console.log(binarySearchRec(arr, key, 0, arr.length - 1));