/**
Las funciones se definen con function, requieren un nombre, parametros opcionales, retorno opcional.
Se ejecutan al invocarlas.
 */
function encontrarMaximo(a, b) {
    console.log("-- Ejecutando funcion para encontrar máximo...")
    if (a > b) {
        return a; // devuelve un valor, en este caso es 'a'
    }else if(a == b){
        console.log("Los numero son iguales")
        return a;
    } 
    else {
        return b;
    }
}
console.log("1) Declarando variables...")
let numero1 = 10;
let numero2 = 10;
console.log("2) Llamando a la función...")
let maximo = encontrarMaximo(numero1, numero2);

console.log("El máximo entre", numero1, "y", numero2, "es:", maximo);