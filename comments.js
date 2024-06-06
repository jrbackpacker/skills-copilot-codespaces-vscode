// Create web server
// Create a file called comments.js and put the following code in it:
// comments.js
// Import express module
var express = require('express');
// Import body-parser module
var bodyParser = require('body-parser');
// Create express app
var app = express();
// Use body-parser middleware
app.use(bodyParser.json());
// Create an array of comments
var comments = [
  {username: 'John', body: 'Hello!'},
  {username: 'Mary', body: 'Hi!'}
];
// Create a route for getting comments
app.get('/comments', function(req, res) {
  res.send(comments);
});
// Create a route for posting comments
app.post('/comments', function(req, res) {
  var comment = req.body;
  comments.push(comment);
  res.send(comment);
});
// Start the server
app.listen(3000, function() {
  console.log('Server is running on http://localhost:3000/');
});
// Now, run the server by executing the following command in the terminal:
// $ node comments.js
// You can test the server by sending a GET request to http://localhost:3000/comments in your browser or using a tool like Postman. You should