# Star Wars API

Script Node.js qui affiche tous les personnages d'un film Star Wars, en utilisant la [Star Wars API](https://swapi-api.hbtn.io/) et le module `request`.

## Usage

```shell
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
...
```

- Le premier argument est l'ID du film (ex. `3` = "Return of the Jedi").
- Un nom de personnage par ligne, dans le même ordre que la liste `characters` de l'endpoint `/films/`.

## Requirements

- Ubuntu 14.04 LTS, Node 10.14.x
- Module `request` (`sudo npm install request --global` puis `export NODE_PATH=/usr/lib/node_modules`)
- Code conforme à `semistandard`