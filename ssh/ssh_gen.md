
## Generate a Key

ssh-keygen -t rsa -b 4096 -C "fabien.benureau@inria.fr"

## SSH Config

```
Host avakas
    User fbenurea
    HostName avakas.mcia.univ-bordeaux.fr
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly=yes
```

On your machine:
.ssh/config

## Kill a SSH Session

<Enter>+'~'+'.'
