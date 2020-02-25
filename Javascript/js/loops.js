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

checkSpeed(130);

function checkSpeed(speed) {
   const speedLimit = 70;
   const kmPerPoint = 5;

   if (speed < speedLimit + kmPerPoint)
      console.log('OK');
   else {
      const points = Math.floor((speed - speedLimit) / kmPerPoint);
      if (points >= 12)
         console.log('Licence suspended');
      else
         console.log('Points', points)
   }
}
