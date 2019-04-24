$(document).ready(function(){
    $('form').on('submit',function(event){
    var url = "{{ url_for('quote/new') }}";

        $.ajax({
            data:{
                gallons:$('#gallons_requested').val()
            },
            type:'POST',
            url:url,
            data:$('suggested_price').serialize(),
//            data:$('total_amount_due').serialize()
            success: function (data) {
                    console.log(data)
        })
//        .done(function(data){
//            $('#suggested_price').data(data.suggested_price)
//            $('#total_amount_due').data(data.total_amount_due)
//        })

        event.preventDefault();
    });

    $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
                }
            }
        })
    });
})