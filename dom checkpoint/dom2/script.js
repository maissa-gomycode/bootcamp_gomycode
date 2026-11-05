
document.addEventListener("DOMContentLoaded", function() {

    // Sélectionner les éléments HTML
    const colorBox = document.getElementById("color-box");
    const changeColorBtn = document.getElementById("change-color-btn");

    // Fonction pour générer une couleur aléatoire
    function getRandomColor() {

        const randomColor = Math.floor(Math.random() * 16777215);

        return "#" + randomColor.toString(16).padStart(6, "0");
    }

    // Événement au clic sur le bouton
    changeColorBtn.addEventListener("click", function() {

        const newColor = getRandomColor();

        colorBox.style.backgroundColor = newColor;

    });

});
