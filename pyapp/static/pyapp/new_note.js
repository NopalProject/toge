const csrftoken= Cookies.get('csrftoken');
//Borrar el cont de la nueva nota
function dropNewNote(){
  $('input[type=text]#noteTitle').val('');
  $('#noteBody').html('');
}
//actualiza las notas mostradas en pantalla
function actualizar(){
  $.ajax({
    method: "POST",
    headers: {'X-CSRFToken':csrftoken},
    url: '/my_notes/',
  }).done(function(data){
    jsdata=JSON.parse(data);
    var notes = ``;
    for(var n in jsdata){
notes += `<div class="col-sm-6 py-2">
  <div class="card" id="${jsdata[n].fields['userId']}">
    <div class="card-header">${jsdata[n].fields['noteTitle']}</div>
    <div class="card-body">
      <p class="card-text">${jsdata[n].fields['noteBody']}</p>
      <a href="#" class="btn btn-primary"><i data-feather="edit-2"></i>
        <span> Edit </span></a>
      <a href="#" class="btn btn-danger"><i data-feather="x-circle"></i>
        <span>Delete</span></a>
    </div>
    <div class="card-footer text-muted">
        Created on: ${jsdata[n].fields['noteCreatedDate']}
    </div>
  </div>
</div>`;
    }
    $('#savedNotes').html(notes);
    feather.replace();
  });
}

//metodos
$('#dropNewNote').click(dropNewNote);

$('#refreshNotes').click(actualizar);


$('#saveNewNote').click(function(){
$.ajax({
  method: "POST",
  headers: {'X-CSRFToken':csrftoken},
  url: "/ajax_test/",
  data: { noteTitle: $('#noteTitle').val(), noteBody: $('#noteBody').text() },
  dataType: "json"
}).done(function(){
  alert("datos guardados correctamente");
  dropNewNote();
  actualizar();
  $('#newNote').attr('class','collapse');
}).fail(function(data){
  alert("Oops, something went wrong");
  alert(data.msg);
});
});

