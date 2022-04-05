document.addEventListener('DOMContentLoaded', function () {

    const checkboxs = document.querySelectorAll('#checkbox');
    const text = document.querySelector('.text');

    checkboxs.forEach(function (checkbox) {
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                this.closest('#text').style.color = "darkgreen";
            } else {
                this.closest('#text').style.color = "black";
            }
        });
    })

})