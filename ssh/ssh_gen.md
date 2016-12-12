
## Generate a Key

ssh-keygen -t rsa -b 4096 -C "fabien.benureau@inria.fr"

## SSH Config

```
Host avakas
    User fbenurea
    HostName avakas.mcia.univ-bordeaux.fr
    IdentityFile ~/research/renc/.ssh/avakas_rsa
    IdentitiesOnly=yes
```

## Kill a SSH Session

<Enter>+'~'+'.'
