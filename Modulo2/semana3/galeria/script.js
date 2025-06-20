$(document).ready(function () {
    // Collect all image sources from thumbnails
    var images = [];
    $('.thumb').each(function() {
        images.push($(this).attr('src'));
    });
    var currentIndex = 0;
    // Mostrar modal con imagen grande
    $('.thumb').click(function () {
        currentIndex = $(this).index('.thumb');// Obtener el índice de la imagen clickeada
        $('#modal-img').attr('src', images[currentIndex]); // Cambiar la imagen del modal
        $('#modal').fadeIn(800);// efectos jquery
    });

    // Botón cerrar
    $('.close').click(function () {
        $('#modal').fadeOut(300);
    });

    // Cerrar modal al hacer clic fuera de la imagen
    $('#modal').click(function (e) {
        if ($(e.target).is('#modal')) {
            $('#modal').fadeOut(300);
        }
    });

    // Navegación siguiente
    $('.next').click(function (e) {
        e.stopPropagation();// Prevenir propagación del evento
        currentIndex = (currentIndex + 1) % images.length; // Avanzar al siguiente índice
        $('#modal-img').fadeOut(150, function () {
            $(this).attr('src', images[currentIndex]).fadeIn(150); // Cambiar imagen
        });
    });

    // Navegación anterior
    $('.prev').click(function (e) {
        e.stopPropagation(); // Prevenir propagación del evento
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        $('#modal-img').fadeOut(150, function () {
            $(this).attr('src', images[currentIndex]).fadeIn(150);
        });
    });

    // Prevenir cierre al hacer clic en la imagen o controles
    $('.modal-content').click(function (e) {
        e.stopPropagation();
    });
});
