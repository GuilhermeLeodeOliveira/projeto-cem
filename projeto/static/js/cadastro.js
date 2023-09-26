let cont=0;
function right(){
    cont++;
    window.location.href = "../";
    alert("Cheguei")
    if(cont>0){
        document.getElementById("comeco").style.display = "none";
    }
    
}

$(document).ready(function () {
    $('#tel').mask('(00)00000-0000');
  });
  