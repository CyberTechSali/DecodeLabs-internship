def check_password(password):
    """Analyse un mot de passe et retourne son niveau : faible, moyen ou fort."""

    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    score = sum([length_ok, has_upper, has_digit, has_symbol])

    if not length_ok:
        return "faible"
    elif score <= 2:
        return "faible"
    elif score == 3:
        return "moyen"
    else:
        return "fort"


def print_banner():
    """Affiche la bannière de présentation de l'outil."""
    banner = """
====================================================
   PASSWORD STRENGTH CHECKER
   Auteur : CyberTechSali
   Verifie si un mot de passe est faible, moyen ou fort
   Tape 'quitter' pour arreter le programme
====================================================
"""
    print(banner)


if __name__ == "__main__":
    print_banner()

    while True:
        password = input("Entrez un mot de passe (ou 'quitter' pour arreter) : ")

        if password.lower() == "quitter":
            print("Fermeture du programme. A bientot !")
            break

        resultat = check_password(password)
        print("Force du mot de passe :", resultat)
        print("-" * 40)
