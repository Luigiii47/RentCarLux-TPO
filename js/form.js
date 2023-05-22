// ACTIVA EVENT LISTENER PARA EL EVENTO 'SUBMIT'
form.addEventListener('submit', e => {
    e.preventDefault();
    checkInputs();
})
// FUNCIÓN CON LAS VALIDACIONES
function checkInputs() {
    // CAPTURAMOS EN VARIABLES LOS VALUES QUE INGRESA EL USUARIO EN CADA CAMPO
    var formulario = document.getElementById("form");
    var nombre = document.getElementById("nombre").value.trim();
    var apellido = document.getElementById("apellido").value.trim();
    var email = document.getElementById("email").value.trim();
    var tel = document.getElementById("tel").value.trim();
    var mensaje = document.getElementById("msg").value.trim();

    // CAPTURAMOS EN UNA VARIABLE LA EXPRESIÓN REGULAR QUE REPRESENTA EL FORMATO CORRECTO DEL EMAIL
    var validEmail = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/

    // CHEQUEAMOS QUE NO HAYA CAMPOS VACÍOS
    if (nombre === '' || apellido === '' || email === '' || mensaje === '') {
        alert(`Por favor, complete todos los campos marcados con un asterisco.`);
        return false;
    }
    // VALIDAMOS NOMBRE
    for (var i = 0; i < nombre.length; i++) {
        var charCode = nombre.charCodeAt(i);
        if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32 || charCode === 225 || charCode === 233 || charCode === 237 || charCode === 243 || charCode === 250)) {
            alert(`El campo "Nombre" sólo puede contener letras y espacios.`);
            return false;
        }
    }
    // VALIDAMOS APELLIDO
    for (var i = 0; i < apellido.length; i++) {
        var charCode = apellido.charCodeAt(i);
        if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122) || charCode === 32 || charCode === 225 || charCode === 233 || charCode === 237 || charCode === 243 || charCode === 250)) {
            alert(`El campo "Apellido" sólo puede contener letras y espacios`);
            return false;
        }

    }
    // VALIDAMOS EMAIL
    if (!email.match(validEmail)) {
        alert(`E-Mail incorrecto\nEl formato debe ser: usuario@dominio.xxx`)
        return false
    }
    // SI TODO ESTÁ BIEN, SALTA ALERT AVISANDO QUE EL MENSAJE SE HA ENVIADO Y SE RESETEAN TODOS LOS CAMPOS 
    alert(`Mensaje enviado!\n\nGracias ${nombre} ${apellido}, le responderemos cuanto antes a su email ${email}`);
    formulario.reset();
}

// FALTA HACERLO FUNCIONAL, QUE SE ENVÍE EFECTIVAMENTE A UN MAIL. ENCONTRÉ UNA API PARA HACERLO, PERO POR ALGUNA RAZÓN, SI ESTÁ ACTIVAD ESTA VALIDACIÓN NO FUNCIONA. PROBÉ UBICAR EL LLEMADO <SCRIPT> EN VARIOS LUGARES, PERO AL APRECER ALGO BLOQUEA LA EJECUCIÓN CORRECTA DE LA API