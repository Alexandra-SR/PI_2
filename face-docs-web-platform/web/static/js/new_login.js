function putView(){
    $("#all_web").empty();
    template = "<div class=\'container\' id=\'container\'>	<div class=\'form-container sign-up-container\'>";
    template += "<!--Crear un nuevo usuario--> <h1>Crear Cuenta</h1>";
    template += "<div class=\'social-container\'></div><span></span>";
    template += "<input id=\'usernameCreate\' type=\'text\' placeholder=\'Usuario\' />";
    template += "<input id=\'nameCreate\' type=\'text\' placeholder=\'Nombre\' />";
    template += "<input id=\'lastnameCreate\' type=\'text\' placeholder=\'Apellido\' />";
    template += "<button id=\'PostUserButton\' onclick='button_press_Create();'>Crear Cuenta</button>";
    template += "<!--Crear un nuevo usuario-->";
    template += "</div> <div class=\'form-container sign-in-container\'>";
    template += "<!--Login del usuario--><form><img src=\'/static/images/small_logo.PNG\' alt=''><div class=\'social-container\'></div><span></span>";
    template += "<input id=\'usernameLogin\' type=\'username\' placeholder=\'Usuario\' />";
    template += "<button id=\'LoginButton\' onclick='button_press_Login();'>Iniciar Sesión</button></form><!--Login del usuario--></div>";
    template += "<div class=\'overlay-container\'><div class=\'overlay\'><div class=\'overlay-panel overlay-left\'><h1>¡Bienvenido de Vuelta!</h1><p>Para ingresar y ver todas las novedades regístrese usando su cuenta</p><button class=\'ghost\' id=\'signIn\'>Iniciar Sesión</button>";
    template += "</div><div class=\'overlay-panel overlay-right\'><h1>¿No Está Registrado?</h1><p>Cree una cuenta para empezar a acceder a documentos de forma segura</p>";
    template += "<button class=\'ghost\' id=\'signUp\'>Crear Cuenta</button></div></div></div></div>";
    $("#all_web").append(template);
}


const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');


signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});



document.getElementById("PostUserButton").disabled = false;
document.getElementById("LoginButton").disabled = false;


$("#usernameCreate, #nameCreate, #lastnameCreate").on(function(){
    if($("#usernameCreate").val() != "" && $("#nameCreate").val() != "" && $("#lastnameCreate").val() != ""){
      document.getElementById("PostUserButton").disabled = false;
    }
});

$("#usernameLogin" ).on(function(){
    if($("#usernameLogin").val() != "" ){
      document.getElementById("LoginButton").disabled = false;
    }
});

//Crear un nuevo usuario
function button_press_Create(){
  var username = $("#usernameCreate").val();
  var name = $("#nameCreate").val();
  var lastname = $("#lastnameCreate").val();


  var complete_user = JSON.stringify(
    {
      "username" : username,
      "name" : name,
      "lastname" : lastname
    }
  );

  $.ajax({
    url: '/signup',
    type: 'POST',
    contentType: 'application/json',
    data: complete_user,
    dataType: 'json',
  });
}

//Logear a un usuario existente
function button_press_Login(){
  var username = $("#usernameLogin").val();

  var complete_login = JSON.stringify(
    {
      "username" : username
    }
  );

  $.ajax({
    url: '/login',
    type: 'post',
    contentType: 'application/json',
    data: complete_login,
    dataType:'json',
    success: function(data){
        console.log("User  test!");
        $("#after").empty();
        window.setTimeout(function(){window.location = '/static/html/options.html';}, 2000);
        var div = '<div class="alert alert-success" role="alert">Great! <a class="alert-link">You\'re logged in.</a></div>';
        $("#after").append(div);
        },
  });
}
