'use strict';

/**
 * Reverses elements in a given array without using the built in array.reverse() method.
 * @param { Array } arr - An array of items to be reversed.
 * @returns - A new array with the elements in reverse order. 
 */
let reverseArray = (arr) => {
  let output = [];

  for (let i = (arr.length - 1); i >= 0; i--) {

    output.push(arr[i]);

  };

  return output;
}

module.exports = reverseArray;