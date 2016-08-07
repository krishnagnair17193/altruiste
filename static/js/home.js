$(function(){
    $('input').on('input', function() {
        $('#'+this.id).removeClass('input-error');
        $('input[type="submit"]').prop('disabled', false);
    }).trigger('input');
    $('#id_message').on('input', function() {
        $('#'+this.id).removeClass('input-error');
        $('input[type="submit"]').prop('disabled', false);
    }).trigger('#id_message');


    $('#contact-success').hide();
	$('#contact-form').on('submit', function(event){
    event.preventDefault();
    $('input[type="submit"]').prop('disabled', true);
    var url = $("#contact-form").attr("action");
    var contactFormData = $("#contact-form").serialize();
    $.ajax({
        url : url, // the endpoint
        type : "POST", // http method
        data : contactFormData, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#contact-success').show();
            $('#contact-form').hide();
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $.each(xhr.responseJSON, function (key, value) {
                var input = document.getElementsByName(key);
                var input_id = '#id_' + key;
                $(input_id).addClass("input-error");
            });

        }
    });
});
});