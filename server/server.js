

const express = require('express');
const app = express();


var server = app.listen(5000, () => {
  console.log('listening on *:5000');
});


var io = require('socket.io')(server,{ /*pingInterval: 500,*/ origins: '*:*'});


app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});



io.on('connection', function(socket){

  console.log('user connect');
  socket.emit('data', 'usuario conectados con exito');

  socket.on('disconnect', function(){

      console.log('user desconect');
  });

  socket.on('mensaje', function(mensaje){
      console.log('mensaje: ' + mensaje);
  });

});





