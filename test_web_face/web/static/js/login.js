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
            },
            301: function(data){
                console.log("Failed to match");
            } 
          },
        success: function(data){
            console.log("User  test!");
            alert(data['msg']);
            window.setTimeout(function(){window.location = '/static/html/docs.html';}, 2000);

        },
        data: JSON.stringify(credentials)
    });
}

