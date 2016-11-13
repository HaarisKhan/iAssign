var modal = document.getElementById('addModal');
var btn = document.getElementById("addBtn");
var span = document.getElementsByClassName("close")[0];

function popup() {
    addModal.style.display = "block";
}

function closeSpan() {
    addModal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
