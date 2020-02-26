//loops
//for loops
// for (InitialExpression; condition; incrementExpression) {
//     Expresion
// }

// for (let i = 0; i > 5; i++) {
//     if (i % 2 !== 0) console.log(i);
// }

//while loops
// let i = 0;
// while (i <= 5) {
//     if (i % 2 !== 0 ) console.log(i);
//     i++;
// }

//Do while not often used...
// let i = 0;
// do {
//     if (i % 2 !== 0 ) console.log(i);
//     i++;  
// } while (i <= 5);


//infinite loop runs forever.
// let i = 0;
// while (1 < 5) {
//     console.log(i);
//     i++; // without the i++ will be an infiinity loop
// }

//************* */
//For IN loop

// const person = {
//     name: 'mosh',
//     age: 30
// };

// for (let key in person)
// console.log(key, person[key]);


//for of loops

// const colors = ['red', 'green', 'blue'];

// for (let color of colors)
//     console.log(color);


//************** */
//Break and continue...
// let i = 0;
// while (i <= 10) {
//     // if (i === 5) break;
//     if (i % 2 === 0) {
//         i++;
//         continue;
//     }
//     console.log(i);//continue will not be used too often in es6
//     i++;
// }

//example for is true or false
// let photo = isLandscape(100, 200)
// console.log('The photo is in landscape: ', photo)
// function isLandscape( width, height) {
//    return (width > height) ? true : false;

// }

// console.log('The photo is in landscape: ', isLandscape(100, 200)) //removed the variable photo and just called the function...
// function isLandscape( width, height) {
//    return (width > height); //removed the explicit statement from the code above to clean up the code

// }

//************************** */

//fizBuzz assignment

//Divisible by 3 => Fiz
//Divisible by 5 => Buzz
//Devisible by 3 && 5 => FizzBuzz
//Not divisible by 3 or 5 => input
//Not a number NaN => 'Not a number'

// 

//*********** */

//Speed Limit program example

// checkSpeed(130);

// function checkSpeed(speed) {
//    const speedLimit = 70;
//    const kmPerPoint = 5;

//    if (speed < speedLimit + kmPerPoint)
//       console.log('OK');
//    else {
//       const points = Math.floor((speed - speedLimit) / kmPerPoint);
//       if (points >= 12)
//          console.log('Licence suspended');
//       else
//          console.log('Points', points)
//    }
// }

//************************ */

//odd and even numbers to 10

// showNumbers(10);

// function showNumbers(limit) {
//    for (let i = 0; i <= limit; i++) {
//       const message = (i % 2 === 0) ? 'Even' : 'Odd'
//       console.log(i, message);
//    }
  
// }

//*********************** */

//count the number of truthy statements

// const array = [0, null, undefined, 1, 2, 3, '', 5];

// console.log("The number of truthy values in the array is: ", countTruthy(array));

// function countTruthy(array) {
//    let count = 0;
//    for (let value of array)
//       if(value)
//          count++;
//    return count;
// }

//************************ */

//disply only string properties in an Object

// const movie = {
//    title: 'a',
//    releaseYear: 2018,
//    rating: 4.5,
//    director: 'b'
// };

// showProperties(movie);

// function showProperties(obj) {
//    for (let key in obj)
//       if (typeof obj[key] === 'string')
//          console.log(key, obj[key]);
// }

//************************ */

//sum number that are multiples of 3 or 5

// console.log(sum(10));

// function sum(limit) {
//    let sum = 0;

//    for (let i = 0; i <= limit; i++)
//       if (i % 3 ===0 || i % 5 === 0)
//          sum += i;

//    return sum;
// }

//********************* */

//Grade students

// const marks = [ 80, 80, 90];

// //Average = 70

// //1-59: F
// //60-69: D
// //70-79: C
// //80-89: B
// //90-100: A

// console.log(calculateGrade(marks));

// function calculateGrade(marks) {
//    const aveage = calculateAverage(marks);
//    if (aveage < 60) return 'F';
//    if (aveage < 70) return 'D';
//    if (aveage < 80) return 'C';
//    if (aveage < 90) return 'B';
//    return 'A';
// }

// function calculateAverage(array) {
//    let sum = 0;
//    for (let value of array)
//       sum +=value;
//    return sum / array.length;
// }

//****************************** */

//show stars example

// showStars(5);

// function showStars(rows) {
//    for (let row = 1; row <= rows; row++) {
//       let pattern = '';
//       for (let i = 0; i < row; i++)
//          pattern += '*';
//       console.log(pattern);
//    }
// }
//************************ */
//Show only Prime Numbers Example

showPrimes(20)

function showPrimes(limit) {
   for (let number = 2; number <= limit; number++) 
      if (isPrime(number)) console.log(number);

 
//isPrime checks to see if a number is prime or not
}
function isPrime(number) {

   for (let factor = 2; factor < number; factor++)
      if (number % factor ===0) 
         return false;
   return true;
}
