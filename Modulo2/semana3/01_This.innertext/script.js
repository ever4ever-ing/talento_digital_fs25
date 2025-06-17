// Seleccionamos el botón por su id
let boton = document.getElementById("cambiarTexto");
let encabezado = document.querySelector('h1');
let parrafos = document.querySelectorAll('.textoCambiar');

boton.addEventListener("click", function () {
    // Cambia el texto del botón usando `this`
    this.innerText = "¡Texto cambiado!";
    encabezado.textContent = 'Titulo nuevo';

    for (let index = 0; index < parrafos.length - 1; index++) {
        parrafos[index].textContent = 'Parrafo nuevo';
    }
    alert('Has hecho click!');
});

encabezado.addEventListener("mouseover", function () {
    // Cambia el texto del botón usando `this`
    this.textContent = 'Nuevo Título';
});

