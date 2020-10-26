function login(){
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
}

function runTest(){
    console.log("Running Test");
    //var credentials = {'username':username, 'password':password};
    $.ajax({
        url:'/test',
        type: 'post',
        dataType: 'json',
        contentType: 'application/json',
        statusCode:{
            401: function(data){
              console.log("Failed identification!");
            }
          },
        success: function(data){
            console.log("Finished test!");
            alert(data['msg']);

        },
        //data: JSON.stringify(credentials)
    });
}

