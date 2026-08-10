import re

# --- Listes de reference utilisees par les fonctions de detection ---

MOTS_URGENCE = [
    "urgent", "immediately", "immediatement", "act now", "agissez maintenant",
    "24 hours", "24h", "account locked", "compte bloque", "suspended",
    "verify now", "expires", "expire"
]

MOTS_SENSIBLES = [
    "password", "mot de passe", "otp", "verification code", "code de verification",
    "mfa", "social security", "wire transfer", "virement", "bank details",
    "credit card", "carte bancaire", "ssn"
]

DOMAINES_GRATUITS = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

ROLES_SENSIBLES = ["ceo", "directeur", "director", "admin", "support",
                    "security", "securite", "hr", "rh", "it "]

EXTENSIONS_DANGEREUSES = [".exe", ".scr", ".js", ".iso", ".bat", ".vbs"]

RACCOURCISSEURS = ["bit.ly", "tinyurl", "t.co", "goo.gl"]

TLD_SUSPECTS = [".xyz", ".top", ".club", ".click", ".loan"]


def check_urgency(texte):
    """Detecte la presence de mots creant une pression temporelle artificielle."""
    texte_lower = texte.lower()
    trouves = [mot for mot in MOTS_URGENCE if mot in texte_lower]
    if trouves:
        return f"Langage d'urgence detecte : {', '.join(trouves)}"
    return None


def check_sensitive_request(texte):
    """Detecte une demande d'informations sensibles (mot de passe, MFA, etc.)."""
    texte_lower = texte.lower()
    trouves = [mot for mot in MOTS_SENSIBLES if mot in texte_lower]
    if trouves:
        return f"Demande d'informations sensibles : {', '.join(trouves)}"
    return None


def check_domain_mismatch(nom_affiche, email_expediteur):
    """Detecte une incoherence entre le nom affiche (role) et le domaine de l'email."""
    nom_lower = nom_affiche.lower()
    email_lower = email_expediteur.lower()

    a_un_role_sensible = any(role in nom_lower for role in ROLES_SENSIBLES)
    est_domaine_gratuit = any(domaine in email_lower for domaine in DOMAINES_GRATUITS)

    if a_un_role_sensible and est_domaine_gratuit:
        return f"Nom affiche '{nom_affiche}' suggere un role officiel, mais l'email vient d'un domaine gratuit ({email_expediteur})"
    return None


def check_suspicious_links(texte):
    """Detecte les raccourcisseurs d'URL, adresses IP brutes, et extensions de domaine suspectes."""
    texte_lower = texte.lower()
    alertes = []

    for raccourci in RACCOURCISSEURS:
        if raccourci in texte_lower:
            alertes.append(f"lien raccourci ({raccourci})")

    if re.search(r"https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", texte_lower):
        alertes.append("lien pointant vers une adresse IP brute")

    for tld in TLD_SUSPECTS:
        if tld in texte_lower:
            alertes.append(f"extension de domaine suspecte ({tld})")

    if alertes:
        return "Lien(s) suspect(s) : " + ", ".join(alertes)
    return None


def check_attachments(texte):
    """Detecte la mention de pieces jointes avec une extension dangereuse."""
    texte_lower = texte.lower()
    trouvees = [ext for ext in EXTENSIONS_DANGEREUSES if ext in texte_lower]
    if trouvees:
        return f"Piece jointe avec extension dangereuse : {', '.join(trouvees)}"
    return None


def analyze_email(nom_affiche, email_expediteur, sujet, corps):
    """Analyse un email complet et retourne la liste des red flags + un niveau de risque."""
    texte_complet = f"{sujet} {corps}"
    red_flags = []

    checks = [
        check_urgency(texte_complet),
        check_sensitive_request(texte_complet),
        check_domain_mismatch(nom_affiche, email_expediteur),
        check_suspicious_links(texte_complet),
        check_attachments(texte_complet),
    ]

    for resultat in checks:
        if resultat:
            red_flags.append(resultat)

    nombre_flags = len(red_flags)

    if nombre_flags == 0:
        niveau = "SAFE"
    elif nombre_flags <= 2:
        niveau = "SUSPICIOUS"
    else:
        niveau = "MALICIOUS"

    return red_flags, niveau


ACTIONS = {
    "SAFE": "-> Action : Close (aucune action requise)",
    "SUSPICIOUS": "-> Action : Warn User (avertir l'utilisateur, verifier par un autre canal)",
    "MALICIOUS": "-> Action : Block & Escalate (bloquer le domaine et signaler a l'equipe securite)",
}


def print_report(nom_affiche, email_expediteur, sujet, red_flags, niveau):
    print("-" * 50)
    print(f"Expediteur affiche : {nom_affiche}")
    print(f"Email reel         : {email_expediteur}")
    print(f"Sujet              : {sujet}")
    print(f"Niveau de risque   : {niveau}")

    if red_flags:
        print("Red flags detectes :")
        for flag in red_flags:
            print(f"  - {flag}")
    else:
        print("Aucun red flag detecte.")

    print(ACTIONS[niveau])
    print("-" * 50)


# --- Exemples integres pour tester rapidement le script ---

EXEMPLES = [
    {
        "nom_affiche": "Sarah Lee",
        "email": "sarah.lee@company.com",
        "sujet": "Q3 Project Status Update - Non-Urgent",
        "corps": "Hi Team, please review the attached project status for Q3 at your earliest convenience. No immediate action is required."
    },
    {
        "nom_affiche": "IT Security",
        "email": "support@login-updates.com",
        "sujet": "FW: Urgent Your Account Security Alert",
        "corps": "Your password will expire in 24 hours. Verify now by clicking this link: http://bit.ly/reset-account"
    },
    {
        "nom_affiche": "CEO Name",
        "email": "hacker@gmail.com",
        "sujet": "IMMEDIATE ACTION REQUIRED: Transfer Authorization",
        "corps": "URGENT: Process the attached wire transfer instruction immediately. This is critical and must remain strictly confidential. Attachment: instructions.exe"
    },
]


def print_banner():
    banner = """
====================================================
   PHISHING TRIAGE TOOL
   Auteur : CyberTechSali
   Analyse un email et detecte les red flags de phishing
   Tape 'quitter' pour arreter le programme
====================================================
"""
    print(banner)


def run_examples():
    print("\n=== ANALYSE DES EMAILS D'EXEMPLE ===")
    for exemple in EXEMPLES:
        red_flags, niveau = analyze_email(
            exemple["nom_affiche"], exemple["email"], exemple["sujet"], exemple["corps"]
        )
        print_report(exemple["nom_affiche"], exemple["email"], exemple["sujet"], red_flags, niveau)


def run_interactive():
    print("\n=== ANALYSE D'UN EMAIL PERSONNALISE ===")
    nom_affiche = input("Nom affiche de l'expediteur : ")
    email_expediteur = input("Adresse email reelle de l'expediteur : ")
    sujet = input("Sujet de l'email : ")
    corps = input("Corps du message (une seule ligne) : ")

    red_flags, niveau = analyze_email(nom_affiche, email_expediteur, sujet, corps)
    print_report(nom_affiche, email_expediteur, sujet, red_flags, niveau)


if __name__ == "__main__":
    print_banner()

    while True:
        choix = input("Choix : [1] Voir les exemples  [2] Analyser mon propre email  [quitter] : ")

        if choix.lower() == "quitter":
            print("Fermeture du programme. A bientot !")
            break
        elif choix == "1":
            run_examples()
        elif choix == "2":
            run_interactive()
        else:
            print("Choix invalide, tape 1, 2 ou 'quitter'.")
