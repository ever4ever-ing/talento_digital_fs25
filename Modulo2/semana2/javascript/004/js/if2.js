// Ejemplo: Información del cliente usando condicionales
// Obtenemos información básica del navegador y pantalla
const navegador = navigator.userAgent; // Cadena con información del navegador
const idioma = navigator.language; // Idioma principal configurado en el navegador
const anchoPantalla = window.screen.width; // Ancho de la pantalla en píxeles
const altoPantalla = window.screen.height; // Alto de la pantalla en píxeles

// Detectamos el navegador usando condicionales

console.log("User Agent detectado:", navegador);

if (navegador.includes("Edg")) {
    console.log("Estás usando Microsoft Edge");
} else if (navegador.includes("Chrome")) {
    console.log("Estás usando Google Chrome");
} else if (navegador.includes("Firefox")) {
    console.log("Estás usando Mozilla Firefox");
} else {
    console.log("Navegador no identificado: " + navegador);
}

// Clasificamos el tamaño de pantalla
if (anchoPantalla > 1200) {
    console.log("Estás usando una pantalla grande (desktop)");
} else if (anchoPantalla > 800) {
    console.log("Estás usando una pantalla mediana (tablet)");
} else {
    console.log("Estás usando una pantalla pequeña (móvil)");
}

// Geolocalización (requiere permiso del usuario)
// Verificamos si el navegador soporta geolocalización y solicitamos la ubicación
if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
        (pos) => {
            // Si el usuario da permiso, mostramos latitud y longitud
            console.log(`Tu ubicación aproximada: Latitud ${pos.coords.latitude}, Longitud ${pos.coords.longitude}`);
        },
        (err) => {
            // Si el usuario rechaza o hay error
            console.log("No se pudo obtener la ubicación o el usuario no dio permiso.");
        }
    );
} else {
    console.log("La geolocalización no está soportada en este navegador.");
}

// Cookies habilitadas
// navigator.cookieEnabled indica si las cookies están activadas
if (navigator.cookieEnabled) {
    console.log("Las cookies están habilitadas en tu navegador.");
} else {
    console.log("Las cookies están deshabilitadas en tu navegador.");
}

// Plataforma del sistema operativo
// navigator.platform da información básica del sistema operativo
const plataforma = navigator.platform;
if (plataforma.startsWith("Win")) {
    console.log("Estás usando Windows.");
} else if (plataforma.startsWith("Mac")) {
    console.log("Estás usando MacOS.");
} else if (plataforma.startsWith("Linux")) {
    console.log("Estás usando Linux.");
} else {
    console.log("Plataforma desconocida: " + plataforma);
}

// Estado de conexión
// navigator.onLine indica si el navegador está conectado a Internet
if (navigator.onLine) {
    console.log("Estás conectado a Internet.");
} else {
    console.log("No tienes conexión a Internet.");
}

// Profundidad de color de pantalla
// screen.colorDepth indica la cantidad de bits por píxel
if (screen.colorDepth >= 24) {
    console.log("Tu pantalla tiene alta profundidad de color.");
} else {
    console.log("Tu pantalla tiene baja profundidad de color.");
}

// Memoria RAM aproximada (si está disponible)
// navigator.deviceMemory da la cantidad de GB de RAM (no disponible en todos los navegadores)
if (navigator.deviceMemory) {
    if (navigator.deviceMemory >= 8) {
        console.log("Tienes un dispositivo con bastante memoria RAM (8GB o más).");
    } else {
        console.log(`Tu dispositivo tiene aproximadamente ${navigator.deviceMemory}GB de RAM.`);
    }
} else {
    console.log("No se pudo determinar la memoria RAM del dispositivo.");
}