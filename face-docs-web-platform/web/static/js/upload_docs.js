function get_current() {
  console.log("Getting the current user");
  $.getJSON("/current", function (data) {
    console.log(data["username"]);
    //var div = '<ui class="contacts" ><li class="btn btn-secondary" role="alert" onclick="whoami(\'first\',\'last\',\'p_ser\')"><div class="d-flex bd-highlight"><div class="img_cont"><img src="/static/images/me.png" class="rounded-circle user_img"><span class="online_icon"></span></div><div class="user_info"><span>name fullname</span><br>@username</div></div></li></ui>';

    //var div = '<div class="btn btn-secondary" role="alert" onclick="whoami(\'first\',\'last\',\'p_ser\')"><span>name fullname</span>';
    //div = div + '<br><span>@<span><span>username</span></div><br>'
    //   div = div.replace("first", data['name']);
    //   div = div.replace("last", data['fullname']);
    //   div = div.replace("p_ser", data['username']);
    //   div = div.replace("fullname", data['fullname'] );
    //   div = div.replace("name", data['name']);
    //   div = div.replace("username", data['username']);

    //$('#me').append(div);
    //get_users(data);
  });
}
function to_who() {
  var user_to = $("#user_to").val();
  $.ajax({
    url: `/to/<${user_to}>`,
    type: "get",
    dataType: "json",
    contentType: "application/json",
    statusCode: {
      401: function (data) {
        console.log("Not authenticated!");
        $("#after").empty();
        var div =
          '<div class="alert alert-danger" role="alert"><a class="alert-link">Error.</a> Inténtalo de nuevo.</div>';
        $("#after").append(div);
        // alert("Wrong credentials! Try again");
        //    window.location = '/static/html/login.html';
      },
      301: function (data) {
        console.log("Username does not exist!");
        $("#after").empty();
        var div =
          '<div class="alert alert-danger" role="alert"><a class="alert-link">¡El usuario seleccionado no exite!</a> Inténtalo de nuevo.</div>';
        $("#after").append(div);
        // alert("Wrong credentials! Try again");
        //    window.location = '/static/html/login.html';
      },
      403: function (data) {
        console.log("Username does not exist!");
        $("#after").empty();
        var div =
          '<div class="alert alert-danger" role="alert"><a class="alert-link">¡No puedes enviarte archivos a ti mismo!</a> Inténtalo de nuevo.</div>';
        $("#after").append(div);
        // alert("Wrong credentials! Try again");
        //    window.location = '/static/html/login.html';
      },
    },
    success: function (data) {
      //   $("#after").empty();
      //   console.log("Authenticated!");
      //   //alert("You have successfully logged in!");
      //   var div = '<div class="alert alert-success" role="alert">Great! <a class="alert-link">You\'re logged in.</a></div>';
      //   $("#after").append(div);
      //   window.setTimeout(function(){window.location = '/static/html/chat.html';}, 2000);
      console.log("Username validated!");
      $("#after").empty();
      var div =
        '<div class="alert alert-success" role="alert"><a class="alert-link">Usuario validado. ¡Archivo enviado!</a></div>';
      $("#after").append(div);
    },

    //data: JSON.stringify(credentials),
  });
  console.log("ACABE TO WHO");
}

function upload() {
  to_who();
  console.log("BIA");
  var form_data = new FormData($("#upload-file")[0]);
  $.ajax({
    type: "POST",
    url: "/uploadajax",
    data: form_data,
    contentType: false,
    cache: false,
    processData: false,
    async: false,
    success: function (data) {
      console.log("Success!");
    },
  });
}

function go_my_docs() {
  window.location = "/static/html/options.html";
}
