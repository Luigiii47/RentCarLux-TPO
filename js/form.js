form.addEventListener('submit', e => {
    e.preventDefault();
    checkInputs();
})

function checkInputs() {
    var formulario = document.getElementById("form");
    var nombre = document.getElementById("nombre").value.trim();
    var apellido = document.getElementById("apellido").value.trim();
    var email = document.getElementById("email").value.trim();
    var tel = document.getElementById("tel").value.trim();
    var mensaje = document.getElementById("msg").value.trim();

    var validEmail = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/

    if (nombre === '' || apellido === '' || email === '' || mensaje === '') {
        alert(`Por favor, complete todos los campos obligatorios marcados con un asterisco.`);
        return false;
    }

    for (var i = 0; i < nombre.length; i++) {
        var charCode = nombre.charCodeAt(i);
        if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32 || charCode === 225 || charCode === 233 || charCode === 237 || charCode === 243 || charCode === 250)) {
            alert(`El campo "Nombre" sólo puede contener letras y espacios.`);
            return false;
        }
    }

    for (var i = 0; i < apellido.length; i++) {
        var charCode = apellido.charCodeAt(i);
        if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32 || charCode === 225 || charCode === 233 || charCode === 237 || charCode === 243 || charCode === 250)) {
            alert(`El campo "Apellido" sólo puede contener letras y espacios`);
            return false;
        }

    }
    if (!email.match(validEmail)) {
        alert(`E-Mail incorrecto\nEl formato debe ser: usuario@dominio.xxx`)
        return false
    }
    alert(`Mensaje enviado!\n\nGracias ${nombre} ${apellido}, le responderemos cuanto antes a su email: ${email}`);
    formulario.reset();
}