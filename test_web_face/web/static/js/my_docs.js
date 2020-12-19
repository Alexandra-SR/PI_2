function go_upload() {
  window.location = "/static/html/upload_docs.html";
}

function get_received() {
  let header = `<tr><th>Username</th><th>Name</th><th>Lastname</th><th>File name</th><th>View</th>
 </tr>`;
  $("#received_table").append(header);
  $.getJSON("/current", function (data) {
    $.getJSON(`/get_received/${data}`, function (data) {
      let size_a = data.length;
      if (size_a > 0) {
        let i = 0;
        $.each(data, function () {
        //   let card = `<tr><td>${data[i]["room"]}</td><td>${data[i]["res_date"]}</td><td>${data[i]["time"]}</td><td><button class="btn btn-danger" onclick="cancelRes(${data[i]["res_id"]})">Cancel Reservation</button></td></tr>`;
        //   $("#res_table").append(card);
            console.log(data[i]);
            i += 1;
        });
      } else {
        let div = `<div class="alert alert-danger" role="alert">You currently have<a class="alert-link"> not received any files.</a></div>`;
        $("#status_received").append(div);
      }
    });
  });
  get_sent();
}


function get_sent() {
    let header = `<tr><th>Username</th><th>Name</th><th>Lastname</th><th>File name</th><th>View</th>
   </tr>`;
    $("#sent_table").append(header);
    $.getJSON("/current", function (data) {
      $.getJSON(`/get_sent/${data}`, function (data) {
          console.log(data);
        let size_a = data.length;
        if (size_a > 0) {
          let i = 0;
          $.each(data, function () {
             let card = `<tr><td>${data[i]["sent_to_username"]}</td><td>${data[i]["name"]}</td><td>${data[i]["lastname"]}</td><td>${data[i]["location"]}</td><td><button class="btn btn-danger"">Click</button></td></tr>`;
             $("#sent_table").append(card);
             console.log(data[i]);
              i += 1;
          });
        } else {
          let div = `<div class="alert alert-danger" role="alert">You currently have<a class="alert-link"> not sent any files.</a></div>`;
          $("#status_sent").append(div);
        }
      });
    });
  }
  
