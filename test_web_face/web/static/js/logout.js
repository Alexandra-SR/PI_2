function logout(){
    $.getJSON('/logout', function(data){
      console.log("Logged Out!");
      alert("Your current session has ended");
      window.location = '/static/html/login.html';
    });
  
  }