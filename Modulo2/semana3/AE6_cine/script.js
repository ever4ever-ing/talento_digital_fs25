$(document).ready(function () {
    $('.btn-primary').click(function () {
        var modal = new bootstrap.Modal(document.getElementById('formModal'));
        modal.show().fadeOut(600);
    });
});
