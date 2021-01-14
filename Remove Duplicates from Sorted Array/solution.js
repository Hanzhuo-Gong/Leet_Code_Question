/**
 * @param {number[]} nums
 * @return {number}
 */



/*
Diagram:

Step:

               |
Input: nums = [1,1,2]
               |
Input: nums = [1,1,2]
temp = 1
                 |
Input: nums = [1,1,2]
temp = 1 === 1 //remove the number

                 |
Input: nums = [1,2]
temp = 1 !== 2 //update the temp number to 2, so temp = 2

//When reach to the end, return the newNums


*/
var removeDuplicates = function(nums) {
    //if the array is empty
    if (nums.length === 0) {
        return [];
    }

    //if the array size is 1
    if (nums.length === 1) {
        return nums;
    }

    let temp = nums[0];
    let i = 1;
    while (i < nums.length) {
        //if the element is the same, remove the element
        if (nums[i] === temp) {
            nums.splice(i,1);
            //console.log(nums[i])
        }
        else {
            temp = nums[i];
            i++;
        }
    }
    /*
    for (let i = 1; i < nums.length; i++) {

    }*/

    /*
    //if the array is empty
    if (nums.length === 0) {
        return 0
    }
    //Sort the array, so the array appears in order
    nums.sort();
    let result = [];

    //append the first element to the set
    let temp = nums[0];
    result.push(temp);


    //Loop over the array
    for(let i = 1; i < nums.length; i++) {
        //if number is the same, do nothing
        if(nums[i] === temp) {
            continue;
        }
        else {
            temp = nums[i];
            result.push(temp);
        }
    }
    //console.log(result);
    return result;
    */
};
