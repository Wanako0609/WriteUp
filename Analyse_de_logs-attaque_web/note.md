
---

### Récapitulatif de tout ce qu’on a trouvé

#### 1. Injection SQL détectée dans les logs

En analysant les logs Apache, on tombe sur une requête SQL planquée dans le paramètre `order`, encodée en Base64.  
Une fois décodée, on a affaire à une **blind SQLi basée sur le temps (Time-Based SQLi)**.

---

#### 2. Structure de l’attaque

L’attaque repose sur une requête du type :

```sql
SELECT (CASE FIELD(
    CONCAT(
        SUBSTRING(BIN(ASCII(SUBSTRING(password, X, 1))), Y, Z),
        CHAR(48), CHAR(49)
    )
    WHEN 1 THEN SLEEP(A) 
    WHEN 2 THEN SLEEP(B) 
END) 
FROM membres WHERE id=1)
```

Explication rapide :

- On extrait les **bits binaires** des caractères du mot de passe, un à un.
- Le bit est ensuite converti en **temps de réponse** (via la fonction `SLEEP`).
- Les 3 premières requêtes permettent de récupérer **2 bits** à chaque fois, la 4e n’en donne qu’un seul.

**Mapping du temps → bits :**

- Pour les requêtes à 2 bits :
  - `0s` → `00`
  - `2s` → `01`
  - `4s` → `10`
  - `6s` → `11`

- Pour la dernière requête à 1 bit :
  - `2s` → `0`
  - `4s` → `1`

---

#### 3. Stratégie pour reconstituer le mot de passe

1. Lire les logs Apache.
2. Extraire les timestamps des requêtes.
3. Calculer les temps entre les requêtes (deltas).
4. Convertir chaque délai en bits binaires selon le schéma au-dessus.
5. Regrouper les bits en octets.
6. Convertir les octets en caractères ASCII.
7. Obtenir le mot de passe final.

---