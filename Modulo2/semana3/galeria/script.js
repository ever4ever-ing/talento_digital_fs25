$(document).ready(function () {
    var images = [
        "https://cdn.pixabay.com/photo/2020/04/20/18/14/chile-pine-5069323_1280.jpg",
        "https://cdn.pixabay.com/photo/2015/10/26/13/23/tree-1007125_1280.jpg",
        "https://cdn.pixabay.com/photo/2019/08/14/03/48/the-tree-is-cold-4404641_1280.jpg",
        "https://cdn.pixabay.com/photo/2013/03/07/16/54/araucana-91294_1280.jpg",
        "https://cdn.pixabay.com/photo/2016/08/11/10/35/araucaria-araucana-1585360_640.jpg",
        "https://cdn.pixabay.com/photo/2015/04/07/06/12/conguillio-national-park-710571_640.jpg"
    ];
    var currentIndex = 0;
    // Mostrar modal con imagen grande
    $('.thumb').click(function () {
        currentIndex = $(this).index('.thumb');
        $('#modal-img').attr('src', images[currentIndex]);
        $('#modal').fadeIn(800);
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
