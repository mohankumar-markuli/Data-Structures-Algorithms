/* Problem :
Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? (important)
 */


const twoSum = function (arr, target) {
    const output = new Array;
    let s = 0
    let e = arr.length - 1;

    while (s < e) {
        const sum = arr[s] + arr[e];
        if (sum == target) {
            console.log(s,e)
            output.push(s,e);
        }
        if (sum > target) e--;
        else s++;
    }
    return output;
}

const collection  = [1, 2, 3, 5, 8, 13, 21];
const example1 = [2,7,11,15]

const example2 = [3,2,4]// failed as the array is not sorted
// two pointer approch works only for the sorted array with decreasing range on processing

const example3 = [3,3]

const result = twoSum(example2, 6);
console.log(result);