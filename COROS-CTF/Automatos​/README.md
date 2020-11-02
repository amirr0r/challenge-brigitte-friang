# Automatos​

![Consigne](img/consigne.png)

```bash
$ zsteg brigitte.png -a
$ for f in $(zsteg -a brigitte.png | cut -d'.' -f1); do zsteg brigitte.png -E $f > zsteg_output/$f; done
```

## Liens utiles

- [Plastic Flagtastic Writeup](https://github.com/tghack/tg19hack/blob/master/forensics/plastic_flagtastic/writeup.md)