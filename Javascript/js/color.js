//falsy and truthy examples

// let userColor = 'red';
// let defaultColor = 'blue';
// let currentColor = userColor || defaultColor;

// console.log(currentColor);


// const readPermission = 4;
// const writePermission = 2;
// const executePermission = 1;

// let myPermission = 0;
// myPermission = myPermission | readPermission | writePermission;

// let message = 
//     (myPermission & readPermission) ? 'yes you have permission! Go Go Go!' : 'no you do not have permission...Stop!';

// console.log(message);

// let a = 'red';
// let b = 'blue';

// let c = '';

// c = a;
// a = b;
// b = c;



// console.log(a);
// console.log(b);

let hour = 13;

if (hour >= 6 && hour < 12) 
    console.log('Good Morning!');
else if (hour >=12 && hour < 18)
    console.log('Good Afternoon');
else 
    console.log('Good Evening');

