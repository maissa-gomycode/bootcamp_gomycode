// 1. Fonctions de manipulation de chaînes

// Inverser une chaîne de caractères
function inverserChaine(chaine) {
    return chaine.split("").reverse().join("");
}

console.log(inverserChaine("Bonjour"));

//Compter les caractères
function compterCaracteres(chaine) {
    return chaine.length;
}

console.log(compterCaracteres("JavaScript"));

// Mettre la première lettre de chaque mot en majuscule
function mettreEnMajuscule(phrase) {
    return phrase
        .split(" ")
        .map(mot => mot.charAt(0).toUpperCase() + mot.slice(1))
        .join(" ");
}

console.log(mettreEnMajuscule("bonjour tout le monde"));

// 2. Fonctions de tableau

// Trouver le maximum et le minimum
function trouverMaximum(tableau) {
    return Math.max(...tableau);
}

function trouverMinimum(tableau) {
    return Math.min(...tableau);
}

let nombres = [12, 5, 8, 20, 3];

console.log(trouverMaximum(nombres)); // 20
console.log(trouverMinimum(nombres)); // 3


// Calculer la somme d'un tableau
function calculerSomme(tableau) {
    return tableau.reduce((somme, nombre) => somme + nombre, 0);
}

console.log(calculerSomme([1, 2, 3, 4, 5]));


// Filtrer un tableau selon une condition
function filtrerTableau(tableau, condition) {
    return tableau.filter(condition);
}

let nombres2 = [1, 2, 3, 4, 5, 6];

let nombresPairs = filtrerTableau(
    nombres2,
    nombre => nombre % 2 === 0
);

console.log(nombresPairs);


// 3. Fonctions mathématiques

// Calculer la factorielle d'un nombre
function factorielle(n) {
    if (n < 0 || !Number.isInteger(n)) {
        return "Veuillez saisir un entier positif.";
    }

    let resultat = 1;

    for (let i = 1; i <= n; i++) {
        resultat *= i;
    }

    return resultat;
}

console.log(factorielle(5));


// Vérifier si un nombre est premier
function estPremier(n) {
    if (n <= 1 || !Number.isInteger(n)) {
        return false;
    }

    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }

    return true;
}

console.log(estPremier(7));  // true
console.log(estPremier(10)); // false

// Générer la suite de Fibonacci
function fibonacci(nombreTermes) {
    let suite = [];

    let a = 0;
    let b = 1;

    for (let i = 0; i < nombreTermes; i++) {
        suite.push(a);

        let suivant = a + b;
        a = b;
        b = suivant;
    }

    return suite;
}

console.log(fibonacci(8));


