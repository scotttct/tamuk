//**************Aerobic Activity Log Constructor */

log = new Log('Ride into the wind', 412, 'JoeSmo', '8:12am', '53min','8 RPE', 'Felt great, but hard riding into the wind');
console.log(log)

function Log( title, activityType, user, time, duration, comments) {
    this.title = title;
    this.activityType = activityType;
    this.author = user;
    this.time = time;
    this.duration = duration;
    this.intensity = intensity;
    this.felt = 5;
    this.comments = comments;
    
}