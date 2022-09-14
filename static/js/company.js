document.getElementById("products").addEventListener('change', function (event) {
    document.getElementById("productsTakaful").value = document.getElementById("products").value
});

document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("productsTakaful").value = document.getElementById("products").value
});