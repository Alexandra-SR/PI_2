function get_current(){
    console.log("Getting the current user");
    $.getJSON("/current", function(data){
      console.log(data)
      $('#title').append(`<h2> Welcome ${data}</h2>`);
      /*var div = '<ui class="contacts" ><li class="btn btn-secondary" role="alert" onclick="whoami(\'first\',\'last\',\'p_ser\')"><div class="d-flex bd-highlight"><div class="img_cont"><img src="/static/images/me.png" class="rounded-circle user_img"><span class="online_icon"></span></div><div class="user_info"><span>name fullname</span><br>@username</div></div></li></ui>';
  
      //var div = '<div class="btn btn-secondary" role="alert" onclick="whoami(\'first\',\'last\',\'p_ser\')"><span>name fullname</span>';
      //div = div + '<br><span>@<span><span>username</span></div><br>'
      div = div.replace("first", data['name']);
      div = div.replace("last", data['fullname']);
      div = div.replace("p_ser", data['username']);
      div = div.replace("fullname", data['fullname'] );
      div = div.replace("name", data['name']);
      div = div.replace("username", data['username']);
  
      $('#me').append(div);
      get_users(data);*/
    });
  }
  