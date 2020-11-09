/*function login(){
    console.log("Login User");
    var username = $('#username').val();  //getting username by ID
    var password = $('#password').val();  // getting password by id

    var credentials = {'username':username, 'password':password};
    $.post({
        url:'/authenticate',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            console.log("Authenticated!");
            alert(data['msg']);

        },
        data: JSON.stringify(credentials)
    });
}*/

function login(){
    var username = $('#username').val();
    var credentials = {'username':username};
    $.ajax({
        url:'/login',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        statusCode:{
            401: function(data){
              console.log("User was not found!");
              $("#after").empty();
                var div = '<div class="alert alert-danger" role="alert"><a class="alert-link">Username was not found.</a> Sign up first.</div>';
                $("#after").append(div);
            },
            301: function(data){
                console.log("Failed to match");
                $("#after").empty();
                var div = '<div class="alert alert-danger" role="alert"><a class="alert-link">Failed to math!</a> Try again.</div>';
                $("#after").append(div);
            } 
          },
        success: function(data){
            console.log("User  test!");
            //alert(data['msg']);
            $("#after").empty();
            window.setTimeout(function(){window.location = '/static/html/docs.html';}, 2000);
            var div = '<div class="alert alert-success" role="alert">Great! <a class="alert-link">You\'re logged in.</a></div>';
            $("#after").append(div);

        },
        data: JSON.stringify(credentials)
    });
}

