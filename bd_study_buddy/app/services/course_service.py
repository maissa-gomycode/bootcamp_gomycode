
from app.cache.redis_cache import get_cache, set_cache


def get_course_categories():

    # Vérifier si les données existent dans Redis
    categories = get_cache("course_categories")

    if categories is not None:

        print("Donnée récupérée depuis Redis")

        return categories

    # Si la donnée n'existe pas dans Redis
    print("Cache Miss : récupération depuis la base de données")

    categories = "Python, HTML, CSS, JavaScript"

    # Enregistrer le résultat dans Redis pendant 5 minutes
    set_cache("course_categories", categories)

    return categories
