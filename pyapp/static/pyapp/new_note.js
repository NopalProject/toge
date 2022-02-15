/*$('#saveNewNote').click(function(){
$.get("/pyapp/ajax_test/",
  function(data){
    alert(data);
  });
});*/

$('#saveNewNote').click(function(){
//  alert(1);
let csrftoken= Cookies.get('csrftoken');
//alert(csrftoken);
$.ajax({
  method: "POST",
  headers: {'X-CSRFToken':csrftoken},
  url: "/pyapp/ajax_test/",
  data: { noteTitle: "John", noteBody: "Boston" },
  dataType: "json"
}).done(function( msg ) {
  alert( "Data Saved: " + msg );
  console.log(msg);
});
});

