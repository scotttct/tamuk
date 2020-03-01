
// const numbers = [ 3, 4];

// //Add to End
// numbers.push( 5, 6);

// //Add to Beginning
// numbers.unshift(1, 3);

// //Add to Middle of an Array:  First number is the beginning, next number is how many to delete, then the parameters to add as 'a' and 'b'
// numbers.splice(2, 0, 'a', 'b')
// console.log(numbers);
// //*******************Finding Elements in Primitives */

// const numbers = [1, 2, 3, 1, 4];

// console.log(numbers.indexOf('a'));//because it does not exist it results in -1

// console.log(numbers.indexOf(1)); //will produce the index of 1

// console.log(numbers.lastIndexOf(1)); //will produce the index of the 1 where it last occurs

// console.log(numbers.indexOf(1) !== -1);  //This checks to see if an element exists within an array, 

// console.log(numbers.includes(1)); //This is the new way of checking to see if an element exists in an array! VERY Important! *****
//Finding Reference Types************************/

//This method could be useful in finding developing a search for courses by ID or by Name...***Important!!!!
// const courses = [
//     { id: 1, name: 'a'},
//     { id: 2, name: 'b'},

// ];
// const course = courses.find(course => course.id === 1);

// console.log(course);

//testing the elements of an Array**********
//Every checks to see if all the elements in an array matches the criteria

// const numbers = [1, 2, 3];

// const allPostive = numbers.every(function(value) {
//     return value >= 0;
// });

// console.log(allPostive);
 //some checks to see if at least 1 elements in an array matches the criteria

//  const numbers = [1, -1, 2, 3];

//  const atLeastOnePositive = numbers.some(function(value) {
//      return value >= 0;
//  });
 
//  console.log(atLeastOnePositive);


//Filter an Array

// const number = [1, -1, 2, 3];

// const filtered = number.filter(n => n >= 0);

// console.log(filtered);

//Map function
// const number = [1, -1, 2, 3];

// const filtered = number.filter(n => n >= 0);

// const items = filtered.map(n => '<li>' + n + '</li>');

// const html = '<ul>' + items.join(' ') + '</ul>';

// console.log(html);

//Both filter and map return a new array, and are chainable..one after another *****/

// const numbers = [1, -1, 2, 3];

// const items = numbers
//     .filter(n => n >= 0)
//     .map(n => ({ value: n }))
//     //we can then filter and map again over and over like:
//     .filter(obj => obj.value > 1)
//     .map(obj => obj.value);

// console.log(items)

// const numbers = [1, -1, 2, 3];

// let sum = 0;
// for (let n of numbers)
//     sum += n;

//reduce function sums an array of numbers// 

// const sum = numbers.reduce((accumulator, currentValue) => {
//     return accumulator + currentValue;
// }, 0);

//***Reduce the function down by simplifying code like:***** */

// const sum = numbers.reduce(
//     (accumulator, currentValue) => accumulator + currentValue
// );

// console.log(sum);
//******************************* */

//Array from Range

// const numbers = arrayFromRange(1, 4);

// console.log(numbers);

// function arrayFromRange(min, max) {
//     const output = [];
//     for (let i = min; i <= max; i++)
//     output.push(i);
// return output;
// }

//Includes exercise

// const numbers = [1, 2, 3, 4];
// let includedNumber = 5;
// console.log(numbers.includes(includedNumber));

// function includes(array, searchElement) {
//     for (let element of array)
//         if (element === searchElement)
//             return true;
//     return false;


//Except Function ***************/

// const numbers = [1, 2, 3, 4];

// const output = except(numbers, [1]);

// console.log(output);

// function except(array, excluded) {
//     const output = [];
//     for (let element of array)
//         if(!excluded.includes(element))
//             output.push(element);
//     return output;
// }

// ***Moving an Element in an Array***/

const numbers = [1, 2, 3, 4];

const output = move(numbers, 0, 1);

console.log(output);

function move(array, index, offset) {
    const position = index + offset;
    if (position >= array.length || position < 0) {
        console.error('invalid offset.');
        return;
    }

    const output = [...array];
    const element = output.splice(index, 1)[0];
    output.splice(index + offset, 0, element);
    return output;
}