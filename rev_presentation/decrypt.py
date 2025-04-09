def decrypt_xor(hex_string, key):
    """
    Décrypte une chaîne hexadécimale en appliquant XOR avec la clé donnée.
    """
    # Convertir la chaîne hexadécimale en bytes
    encrypted_bytes = bytes.fromhex(hex_string)
    
    # Appliquer XOR avec la clé pour chaque byte
    decrypted_bytes = bytes(b ^ key for b in encrypted_bytes)
    
    # Retourner la chaîne décryptée (UTF-8)
    return decrypted_bytes.decode('utf-8')

if __name__ == "__main__":
    # Clé utilisée pour le XOR
    XOR_KEY = 0x50
    
    # Demander la chaîne chiffrée en hexadécimal
    hex_string = input("Entrez la chaîne chiffrée (hexadécimale) : ")
    
    try:
        # Décrypter la chaîne
        decrypted_string = decrypt_xor(hex_string, XOR_KEY)
        print(f"Chaîne décryptée : {decrypted_string}")
    except Exception as e:
        print(f"Erreur lors du décryptage : {e}")

