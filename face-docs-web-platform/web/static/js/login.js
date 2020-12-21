function login() {
  var username = $("#username").val();
  var credentials = { username: username };
  $.ajax({
    url: "/login",
    type: "post",
    dataType: "json",
    contentType: "application/json",
    statusCode: {
      401: function (data) {
        console.log("User was not found!");
        $("#after").empty();
        var div =
          '<div class="alert alert-danger" role="alert"><a class="alert-link">Usuario no encontrado.</a> Regístrese primero.</div>';
        $("#after").append(div);
      },
      301: function (data) {
        console.log("Failed to match");
        $("#after").empty();
        var div =
          '<div class="alert alert-danger" role="alert"><a class="alert-link">¡Error en la validación!</a> Inténtalo de nuevo.</div>';
        $("#after").append(div);
      },
    },
    success: function (data) {
      console.log("User  test!");
      //alert(data['msg']);
      $("#after").empty();
      window.setTimeout(function () {
        window.location = "/static/html/options.html";
      }, 2000);
      var div =
        '<div class="alert alert-success" role="alert">¡Genial! <a class="alert-link">Has ingresado.</a></div>';
      $("#after").append(div);
    },
    data: JSON.stringify(credentials),
  });
}
