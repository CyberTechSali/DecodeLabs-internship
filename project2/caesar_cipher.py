def encrypt(text, shift):
    """Chiffre un texte en decalant chaque lettre de 'shift' positions."""
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Espaces, chiffres, ponctuation : on ne touche pas
            result += char

    return result


def decrypt(text, shift):
    """Dechiffre un texte en inversant le decalage applique par encrypt()."""
    return encrypt(text, -shift)


def print_banner():
    """Affiche la banniere de presentation de l'outil."""
    banner = """
====================================================
   CAESAR CIPHER TOOL
   Auteur : CyberTechSali
   Chiffre et dechiffre un texte avec un decalage (cle)
   Tape 'quitter' pour arreter le programme
====================================================
"""
    print(banner)


if __name__ == "__main__":
    print_banner()

    while True:
        text = input("Entrez le texte a chiffrer (ou 'quitter' pour arreter) : ")

        if text.lower() == "quitter":
            print("Fermeture du programme. A bientot !")
            break

        shift = int(input("Entrez la cle (decalage, ex: 3) : "))

        encrypted = encrypt(text, shift)
        decrypted = decrypt(encrypted, shift)

        print("Texte original  :", text)
        print("Texte chiffre   :", encrypted)
        print("Texte dechiffre :", decrypted)
        print("-" * 40)
