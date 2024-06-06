// Remove the signature declaration
function skillsMember() {
    var member = {
        name: 'John Doe',
        age: 30,
        skills: ['JavaScript', 'React', 'Node'],
        // signature: function() {
        //     console.log(`${this.name} has ${this.skills.length} skills`);
        // }
    };

    return member;
}