
document.getElementById("login-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                correo: email,
                contrasena: password
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert("¡Usuario registrado exitosamente!");
        } else {
            alert(`Error: ${data.error}`);
        }
    } catch (error) {
        console.error("Error en la solicitud:", error);
        alert("Hubo un problema al conectar con el servidor.");
    }
});
