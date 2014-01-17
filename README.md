prjSouth
========

Python + South

##### Cria as Tabelas (Installed App) #####
$ ./manage.py syncdb


#### Inicia a migracao ####
$ ./manage.py schemamigration core --initial


#### Migra os campos nas tabelas ####
$ ./manage.py migrate core --fake

#### agora, add um novo campo na model.... ####

#### coloca no schema antes de migra as alteracoes ####
$ ./manage.py schemamigration core --auto

#### migra as alteracoes (novos campos, novas tabelas..) ####
$ ./manage.py migrate core
