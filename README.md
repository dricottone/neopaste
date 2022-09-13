# neopaste

Paste file streams side-by-side, without concern for Unicode wide characters or
ANSI color codes.


### Usage

```
npaste [OPTIONS] [FILE ..]
```

|Option              |Description                                  |
|:-------------------|:--------------------------------------------|
|`--delimiter DELIM` |Delimit columns using `DELIM` (default: tab) |
|`--left`            |Left-justify columns (default)               |
|`--right`           |Right-justify columns                        |
|`--center`          |Center columns                               |
|`--help`            |Print help message                           |
|`--version`         |Print software version                       |

If `FILE` is `-`, or if no `FILE`s, read from STDIN.


### Example

Now, a core tenet of neopaste is compatibility with ANSI color codes. None of
which, of course, appear below. In fact, the use of `unbuffer` likely seems
strange. *Please* pretend that there are colors below.

```
$ npaste -d '  ' \
 <(df -h | grep -e '^Filesystem' -e '^/dev') \
 <(unbuffer cal) \
 <(wego | head -7)
Filesystem      Size  Used Avail Use% Mounted on        June 2020       Weather for Buffalo, US
/dev/sda3       220G  178G   31G  86% /           Su Mo Tu We Th Fr Sa
/dev/sda2       511M   62M  450M  13% /boot           1  2  3  4  5  6    _`/"".-.     light rain
/dev/sdc1       916G  101G  769G  12% /hdd         7  8  9 10 11 12 13     ,\_(   ).   73 (75) °F
                                                  14 15 16 17 18 19 20      /(___(__)  ↑ 5 mph
                                                  21 22 23 24 25 26 27        ʻ ʻ ʻ ʻ
                                                  28 29 30                   ʻ ʻ ʻ ʻ   0.0 in/h
```


## Dependencies

My recommendation is to install this software through **pipx**, which will
manage runtime dependencies for you.

The only runtime dependency is **wcwidth**, available from PyPI through pip.

Testing and build dependencies are **setuptools** and
[gap](https://git.dominic-ricottone.com/~dricottone/gap).


## Licensing

This software is distributed under the GPL license.

