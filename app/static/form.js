function function1()
{
    var myInput = document.getElementById("total_amount_due");
    check=parseFloat(myInput.value);
    if(check=>0){
    document.getElementById('get_quote').removeAttribute('disabled');
    }

}
