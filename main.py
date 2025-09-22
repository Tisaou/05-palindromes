"""Module principal pour tester la fonction ispalindrome.
Ce programme vérifie si des mots ou phrases sont des palindromes.
"""

#### Fonction secondaire


def ispalindrome(p):
    """Prends en parametre une chaine de caractère et renvoie vrai si c'est un palindrome ou non"""
    p = p.strip()
    p = p.lower()
    p = p.replace("é","e")
    p = p.replace("è","e")
    p = p.replace("ê","e")
    p = p.replace("ë","e")
    p = p.replace("à","a")
    p = p.replace("ù","u")
    p = p.replace("ç","c")
    p = p.replace("ô","o")
    p = p.replace(" ", "")
    p = p.replace(",", "")
    p = p.replace(":", "")
    p = p.replace(";", "")
    p = p.replace("!", "")
    p = p.replace("?", "")
    p = p.replace("'", "")
    p = p.replace("-", "")
    p = p.replace(".", "")
    if p == p[::-1]:
        return True
    return False

#### Fonction principale


def main():
    """Fonction main qui permet de de faire appel a ispalindrome et de tester quelques mots"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
