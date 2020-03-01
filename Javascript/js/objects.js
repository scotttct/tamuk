//factory function
// function createCircle(radius) {
//     return {
//         radius,
//         draw() {
//             console.log('draw');
//         }
//     };
// }

// const circle1 = createCircle(1);
// console.log(circle1);
//****************************** */
//

//Constructor Function for creating objects - Use Pascal Notation

// function Circle(radius) {
//     this.radius = radius;
//     this.draw= function() {
//         console.log('draw');
//     }
// }

// const circle = new Circle(1);

// console.log(Math.SQRT2)

//create an address object, showAddress(address)
//street
//city
//zipCode

   
// function showAddress(address) {
//   for (let key in address)
//     console.log(key, address[key]);
// }

// showAddress(address);

//factory Function**********
// let address = createAddress("1666 Starling Drive","Sarasota","34231");

// console.log(address) 

// function createAddress(street, city, zipCode) {
//     return {
//         street,
//         city,
//         zipCode
//     };
// }

//***********Constructor Function************* */
// let address1 = new Address("1666 Starling Drive","Sarasota","34231");
// let address2 = new Address("1666 Starling Drive","Sarasota","34231");
// let address3 = address1;
// console.log('Are both addresses 1 and 2 equal?', areEqual(address1,address2));
// console.log('Are both addresses 1 and 2 the same?',areSame(address1,address2));
// console.log('Are both addresses 1 and 3 the same?',areSame(address1,address3));

// function Address(street, city, zipCode) {
//     this.street = street;
//     this.city = city;
//     this.zipCode = zipCode;
// }

// function areEqual(address1, address2) {
//     return address1.street === address2.street &&
//         address1.city === address2.city && 
//         address1.zipCode === address2.zipCode;
// }
// function areSame(address1, address2) {
//     return address1 === address2;
// }

//**********Blog Post Exercise */
//title
//body
//author
//views
//comments
// (author, body)
//isLive

//Blog Post constructor****************

post = new Post('a', 'b', 'c');
console.log(post)

function Post( title, body, author ) {
    this.title = title;
    this.body = body;
    this.author = author;
    this.views = 0;
    this.comment = [];
    this.isLive = false;
}

// This is how to use it as an object

// let post = {
//     title: 'a',
//     body: 'b',
//     author: 'c',
//     views: 10,
//     comment: [
//         { author: 'a', body: 'b' },
//         { author: 'c', body: 'd' },
//     ],
//     isTrue: true
// };
// console.log(post);
//********************************************************* */
//**************Aerobic Activity Log Constructor */

// log = new Log('Ride into the wind', 412, 'JoeSmo', '8:12am', '53min','8 RPE', 'Felt great, but hard riding into the wind');
// console.log(log)

// function Log( title, activityType, user, time, duration, comments) {
//     this.title = title;
//     this.activityType = activityType;
//     this.author = user;
//     this.time = time;
//     this.duration = duration;
//     this.intensity = intensity;
//     this.felt = 5;
//     this.comments = comments;
    
// }
//*************************************************************** */
//price tag exercise....
let priceRange = [
    {label: '$', tooltip: 'Inexpensive', minPerPerson: 0, maxPerPerson: 10},
    {label: '$', tooltip: 'Inexpensive', minPerPerson: 0, maxPerPerson: 10},
    {label: '$', tooltip: 'Inexpensive', minPerPerson: 0, maxPerPerson: 10},
];

//filter by min and max using:
let restaurant = [ 
    { averagePerPerson = 5 }
]