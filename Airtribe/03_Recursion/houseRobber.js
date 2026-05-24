function maxMoney(i, nums) {
    if (i >= nums.length) return 0;

    const rob = nums[i] + maxMoney(i + 2, nums);
    const notRob = maxMoney(i + 1, nums);

    return Math.max(rob, notRob);
}

var rob = function (nums) {
    return maxMoney(0, nums);
}

console.log(rob([1, 2, 3, 1]));