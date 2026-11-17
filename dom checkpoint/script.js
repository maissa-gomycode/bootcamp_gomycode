
// Sélectionner tous les articles
const cartItems = document.querySelectorAll(".cart-item");

// Sélectionner le total
const totalElement = document.getElementById("total");

// Fonction pour calculer le prix total
function calculateTotal() {
    let total = 0;

    document.querySelectorAll(".cart-item").forEach(item => {
        const price = parseFloat(
            item.querySelector(".price").textContent
        );

        const quantity = parseInt(
            item.querySelector(".quantity").textContent
        );

        total += price * quantity;
    });

    totalElement.textContent = total + " TND";
}

// Parcourir chaque article
cartItems.forEach(item => {

    // Bouton +
    const plusButton = item.querySelector(".plus");

    plusButton.addEventListener("click", function() {
        const quantityElement = item.querySelector(".quantity");

        let quantity = parseInt(quantityElement.textContent);

        quantity++;

        quantityElement.textContent = quantity;

        calculateTotal();
    });

    // Bouton -
    const minusButton = item.querySelector(".minus");

    minusButton.addEventListener("click", function() {
        const quantityElement = item.querySelector(".quantity");

        let quantity = parseInt(quantityElement.textContent);

        if (quantity > 1) {
            quantity--;

            quantityElement.textContent = quantity;
        }

        calculateTotal();
    });

    // Bouton supprimer
    const deleteButton = item.querySelector(".delete");

    deleteButton.addEventListener("click", function() {
        item.remove();

        calculateTotal();
    });

    // Bouton Like 
    const likeButton = item.querySelector(".like");

    likeButton.addEventListener("click", function() {
        likeButton.classList.toggle("liked");
    });

});

// Calcul initial du total
calculateTotal();
