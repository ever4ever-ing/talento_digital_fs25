let comprasSemana = [1000, 2000.5, 3000, 5000, 8000]
let total = 0;
for (let i = 0; i < comprasSemana.length; i++) {
    total += comprasSemana[i];
}
console.log("El gasto total fue: $" + total);