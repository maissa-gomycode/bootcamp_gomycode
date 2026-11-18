
def generate_summary(text: str, max_bullets: int) -> dict:

    # Découpe le texte en phrases
    sentences = [
        sentence.strip()
        for sentence in text.replace("!", ".").replace("?", ".").split(".")
        if sentence.strip()
    ]

    # Sélectionne les premières phrases
    bullets = sentences[:max_bullets]

    return {
        "summary": " ".join(bullets),
        "bullets": bullets,
        "total_bullets": len(bullets)
    }
