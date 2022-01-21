$(document).ready(function () {
    

$('.parsear').click(function () { 
    $.ajax({
    url: "/parse_cobol/",
    dataType: "json",
    success: function (response) {
        console.log(response);
    }
});

    
});

}); 