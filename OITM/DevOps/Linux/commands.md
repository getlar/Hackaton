## Some commands:

```sh
NAME
     file – determine file type

SYNOPSIS
     file [-bcdDhiIkLnNprsvz] [--exclude-quiet] [--extension]
          [--mime-encoding] [--mime-type] [-f namefile] [-m magicfiles]
          [-P name=value] [-M magicfiles] file
     file -C [-m magicfiles]
     file [--help]

$ file -s /dev/wd0{b,d}
/dev/wd0b: data
/dev/wd0d: x86 boot sector

$ file -s /dev/hda{,1,2,3,4,5,6,7,8,9,10}
/dev/hda:   x86 boot sector
/dev/hda1:  Linux/i386 ext2 filesystem
/dev/hda2:  x86 boot sector
/dev/hda3:  x86 boot sector, extended partition table
/dev/hda4:  Linux/i386 ext2 filesystem
/dev/hda5:  Linux/i386 swap file
/dev/hda6:  Linux/i386 swap file
/dev/hda7:  Linux/i386 swap file
/dev/hda8:  Linux/i386 swap file
/dev/hda9:  empty
/dev/hda10: empty

$ file -i file.c file /dev/{wd0a,hda}
file.c:      text/x-c
file:        application/x-executable
/dev/hda:    application/x-not-regular-file
/dev/wd0a:   application/x-not-regular-file
```

```sh
NAME
     dd – convert and copy a file

SYNOPSIS
     dd [operands ...]

Check that a disk drive contains no bad blocks:

    dd if=/dev/ada0 of=/dev/null bs=1m

Do a refresh of a disk drive, in order to prevent presently recoverable
read errors from progressing into unrecoverable read errors:

    dd if=/dev/ada0 of=/dev/ada0 bs=1m

Remove parity bit from a file:

    dd if=file conv=parnone of=file.txt

Check for (even) parity errors on a file:

    dd if=file conv=pareven | cmp -x - file

To create an image of a Mode-1 CD-ROM, which is a commonly used format
for data CD-ROM disks, use a block size of 2048 bytes:

    dd if=/dev/cd0 of=filename.iso bs=2048
```

```sh
NAME
     od – octal, decimal, hex, ASCII dump

SYNOPSIS
     od [-aBbcDdeFfHhIiLlOosvXx] [-A base] [-j skip] [-N length] [-t type]
        [[+]offset[.][Bb]] [file ...]

Dump stdin skipping the first 13 bytes using named characters and dumping no more than 5 bytes:

    $ echo "FreeBSD: The power to serve" | od -An -a -j 13 -N 5
                p   o   w   e   r
```

```sh
NAME
     touch – change file access and modification times

SYNOPSIS
     touch [-A [-][[hh]mm]SS] [-achm] [-r file] [-t [[CC]YY]MMDDhhmm[.SS]]
           [-d YYYY-MM-DDThh:mm:SS[.frac][tz]] file ...
```


```sh
NAME
     whoami – display effective user id

SYNOPSIS
     whoami

```

```sh
NAME
     locate – find filenames quickly

SYNOPSIS
     locate [-0Scims] [-l limit] [-d database] pattern ...

$ locate -d $HOME/lib/mydb: foo

    will first search string “foo” in $HOME/lib/mydb and then in
    /var/db/locate.database.

$ locate -d $HOME/lib/mydb::/cdrom/locate.database foo

    will first search string “foo” in $HOME/lib/mydb and then in
    /var/db/locate.database and then in /cdrom/locate.database.
```


```sh
/proc/self/cmdline

/proc/<PID>/cmdline

/proc/PID/cmdline

/proc/[PID]/cmdline

    to get the command line arguments originally used for starting given process
```

```sh
#!/usr/bin/env zsh
    A /usr/bin/env parancs a $PATH változót használva keresi meg és indítja el a paraméterként megadott programot, esetünkben a zsh-t. Így (amennyiben a $PATH-en szerepelő könyvtárban található), a zsh indítása mindig sikeres lesz.
```