function runTestTakePicture(){
    console.log("Running Test");
    //var credentials = {'username':username, 'password':password};
    $.ajax({
        url:'/testSignUp',
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

