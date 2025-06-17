let perro = {
    nombre: "Firulais",
    raza: "Labrador",
    edad: 5,
    gustos: ["jugar con la pelota", "correr", "comer croquetas"],
    ladrar: function() {
        console.log("¡Guau! ¡Guau!");
    }
};

let gato = {
    nombre: "Michi",
    raza: "Siames",
    edad: 3,
    gustos: ["dormir", "botar taza!", "comer atún"],
    maullar: function() {
        console.log("¡Miau! ¡Miau!");
    },
    botarTaza: function() {
        console.log(this.gustos[1])
    }

};


perro.ladrar();
gato.maullar();
gato.botarTaza();


gato.maullar();
gato.maullar();
gato.maullar();
gato.maullar();
gato.maullar();



