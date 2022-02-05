<script>
  const drkmdeSw = document.querySelector('#flexSwitchCheckDefault');

  function mo(){
    if(drkmdeSw.checked){
      document.body.style.background = "black";
      document.body.style.color = "white";
      document.getElementById('offcanvas').style.background ="gray";
      //alert('modo oscuro');
    }else{
      document.body.style.background = "white";
      document.body.style.color ="black";
      document.getElementById('offcanvas').style.background ="white";
      //alert('modo clarito');
    }
  }
</script>
