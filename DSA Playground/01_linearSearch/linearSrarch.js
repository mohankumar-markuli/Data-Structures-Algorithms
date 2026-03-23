const linearSearch = (arr, target) => {
    const n = arr.length;

    for (let i = 0; i < n; i++) {
        if (arr[i] === target) {
            return i;
        }
    }
    return -1;
}

const collection = ["mohan", 3, 4, 5, "abd", "markuli"];
const searchElement = "abd";
const elementIndex = linearSearch(collection, searchElement);

console.log(elementIndex);