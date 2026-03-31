/*
    given an array of numbers
    return the count of numbers strictly less then zero.
*/

const input = [-1, 0, -8, 5];
// output: 2


function countNegatives(arr) {
  // implement your solution here

  if (!Array.isArray(arr)) return false;    //validate input type

  let count = 0;
  if (arr.length == 0) return 0;    // end point case

  for (let i = 0; i < arr.length; i++) {
    const value = arr[i];

    // validate data
    if (typeof value !== 'number' || !Number.isFinite(value)) return false; 
    if (value < 0) count++;
  }
  return count;
}

console.log(countNegatives(input));