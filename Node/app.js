var express = require('express');
var app = express();
var fs = require("fs");
var link = "10.100.16.120";
app.use(express.static('public'));
app.get('/asia', function (req, res) {
   fs.readFile( __dirname + "/" + "asia.json", 'utf8', function (err, data) {
      console.log( data );
      res.setHeader("Access-Control-Allow-Origin", "http://"+link+":8000");
      res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
      res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
      res.setHeader('Access-Control-Allow-Credentials', true);
      res.end( data );
   });
})
app.get('/africa', function (req, res) {
   fs.readFile( __dirname + "/" + "africa.json", 'utf8', function (err, data) {
      console.log( data );
      res.setHeader("Access-Control-Allow-Origin", "http://localhost:8000");
      res.setHeader("Access-Control-Allow-Origin", "http://"+link+":8000");
      res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
      res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
      res.setHeader('Access-Control-Allow-Credentials', true);
      res.end( data );
   });
})
app.get('/australia', function (req, res) {
   fs.readFile( __dirname + "/" + "australia.json", 'utf8', function (err, data) {
      console.log( data );
      res.setHeader("Access-Control-Allow-Origin", "http://localhost:8000");
      res.setHeader("Access-Control-Allow-Origin", "http://"+link+":8000");
      res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
      res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
      res.setHeader('Access-Control-Allow-Credentials', true);
      res.end( data );
   });
})
app.get('/europe', function (req, res) {
   fs.readFile( __dirname + "/" + "europe.json", 'utf8', function (err, data) {
      console.log( data );
      res.setHeader("Access-Control-Allow-Origin", "http://localhost:8000");
      res.setHeader("Access-Control-Allow-Origin", "http://"+link+":8000");
      res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
      res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
      res.setHeader('Access-Control-Allow-Credentials', true);
      res.end( data );
   });
})
app.get('/north_america', function (req, res) {
   fs.readFile( __dirname + "/" + "northamerica.json", 'utf8', function (err, data) {
      console.log( data );
      res.setHeader("Access-Control-Allow-Origin", "http://"+link+":8000");
      res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
      res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
      res.setHeader('Access-Control-Allow-Credentials', true);
      res.end( data );
   });
})
app.get('/south_america', function (req, res) {
   fs.readFile( __dirname + "/" + "southamerica.json", 'utf8', function (err, data) {
      console.log( data );
      res.setHeader("Access-Control-Allow-Origin", "http://localhost:8000");
      res.setHeader("Access-Control-Allow-Origin", "http://"+link+":8000");
      res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
      res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
      res.setHeader('Access-Control-Allow-Credentials', true);
      res.end( data );
   });
})

var server = app.listen(8888, function () {
   var host = server.address().address
   var port = server.address().port

   console.log("Example app listening at http://%s:%s", host, port)
})

