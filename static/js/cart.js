function show_shipping() { 
    if (document.getElementById("check_shipping").checked) {
            console.log('Checked');
            document.getElementById("shipping").style.display = 'none';
            $(document.getElementById("id_shipping_first_name")).val($(document.getElementById("id_billing_first_name")).val());
            $(document.getElementById("id_shipping_last_name")).val($(document.getElementById("id_billing_last_name")).val());
            $(document.getElementById("id_shipping_address")).val($(document.getElementById("id_billing_address")).val());
            $(document.getElementById("id_shipping_city")).val($(document.getElementById("id_billing_city")).val());  
            $(document.getElementById("id_shipping_state")).val($(document.getElementById("id_billing_state")).val()); 
            $(document.getElementById("id_shipping_zip_code")).val($(document.getElementById("id_billing_zip_code")).val());  
    } else {
            console.log('UnChecked');
            $(document.getElementById("id_shipping_first_name")).val("");
            $(document.getElementById("id_shipping_last_name")).val("");
            $(document.getElementById("id_shipping_address")).val("");
            $(document.getElementById("id_shipping_city")).val(""); 
            $(document.getElementById("id_shipping_state")).val(""); 
            $(document.getElementById("id_shipping_zip_code")).val(""); 
            document.getElementById("shipping").style.display = 'block';
    }
};

$(document).ready(function() {
    document.getElementById("check_shipping").onclick = show_shipping;

    $( "#id_billing_first_name" ).change(function() {
        if($('#check_shipping').is(':checked')) {
            $(document.getElementById("id_shipping_first_name")).val($(document.getElementById("id_billing_first_name")).val());
        }
    });

    $( "#id_billing_last_name" ).change(function() {
        if($('#check_shipping').is(':checked')) {
            $(document.getElementById("id_shipping_last_name")).val($(document.getElementById("id_billing_last_name")).val());
        }
    });

    $( "#id_billing_address" ).change(function() {
        if($('#check_shipping').is(':checked')) {
            $(document.getElementById("id_shipping_address")).val($(document.getElementById("id_billing_address")).val());
        }
    });

    $( "#id_billing_city" ).change(function() {
        if($('#check_shipping').is(':checked')) {
            $(document.getElementById("id_shipping_city")).val($(document.getElementById("id_billing_city")).val()); 
        }
    });

    $( "#id_billing_state" ).change(function() {
        if($('#check_shipping').is(':checked')) {
            $(document.getElementById("id_shipping_state")).val($(document.getElementById("id_billing_state")).val()); 
        }
    });

    $( "#id_billing_zip_code" ).change(function() {
        if($('#check_shipping').is(':checked')) {
            $(document.getElementById("id_shipping_zip_code")).val($(document.getElementById("id_billing_zip_code")).val()); 
        }
    });    
});

