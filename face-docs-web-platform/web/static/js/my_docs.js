function go_upload() {
  window.location = "/static/html/options.html";
}

function get_received() {
  let header = `<tr><th>Usuario</th><th>Nombre</th><th>Apellido</th><th>Archivo</th><th>Descargar</th> </tr>`;
  $("#received_table").append(header);
  $.getJSON("/current", function (data) {
    $.getJSON(`/get_received/${data}`, function (data) {
      let size_a = data.length;
      if (size_a > 0) {
        let i = 0;
        $.each(data, function () {
          let card = `<tr><td>${data[i]["sent_from_username"]}</td><td>${data[i]["name"]}</td><td>${data[i]["lastname"]}</td><td>${data[i]["fileName"]}</td><td> <div class="site-content cf">
          <a class="btn btn-info" href="/${data[i]["location"]}" download="${data[i]["fileName"]}">Download</a>
       </div></td></tr>`;
          $("#received_table").append(card);
          console.log(data[i]);
          i += 1;
        });
      } else {
        let div = `<div class="alert alert-danger" role="alert">Actualmente <a class="alert-link"> no has recibido archivos.</a></div>`;
        $("#status_received").append(div);
      }
    });
  });
  get_sent();
}

function get_sent() {
  let header = `<tr><th>Usuario</th><th>Nombre</th><th>Apellido</th><th>Archivo</th><th>Descargar</th>
   </tr>`;
  $("#sent_table").append(header);
  $.getJSON("/current", function (data) {
    $.getJSON(`/get_sent/${data}`, function (data) {
      console.log(data);
      let size_a = data.length;
      if (size_a > 0) {
        let i = 0;
        $.each(data, function () {
          let card = `<tr><td>${data[i]["sent_to_username"]}</td><td>${data[i]["name"]}</td><td>${data[i]["lastname"]}</td><td>${data[i]["fileName"]}</td><td> <div class="site-content cf">
          <a class="btn btn-info" href="/${data[i]["location"]}" download="${data[i]["fileName"]}">Download</a>
       </div></td></tr>`;
          $("#sent_table").append(card);
          console.log(data[i]);
          i += 1;
        });
      } else {
        let div = `<div class="alert alert-danger" role="alert">Actualmente<a class="alert-link"> no has enviado archivos.</a></div>`;
        $("#status_sent").append(div);
      }
    });
  });
}

function download() {
  console.log("ENTRE DOWNLOAD");
  $.ajax({
    url: "/uploads/joaquin.ramirez_edir.vidal_user.png",
    method: "GET",
    xhrFields: {
      responseType: "blob",
    },
    success: function (data) {
      var a = document.createElement("a");
      var url = window.URL.createObjectURL(data);
      a.href = url;
      a.download = "myfile.png";
      document.body.append(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);
    },
  });
}
