$(document).ready(function() {


    div =
        $('#parsear').click(function(e) {
            e.preventDefault();
            $.ajax({
                contentType: "application/json; charset=utf-8",
                url: "/parse_cobol/",
                data: 'data',
                dataType: "json",

                success: function(response) {

                    for (let i = 0; i < response.lineas.length; i++) {

                        var parElement = document.getElementById("myPar");
                        var para = document.createElement("p");
                        var textToAdd = document.createTextNode(response.lineas[i]);
                        para.appendChild(textToAdd);
                        parElement.appendChild(para)

                    }


                }
            });


        });

});