# Stranger RSA​

![Consigne](img/consigne.png)

```python
$ openssl rsautl -decrypt -inkey private.pem -in EVIL-FILE.txt.enc -out flag
$ cat flag
221 x 7
$ openssl rsa -in private.pem  -pubout > key.pub
$ cat flag | openssl rsautl -encrypt -pubin -inkey public.pub > message.encrypted
$ 
```

