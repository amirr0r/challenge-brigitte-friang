#  Alone Muks

![Consigne](img/consigne.png)

Après s'être connecté en SSH en tant que **user**, on constate qu'on se retrouve dans un restricte shell:

![rbash](img/restricted_shell.png)

Pour s'en extraire, on peut utiliser **python**:

![python](img/python.png)

L'utilisateur **globalSystem** peut exécuter `vim` via `sudo`:

![globalSystem vim](img/globalSystem_vim.png)

Il est donc possible d'obtenir un shell:

![globalSystem shell](img/globalSystem_shell.png)

Rebelote pour l'utilisateur **navigationSystem**:

![navigationSystem shell](img/navigationSystem_shell.png)

Il est donc possible de lire le fichier flag.txt: `DGSESIEE{44adfb64ff382f6433eeb03ed829afe0}`

![flag](img/flag.png)

## Liens utiles

- [**gtfobins**: `vim`](https://gtfobins.github.io/gtfobins/vim/)