// Ejemplo de uso de getUserMedia para acceder a la cámara del usuario

if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            const video = document.getElementById('video');
            video.srcObject = stream;
            console.log("Cámara activada");
        })
        .catch(function(err) {
            console.log("No se pudo acceder a la cámara:", err);
        });
} else {
    console.log("getUserMedia no es soportado en este navegador.");
}
