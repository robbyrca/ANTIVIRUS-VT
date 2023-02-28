# ANTIVIRUS-VT

En este Readme estara escrito todas las herramientas que hemos utilizado e implementando para poner nuestro proyecto en marcha
(los codigos que hemos utlizado en lenguaje pyhton estan escritos en 2 carpetas diferentes).

# BASE DE DADES 
 
  Pas1: Instalar MySql
 
  Tindrem que fer un sudo apt update y a continuació posarem sudo apt install mysql-server
  
  Pas2: Configuració MySql
  
  Quan ya el tindrem instalat tindrem que modificar el nostre mySql al nostre gust i aixó es fa amb la comanda sudo mysql_secure_installation
  
  Pas3: Ajustar la autenticació i els privilegis de usuari (aixó no es obligatori)
  
  Per poder fer-ho tindrem que obrir la consola MySql amb la comanda sudo mysql
  
  Ara comprobarem el metode de autenticació utilizat per unes dels nostres usuaris amb la següent comanda:
  mysql> SELECT user, authentication_string, plugin, host FROM mysql.user;
  
  Ara cambiarem el password per una contrasenya segura de la nostre elecció, tenint en compte que aquesta comanda
  pot cambiar la contrasenya "raiz": mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH csching_sha2_password BY 'password';
  
  Ara executarem FLUSH PRIVILEGES per indicar al servidor que torni a cargar la taula de permisos y apliqui el nous canvis
  
  Despres de això posarem la següent comanda mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
  i despres un exit.

  Pas4: Probar MariaDB 
  
  Posarem aquesta comanda: systemctl status mysql.service per poder comprobar el seu estat 
  
  Ahora intentarem establir una conexió amb la base de dades utilizant la eina mysqladmin(es un client que permet executar comandes administratives). Per exemple, aquesta comanda ens dira conectar MySql com root: sudo mysqladmin -p -u root version

Nuestra base de datos:

  host="localhost",
  
  user="robbyrca",
  
  password="QWEqwe123!",
  
  database="antivirus"

# REVISAR LINK -GESTIÓ USB-
  
1. Encuentra cómo se llama la unidad
Necesitará saber cómo se llama la unidad para montarla. Para hacer eso, dispare uno de los siguientes:

lsblk

sudo blkid

sudo fdisk -l

Usted está buscando una partición que debe ser algo como: /dev/sdb1. Cuantos más discos tenga, mayor será la letra. De todos modos, encuéntralo y recuerda cómo se llama.

2. Crear un punto de montaje (opcional)

Esto necesita ser montado en el sistema de archivos en algún lugar . Por lo general, puede usar / mnt / si está siendo flojo y no hay nada más montado allí, pero de lo contrario querrá crear un nuevo directorio:

sudo  mkdir /media/usb

3. Monte!

sudo mount /dev/sdb1 /media/usb

Cuando termines, simplemente ponemos:

sudo umount /media/usb
  
# INSTALACIÓ SERVEI WEB APACHE
  
  Pas1: Instalació de Apache--->sudo apt update i sudo apt install apache2
  
  Pas2: Ajustar el firewall----> sudo ufw app list, sudo afw allow 'Apache' i per verificar el canvi --->sudo ufw status 
  
  Pas3: Comprobar el servei web----> sudo systemctl status apache2, http://ipdelservidor
  

  








