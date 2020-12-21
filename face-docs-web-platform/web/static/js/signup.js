function signup(){
  var name = $('#name').val(); //getting name by ID w/ jquery
  var lastname = $('#lastname').val(); //getting lastname by ID w/ jquery
  var username = $('#username').val(); //getting username by ID w/ jquery
  //var password = $('#password').val(); //getting password by ID w/ jquery
  //var studentID = $('#studentID').val(); //getting studentID by ID w/ jquery

  //console.log("DATA>",username, password);
  var credentials = {'name': name, 'lastname': lastname, 'username': username};
  $.ajax({
    url: '/signup',
    type: 'post',
    dataType: 'json',
    contentType: 'application/json',
    statusCode:{
      401: function(data){
        console.log("Username already exists");
        //alert("There's already an account with the same username!\nTry a new one");
        //window.location = '/static/html/signup.html';
        $("#after").empty();
        var div = '<div class="alert alert-danger" role="alert"><a class="alert-link">¡El usuario ya existe!</a> Inténtelo con otro usuario.</div>';
        $("#after").append(div);


    }
  },
    success: function(data){
      $("#after").empty();
      console.log("Account created!");
      //alert("You have successfully created an account!");
      //window.location = '/static/html/login.html';
      var div = '<div class="alert alert-success" role="alert">¡Genial! <a class="alert-link">Tu cuenta ha sido creada.</a></div>';
      $("#after").append(div);
      window.setTimeout(function(){window.location = '/static/html/login.html';}, 3000);

    },
    data: JSON.stringify(credentials)
  });
}