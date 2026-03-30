/*

The Fibonacci Series is a series of numbers
where each number is sum of the two preceding ones.
It starts with 0 and 1

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n>1

*/

// Method 1 = using iteration 

function generateFibonacci(n) {
    const outputArray = []
    if (n === 0) return outputArray;
    if (n === 1) outputArray.push(0);
    else {
        outputArray.push(0,1);
        for(let i=2;i<n;i++){
            const result = outputArray[i-1] + outputArray[i-2];
            outputArray.push(result);
        }
    }
    return outputArray;
}

const result = generateFibonacci(1);
console.log(result);

// method 2 - using resursivefunction
