var modal = document.getElementById('addModal');
var btn = document.getElementById("addBtn");
var span = document.getElementsByClassName("close")[0];

function popup() {
    modal.style.display = "block";
}

function closeSpan() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
