## POSTGRESQL PYTHON SCRIPT :-

### Script Includes :-

1. Connection to pgadmin.
2. Use of cursor to execute different query/commands.
3. CRUD operation query/code.
4. Relation between two table it can be ( one-to-one ) or ( many-to-one ).

### Setup For Postgres In Linux :-

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

```
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
```

```
sudo apt-get update
```

```
sudo apt-get -y install postgresql
```

