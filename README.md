# ANTIVIRUS-VT

En este Readme estara escrito todas las herramientas que hemos utilizado e implementando para poner nuestro proyecto en marcha

# CODIGO DE PYTHON 

Esta dividido en dos carpetas:

`sendApi.py`

`FileReport.py`

# GITHUB DE LA BASE DE DATOS

Este es el link para acceder a todo los archivos que hemos utilizado para la nuestra DB

https://github.com/robbyrca/antivirus_vt-db

# GITHUB DE LA PAGINA WEB

Este es el link para acceder a nuestro github con todos los archivos que hemos necesitado para la web

https://github.com/robbyrca/antivirus_vt-website

# BASE DE DADES 
 
  Paso1: Instalar MySql
 
  Tendremos que hacer un `sudo apt update` y a continuación poner `sudo apt install mysql-server`
  
  Paso2: Configuración MySql
  
  Cuando ya lo tengamos instalado tendremos que modificar nuestro mySql a nuestro gusto y de esta manera se hace con la comanda `sudo mysql_secure_installation`
  
  Pas3: Ajustar la autenticación i los privilegioss del usuario
  
  Para poder hacerlo tendremos que abrir la consola MySql con la comanda `sudo mysql`
  
  Ahora comprobaremos el metodo de autenticación utilizado por uno de nuestros usuarios con la siguiente comanda:
  
  `mysql> SELECT user, authentication_string, plugin, host FROM mysql.user;`
  
  Ahora deberemos de cambiar el password por una contraseña segura de nuestra elección, teniendo en cuenta que esta comanda
  puede cambiar la contraseña "raiz": `mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH csching_sha2_password BY 'password';`
  
  Ahora ejecutaremos `FLUSH PRIVILEGES` para indicar el servidor que vuelva a cargar la tabla de permisos y que aplique los nuevos cambios.
  
  Despues de esto pondremos la siguiente comanda 
  
  `mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;`
  
Si deseamos conectarnos a la base de datos en local y con nombre de usuario root tendríamos que escribir:

`mysql -h localhost -u root -p`

Si queremos ver una lista de las bases de datos alojadas en nuestro servidor podemos escribir el comando show databases. Así:

`mysql>show databases;`

Una vez hemos terminado de trabajar con MySQL, si queremos cerrar la conexión con el servidor, simplemente escribimos "quit" desde el prompt de MySQL:

`mysql> quit`

Nuestra base de datos:

  host="localhost",
  
  user="robbyrca",
  
  password="QWEqwe123!",
  
  database="antivirus"

# REVISAR LINK -GESTIÓ USB-
  
PASO 1: CREAR EL DIRECTORIO PARA MONTAR LA MEMORIA USB**

`mkdir /media/usb`

**PASO 2: IDENTIFICAR EL NOMBRE DE LA UNIDAD QUE QUEREMOS MONTAR**

`ls -l /dev/sd`

PASO 3: MONTAR LA MEMORIA USB CON LA TERMINAL(mi memoria USB es FAT)**

sudo `mount -t vfat /dev/sdb1 /media/usb` —> USB en formato FATx32**

(sudo `mount -t ntfs-3g /dev/sdb1 /media/usb`)(USB enformateada en [NTFS](https://es.wikipedia.org/wiki/NTFS))

(sudo `mount -t ext4 /dev/sdb1 /media/usb`)(USB en formato [ext4](https://es.wikipedia.org/wiki/Ext4))

PASO 4: REALIZAR LAS OPERACIONES QUE TENEMOS QUE REALIZAR

Este es el comando:

`ls /media/us`

tendria que mostrar los archivos del pen 

**PASO 5: DESMONTAR LA MEMORIA USB**

sudo`umount /media/usb`

---

Lo primero que necesitas para tener un servidor Linux ubuntu que monte una unidad USB automáticamente es habilitar el soporte para USB en el sistema. 

Esto se puede hacer editando el archivo de configuración del kernel:

1. Abre una terminal y escribe `sudo nano /etc/default/grub`.
2. Busca la línea `GRUB_CMDLINE_LINUX_DEFAULT` y agrega `usbcore.autosuspend=-1` al final de la línea. Esto habilitará el soporte para USB.
3. Guarda el archivo y luego ejecuta el siguiente comando para actualizar el archivo de configuración del kernel: `sudo update-grub`.

Una vez que el soporte para USB está habilitado, puedes configurar el servidor para montar una unidad USB automáticamente. Esto se puede lograr editando el archivo de configuración del sistema "fstab", que controla cómo se montan los sistemas de archivos.

1. Abre una terminal y escribe: `sudo nano /etc/fstab`.

2. Agrega la siguiente línea al archivo: `/dev/sdb1 /mnt/usbdrive auto rw,user,noauto 0 0`. Esta línea le dice al sistema que monte la unidad USB en la carpeta `/mnt/usbdrive` cada vez que se conecte.

3. Guarda el archivo y reinicia el sistema para que los cambios surtan efecto.

Ahora, cada vez que conectes una unidad USB, el servidor Linux la montará automáticamente en la carpeta `/mnt/usbdrive`.

Este es el codigo para montar el USB en python:

#!/usr/bin/env python

*coding: utf-8 -*

import os

Comprobamos primero si hay algún dispositivo USB conectado

`usb_list = os.popen("lsblk | grep usb").read()`

Si hay algún dispositivo USB, procedemos a su montaje

`if usb_list:`

Extraemos el nombre del dispositivo

`dev_name = usb_list.split(" ")[0]`

Creamos el directorio donde se montará el dispositivo

`mount_dir = "/mnt/"+dev_name`
`os.popen("mkdir "+mount_dir)`

Montamos el dispositivo

`os.popen("mount /dev/"+dev_name+" "+mount_dir`

Informamos al usuario que ha sido montado

`print("Se ha montado el dispositivo "+dev_name+" en "+mount_dir)
else:
print("No se ha detectado ningún dispositivo USB")`


# Registrar los identificadores de los usb y los ficheros analizados en Base de Datos

[https://es.ccm.net/ordenadores/hardware/1538-encontrar-el-id-de-hardware-de-un-dispositivo/](https://es.ccm.net/ordenadores/hardware/1538-encontrar-el-id-de-hardware-de-un-dispositivo/) ] —> en windows

[ [https://github.com/Arkhelan/Proyecto/blob/main/Scripts/home/albert/fin/detusb.sh](https://github.com/Arkhelan/Proyecto/blob/main/Scripts/home/albert/fin/detusb.sh) ] —> .py del albert

Win +R —> ***devmgmt.msc***

propiedades

detalles

id hardware

Comandos que hemos utilizado

`df -h`
`lsblk`
`sudo fdisk -l`      —> ESTE ES EL BUENO “DISK MODEL=NOMBRE DEL USB”
`lsusb`

comandos GREP —> [ [https://www.freecodecamp.org/espanol/news/grep-command-tutorial-how-to-search-for-a-file-in-linux-and-unix-with-recursive-find/](https://www.freecodecamp.org/espanol/news/grep-command-tutorial-how-to-search-for-a-file-in-linux-and-unix-with-recursive-find/) ]

Hemos creado una carpeta llamada `usbworkspace` para trabajar con el usb…

Hemos creado 2 archivos: usbName —> `sudo fdisk -l > usbName`

En este archivo van todos los datos de los discos que tenga la maquina…

Creamos el segundo archivo: usbID —> `grep ‘Disk model:’ usbName > usbID` 

En este momento tenemos 2 id en el archivo usbID: `el modelo del USB` y `el disco de virtualBox llamado VBOX HARDDISK`

Para poder obtener `SOLO` el nombre del USB tenemos que excluir el VBOX HARDDISK

En teoria este comando tendria mostrar el nombre del usb pero NO lo hace

`grep -v "VBOX HARDDISK" Disk model usbName`

Para que funcione tenemos que crear un registro en la DDBB  

# INSTALACIÓ SERVEI WEB APACHE
  
Pas1: Instalació de Apache--->`sudo apt update i sudo apt install apache2`
  
Pas2: Ajustar el firewall----> `sudo ufw app list, sudo afw allow 'Apache'` i per verificar el canvi --->`sudo ufw status` 
  
Pas3: Comprobar el servei web----> `sudo systemctl status apache2, http://ipdelservidor`
  
  
  

  








