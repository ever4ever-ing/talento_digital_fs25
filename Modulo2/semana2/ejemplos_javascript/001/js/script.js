// Ejemplo 1: if simple
let edad = 20;

if (edad >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");
}


// Ejemplo 2: if-else
let temperatura =11;
let estaLloviendo = true;

if (temperatura > 25) {
    console.log("Hace calor");
}else if( temperatura <= 10 || estaLloviendo){ // OPERADOR OR
    console.log("Muy frío, no habíamos visto un frío tanto este año como este año tanto frío");
}
else {
    console.log("No hace calor");
}

// Ejemplo 3: if-else if-else
let hora = 20.50;


if (hora < 12) {
    console.log("Buenos días");
} else if (hora < 18) {
    console.log("Buenas tardes");
} else if( hora>= 19 && hora<= 22 ){ //OPERADOR AND
    console.log("Toca Programar!");
    if(hora>=20.40 &&  hora <= 21 ){
        console.log("Recreo!");
    }else{
        console.log("Seguir aprendiendo.");
    }
}
else {
    console.log("Buenas noches");
}

for (let i = 0; i <= 10; i++) {
    console.log("Hola mundo!");
}


for (let i = 10; i > 0; i--) {
    console.log(i);
}


let i = 0;
while (i < 3) {
    console.log("Esto es un bucle while");
    i++;
}


// // Ejemplo 4: Operador ternario (if de una línea)
// let esDiaLaboral = true;
// let mensaje = esDiaLaboral ? "A trabajar" : "A descansar";
// console.log(mensaje);

// // Ejemplo 5: Condicionales anidados
// let esEstudiante = true;
// let tieneDescuento = false;

// if (esEstudiante) {
//     if (tieneDescuento) {
//         console.log("Tienes un 50% de descuento");
//     } else {
//         console.log("Tienes un 20% de descuento");
//     }
// } else {
//     console.log("No tienes descuento");
// }

// // Ejemplo 6: Usando operadores lógicos en condicionales
// let esMiembro = true;
// let puntos = 120;

// if (esMiembro && puntos > 100) {
//     console.log("Tienes acceso premium");
// } else if (esMiembro || puntos > 50) {
//     console.log("Tienes acceso estándar");
// } else {
//     console.log("Acceso limitado");
// }