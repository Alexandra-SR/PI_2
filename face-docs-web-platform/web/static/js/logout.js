function logout(){
    $.getJSON('/logout', function(data){
      console.log("Logged Out!");
      alert("Tu sesión ha culminado");
      window.location = '/static/html/login.html';
    });
  
  }