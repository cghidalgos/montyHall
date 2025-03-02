document.addEventListener("DOMContentLoaded", function () {
    const btnSimular = document.getElementById("btn-simular");
    const numSimInput = document.getElementById("num_sim");
    const resultadoDiv = document.getElementById("resultado");
    const graficaImg = document.getElementById("grafica");
    const progressBar = document.getElementById("progress-bar");

    btnSimular.addEventListener("click", () => {
        const numSim = numSimInput.value;

        if (!numSim || numSim < 10) {
            alert("Por favor, ingrese un número válido de simulaciones.");
            return;
        }

        // Reiniciar progreso y ocultar imagen
        progressBar.style.width = "0%";
        progressBar.innerText = "0%";
        graficaImg.style.display = "none";

        // Simular incremento de barra de progreso
        let progress = 0;
        let interval = setInterval(() => {
            progress += 5;
            if (progress >= 100) {
                clearInterval(interval);
            }
            progressBar.style.width = progress + "%";
            progressBar.innerText = progress + "%";
        }, 100);

        // Enviar solicitud AJAX a Flask
        fetch("/simular", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ num_sim: numSim }),
        })
        .then(response => response.json())
        .then(data => {
            clearInterval(interval);
            progressBar.style.width = "100%";
            progressBar.innerText = "100%";

            resultadoDiv.innerHTML = `<h3>Probabilidad de ganar al cambiar: ${data.probabilidad}</h3>`;
            graficaImg.src = data.grafica + "?" + new Date().getTime();  // Evitar caché
            graficaImg.style.display = "block";
        })
        .catch(error => console.error("Error:", error));
    });
});
