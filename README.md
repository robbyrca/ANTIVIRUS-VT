# ANTIVIRUS-VT

En este Readme estara escrito todas las herramientas que hemos utilizado e implementando para poner nuestro proyecto en marcha
(los codigos que hemos utlizado en lenguaje pyhton estan escritos en 2 carpetas diferentes).

# BASE DE DADES 
 
  Paso1: Instalar MySql
 
  Tendremos que hacer un sudo apt update y a continuación poner sudo apt install mysql-server
  
  Paso2: Configuración MySql
  
  Cuando ya lo tengamos instalado tendremos que modificar nuestro mySql a nuestro gusto y de esta manera se hace con la comanda sudo mysql_secure_installation
  
  Pas3: Ajustar la autenticación i los privilegioss del usuario
  
  Para poder hacerlo tendremos que abrir la consola MySql con la comanda sudo mysql
  
  Ahora comprobaremos el metodo de autenticación utilizado por uno de nuestros usuarios con la siguiente comanda:
  
  mysql> SELECT user, authentication_string, plugin, host FROM mysql.user;
  
  Ahora deberemos de cambiar el password por una contraseña segura de nuestra elección, teniendo en cuenta que esta comanda
  puede cambiar la contraseña "raiz": mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH csching_sha2_password BY 'password';
  
  Ahora ejecutaremos FLUSH PRIVILEGES para indicar el servidor que vuelva a cargar la tabla de permisos y que aplique los nuevos cambios.
  
  Despues de esto pondremos la siguiente comanda 
  
  mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
  
Si deseamos conectarnos a la base de datos en local y con nombre de usuario root tendríamos que escribir:

mysql -h localhost -u root -p

Si queremos ver una lista de las bases de datos alojadas en nuestro servidor podemos escribir el comando show databases. Así:

mysql>show databases;

Una vez hemos terminado de trabajar con MySQL, si queremos cerrar la conexión con el servidor, simplemente escribimos "quit" desde el prompt de MySQL:

mysql> quit

Nuestra base de datos:

  host="localhost",
  
  user="robbyrca",
  
  password="QWEqwe123!",
  
  database="antivirus"

# REVISAR LINK -GESTIÓ USB-
  
P**ASO 1: CREAR EL DIRECTORIO PARA MONTAR LA MEMORIA USB**

**`mkdir /media/usb`**

**PASO 2: IDENTIFICAR EL NOMBRE DE LA UNIDAD QUE QUEREMOS MONTAR**

**`ls -l /dev/sd*`**

**PASO 3: MONTAR LA MEMORIA USB CON LA TERMINAL(mi memoria USB es FAT)**

sudo **`mount -t vfat /dev/sdb1 /media/usb` —> USB en formato FATx32**

(sudo **`mount -t ntfs-3g /dev/sdb1 /media/usb`**)(**USB enformateada en [NTFS](https://es.wikipedia.org/wiki/NTFS))**

(sudo **`mount -t ext4 /dev/sdb1 /media/usb`)(USB en formato [ext4](https://es.wikipedia.org/wiki/Ext4))**

**PASO 4: REALIZAR LAS OPERACIONES QUE TENEMOS QUE REALIZAR**

**`ls /media/us`**

tendria que mostrar los archivos del pen 

**PASO 5: DESMONTAR LA MEMORIA USB**

sudo**`umount /media/usb`**

---

Lo primero que necesitas para tener un servidor Linux ubuntu que monte una unidad USB automáticamente es habilitar el soporte para USB en el sistema. 

Esto se puede hacer editando el archivo de configuración del kernel:

1. Abre una terminal y escribe "sudo nano /etc/default/grub".
2. Busca la línea "GRUB_CMDLINE_LINUX_DEFAULT" y agrega "usbcore.autosuspend=-1" al final de la línea. Esto habilitará el soporte para USB.
3. Guarda el archivo y luego ejecuta el siguiente comando para actualizar el archivo de configuración del kernel: "sudo update-grub".

Una vez que el soporte para USB está habilitado, puedes configurar el servidor para montar una unidad USB automáticamente. Esto se puede lograr editando el archivo de configuración del sistema "fstab", que controla cómo se montan los sistemas de archivos.

1. Abre una terminal y escribe "sudo nano /etc/fstab".
2. Agrega la siguiente línea al archivo: "/dev/sdb1 /mnt/usbdrive auto rw,user,noauto 0 0". Esta línea le dice al sistema que monte la unidad USB en la carpeta "/mnt/usbdrive" cada vez que se conecte.
3. Guarda el archivo y reinicia el sistema para que los cambios surtan efecto.

Ahora, cada vez que conectes una unidad USB, el servidor Linux la montará automáticamente en la carpeta "/mnt/usbdrive".

NO ME FUNCIONA ESTA SEGUNDA PARTE, LE HE DADO VUELTAS AL TEMA Y NADA

he encontrado esta info. puede servir ….

[https://ubunlog.com/montar-unidades-en-ubuntu/](https://ubunlog.com/montar-unidades-en-ubuntu/)

[https://vivaelsoftwarelibre.com/montar-particiones-al-iniciar-linux-automaticamente/](https://vivaelsoftwarelibre.com/montar-particiones-al-iniciar-linux-automaticamente/) —> UID numero….

NO ENCUENTRO NADA PARA MONTAR DE FORMA AUTOMÁTICA.

he visto un repositorio de GitHub donde se encuentra un script para montar de manera automática un USB 😇:

[ [https://github.com/Arkhelan/Proyecto/blob/main/Scripts/home/albert/fin/detusb.sh](https://github.com/Arkhelan/Proyecto/blob/main/Scripts/home/albert/fin/detusb.sh) ] 

!/bin/bash

echo "el script se ha iniciado" >> /home/albert/scripts/registro2.txt

for (( ; ; ));

do

echo "el script ha dado una vuelta" >> /home/albert/scripts/registro2.txt

a=0

sleep 1

for i in $(ls /dev/sd*)

do

if [ $i != "/dev/sda" ] && [ $i != "/dev/sda1" ] && [ $i != "/dev/sda2" ] && [ $i != "/dev/sda3" ];

then

a=$(echo $i)

fi

done

if [ $a != "0" ];

then

b=${a:-1}

if [ "$b" =="1" ];

then

a=$a"1"

fi

echo $a

break

fi

done

mount $a /media/usb

sudo chmod 777 /media/usb

echo "el script ha finalizado" >> /home/albert/scripts/registro2.txt

sudo bash /home/albert/fin/scriptfinal.sh

---

---

este es otro en BASH

!/bin/bash

Se verifica si hay un dispositivo usb conectado
dispositivoUSB=$(ls -1 /dev/sd* | grep -v 'sda\|sdb' | sed -n '1p')

Si hay un dispositivo USB conectado
if [ -n "$dispositivoUSB" ]; then

Se obtiene el nombre de la particion
nombreParticion=$(blkid $dispositivoUSB | awk '{print $2}' | cut -d '"' -f2)

Si hay una particion se monta
if [ -n "$nombreParticion" ]; then
sudo mount -t ntfs $dispositivoUSB /media/$nombreParticion
fi
fi

Ese codigo esta en bash —> vamos a crear uno en python!

#!/usr/bin/env python

*coding: utf-8 -*

import os

Comprobamos primero si hay algún dispositivo USB conectado
usb_list = os.popen("lsblk | grep usb").read()

Si hay algún dispositivo USB, procedemos a su montaje
if usb_list:

Extraemos el nombre del dispositivo
dev_name = usb_list.split(" ")[0]

Creamos el directorio donde se montará el dispositivo
mount_dir = "/mnt/"+dev_name
os.popen("mkdir "+mount_dir)

Montamos el dispositivo
os.popen("mount /dev/"+dev_name+" "+mount_dir)

Informamos al usuario que ha sido montado
print("Se ha montado el dispositivo "+dev_name+" en "+mount_dir)
else:
print("No se ha detectado ningún dispositivo USB")
  
  
# INSTALACIÓ SERVEI WEB APACHE
  
Pas1: Instalació de Apache--->sudo apt update i sudo apt install apache2
  
Pas2: Ajustar el firewall----> sudo ufw app list, sudo afw allow 'Apache' i per verificar el canvi --->sudo ufw status 
  
Pas3: Comprobar el servei web----> sudo systemctl status apache2, http://ipdelservidor
  
  
  

  








