#!/bin/bash
#Respaldar Base de datos asociacion de colombianos
NOMBRE_BD="dolibarr"
ARCHIVO_CONEXION_DB="/home/rsa-key-20211019/MariaDbAsociacion/db.cnf"
RUTA_RESULTADO="/home/rsa-key-20211019/MariaDbAsociacion/Backups"
DIA=`date +"%d-%m-%Y"`
HORA=`date +"%H.%M"`
ARCHIVO_RESULTADO="BackupDolibarr-$DIA-$HORA.sql"
RUTA_FINAL="$RUTA_RESULTADO/$ARCHIVO_RESULTADO"
sudo mysqldump --defaults-file=$ARCHIVO_CONEXION_DB $NOMBRE_BD > $RUTA_FINAL
