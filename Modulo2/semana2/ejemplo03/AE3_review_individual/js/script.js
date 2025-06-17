// ESPERAMOS A QUE TODO EL CONTENIDO DEL HTML SE CARGUE COMPLETAMENTE ANTES DE EJECUTAR JAVASCRIPT
document.addEventListener("DOMContentLoaded", function () {

    // SELECCIONAMOS LOS ELEMENTOS <span> DEL HTML QUE MUESTRAN LOS CONTADORES
    // getElementById BUSCA UN ELEMENTO POR SU ID EN EL HTML
    const contadorSolicitudes = document.getElementById("contador-solicitudes");
    const contadorConexiones = document.getElementById("contador-conexiones");

    // SELECCIONAMOS TODOS LOS ÍCONOS QUE TENGAN LA CLASE "aceptar" (✅)
    // querySelectorAll DEVUELVE UNA LISTA CON TODOS LOS ELEMENTOS QUE COINCIDAN CON ESA CLASE
    const botonesAceptar = document.querySelectorAll(".aceptar");

    // SELECCIONAMOS TODOS LOS ÍCONOS QUE TENGAN LA CLASE "rechazar" (❌)
    const botonesRechazar = document.querySelectorAll(".rechazar");

    // FUNCIÓN QUE DISMINUYE EL CONTADOR DE SOLICITUDES
    function disminuirSolicitudes() {
        // TOMAMOS EL TEXTO ACTUAL (QUE ES UN NÚMERO COMO TEXTO) Y LO CONVERTIMOS EN NÚMERO
        let actual = parseInt(contadorSolicitudes.textContent);

        // LE RESTAMOS 1 Y ACTUALIZAMOS EL TEXTO DEL <span>
        contadorSolicitudes.textContent = actual - 1;
    }

    // FUNCIÓN QUE AUMENTA EL CONTADOR DE CONEXIONES
    function aumentarConexiones() {
        // TOMAMOS EL VALOR ACTUAL DE CONEXIONES
        let actual = parseInt(contadorConexiones.textContent);

        // SUMAMOS 1 Y LO MOSTRAMOS EN PANTALLA
        contadorConexiones.textContent = actual + 1;
    }

    // PARA CADA ÍCONO DE "ACEPTAR", AGREGAMOS UN EVENTO DE CLIC
    botonesAceptar.forEach(function (boton) {
        boton.addEventListener("click", function () {
            // this SE REFIERE AL ELEMENTO QUE SE CLICKEÓ (EN ESTE CASO, EL ICONO ✅)
            // parentElement SUBE UN NIVEL EN EL HTML Y TOMA EL <div> QUE CONTIENE TODA LA SOLICITUD
            const solicitud = this.parentElement;

            // BORRAMOS LA SOLICITUD DEL HTML
            solicitud.remove();

            // LLAMAMOS A LAS FUNCIONES PARA ACTUALIZAR LOS CONTADORES
            disminuirSolicitudes();   // RESTA 1 EN SOLICITUDES
            aumentarConexiones();     // SUMA 1 EN CONEXIONES

            // MOSTRAMOS UN MENSAJE AL USUARIO
            alert("¡Solicitud aceptada, tienes un nuevo amigo!");

        });
    });

    // PARA CADA ÍCONO DE "RECHAZAR", AGREGAMOS UN EVENTO DE CLIC
    botonesRechazar.forEach(function (boton) {
        boton.addEventListener("click", function () {
            // SUBIMOS AL CONTENEDOR DE LA SOLICITUD
            const solicitud = this.parentElement;

            // ELIMINAMOS ESE BLOQUE DEL HTML
            solicitud.remove();

            // ACTUALIZAMOS SOLO LAS SOLICITUDES, NO LAS CONEXIONES
            disminuirSolicitudes();

            // OPCIONAL: IMPRIMIMOS EN LA CONSOLA PARA SEGUIMIENTO
            console.log("Solicitud rechazada");
        });
    });

});
