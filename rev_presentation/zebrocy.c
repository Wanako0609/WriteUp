#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

// Clé XOR unique
#define XOR_KEY 0x50

const char hash_hex[] = "f6541b569787aa050c54ad85976ac5b729697a022be188b0040d37aa91e49ae2";
// Chiffre chaque caractère en appliquant XOR avec la clé
void xor_with_key(const char *input, uint8_t *output, size_t input_len) {
    for (size_t i = 0; i < input_len; i++) {
        output[i] = input[i] ^ XOR_KEY;
    }
}

// Convertit les données chiffrées en chaîne hexadécimale
void to_hex_string(const uint8_t *data, char *hex_str, size_t len) {
    for (size_t i = 0; i < len; i++) {
        sprintf(&hex_str[i * 2], "%02x", data[i]);
    }
    hex_str[len * 2] = '\0'; // Ajouter un caractère de fin de chaîne
}

// Envoie la chaîne hexadécimale via curl à http://127.0.0.1
void send_to_localhost(const char *data_hex) {
    char command[512];
    snprintf(command, sizeof(command), "curl -X POST -d \"%s\" http://127.0.0.1", data_hex);
    system(command);
}

int main() {
    // Demander à l'utilisateur d'entrer une chaîne
    char input[256];
    printf("Entrez une chaîne à chiffrer : ");
    if (fgets(input, sizeof(input), stdin) == NULL) {
        perror("Erreur lors de la lecture de l'entrée");
        return 1;
    }

    // Supprimer le caractère de fin de ligne (si présent)
    size_t input_len = strlen(input);
    if (input[input_len - 1] == '\n') {
        input[input_len - 1] = '\0';
        input_len--;
    }

    // Chiffrer la chaîne avec XOR
    uint8_t encrypted[input_len];
    xor_with_key(input, encrypted, input_len);

    // Convertir le résultat en hexadécimal
    char encrypted_hex[input_len * 2 + 1];
    to_hex_string(encrypted, encrypted_hex, input_len);

    // Envoyer les données chiffrées
    send_to_localhost(encrypted_hex);

    printf("Données chiffrées envoyées à http://127.0.0.1 : %s\n", encrypted_hex);
    return 0;
}

