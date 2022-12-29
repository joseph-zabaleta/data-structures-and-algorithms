'use strict';

const arrayReverse = require('./arrayReverse');

describe('Javascript: Reverse an Array Tests: ', () => {

  test('Should return an array with the elements in reversed order without using any built-in methods available to JavaScript.', () => {

    const input = [1, 2, 3, 4, 5, 6];
    const actual = arrayReverse(input);
    const expected = input.reverse();

    expect(actual).toStrictEqual(expected);
  });

  test('Should be able to handle an array of positive and negative numbers.', () => {

    let input = [89, 2354, 3546, 23, 10, -923, 823, -12];
    let actual = arrayReverse(input);
    let expected = input.reverse();

    expect(actual).toStrictEqual(expected);

    input = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199];
    actual = arrayReverse(input);
    expected = input.reverse();

    expect(actual).toStrictEqual(expected);
  });

  test('Should be able to handle an array of objects or strings.', () => {

    const input = [{ name: 'bob', house: 'white', }, { name: 'tim', house: 'blue', }];
    const actual = arrayReverse(input);
    const expected = input.reverse();

    expect(actual).toStrictEqual(expected);
  });

  test('Should be able to handle an empty array', () => {
    expect(arrayReverse([])).toStrictEqual([]);
  });

});