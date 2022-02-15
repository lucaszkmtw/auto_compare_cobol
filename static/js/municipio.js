$('#parsear').click(function(e) {
    document.getElementById("myPar").innerHTML = "";
    var select = document.getElementById('municipio');
    var option = select.options[select.selectedIndex];
    archivo = option.value;
    console.log(archivo);
    e.preventDefault();
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: "/parse_cobol/",
        data: {
            'archivo': archivo
        },
        dataType: "json",

        success: function(response) {
            var parElement = document.getElementById("myPar");

            for (let i = 0; i < response.lineas.length; i++) {

                var para = document.createElement("p");
                para.classList.add("editable");
                var textToAdd = document.createTextNode(response.lineas[i]);
                para.appendChild(textToAdd);
                parElement.appendChild(para)
            }
        }
    });
});



$('body').on('click', '.editable', function() {






    // // var $el = $(this);

    // // var $input = $('<input/>').val($el.text());
    // // $el.replaceWith($input);

    // // var save = function() {
    // //     var $p = $('<p data-editable />').text($input.val());
    // //     $input.replaceWith($p);
    // // };

    /**
      We're defining the callback with `one`, because we know that
      the element will be gone just after that, and we don't want 
      any callbacks leftovers take memory. 
      Next time `p` turns into `input` this single callback 
      will be applied again.
    */


});



window.addEventListener("scroll", function(event) {

    var top = this.scrollY;

    if (top == '') {
        document.getElementById('button_scroll').style.display = 'none';

    } else {
        document.getElementById('button_scroll').style.display = 'block';
        document.getElementById('button_scroll').style.visibility = 'visible';
        document.getElementById("button_scroll").style.marginTop = top + "px";

    }

}, false);






function abrir_modal_creacion(url) {
    $('#creacion').load(url, function() {
        $(this).modal('show');


    });
}


function cerrar_modal_creacion() {
    $('#creacion').modal('hide');
}