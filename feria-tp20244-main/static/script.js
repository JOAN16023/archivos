function validateLogin() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "usuario" && password === "contraseña") {
        alert("Inicio de sesión exitoso");
    } else {
        var message = document.querySelector(".message");
        message.style.display = "block";
    }
}