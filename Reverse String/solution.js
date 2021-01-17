/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */

/*
Diagram:

Edge case: If array length is less or equal to 1, return the array
Start with two pointer, one point at the first element, one point to the last element.
switch the element with two pointer

Input: ["h","e","l","l","o"]

         |               |
Input: ["h","e","l","l","o"]

         |               |
Input: ["o","e","l","l","h"]

             |       |
Input: ["o","e","l","l","h"]

             |       |
Input: ["o","l","l","e","h"]

                 |
Input: ["o","l","l","e","h"]

return
*/
var reverseString = function(s) {
    //If array length is less or equal to 1, return the array
    if (s.length <=1) {
        return s
    }

    let j = s.length - 1;


    for(let i = 0; i< j; i++) {
        let temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        j--;
    }
};
