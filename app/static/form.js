function function1()
{
    var myInput = document.getElementById("myid");
    check=parseFloat(myInput.value);
    if(check=>0){
    document.getElementById('get_quote').removeAttribute('disabled');
    }

}
