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
  
  Despres de això posarem la següent comanda mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
  i despres un exit.
  
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
  
1. Encuentra cómo se llama la unidad
Necesitará saber cómo se llama la unidad para montarla. Para hacer eso, podemos utilizar uno de los siguientes:

lsblk

sudo blkid

sudo fdisk -l


2. Crear un punto de montaje 

Esto necesita ser montado en el sistema de archivos en algún lugar . Por lo general, puede usar / mnt / si está siendo flojo y no hay nada más montado allí, pero de lo contrario querrá crear un nuevo directorio:

sudo  mkdir /media/usb

3. Montar USB

Seguidamente, tendremos que poner:

sudo mount /dev/sdb1 /media/usb

Cuando terminemos, simplemente ponemos:

sudo umount /media/usb
  
  
# INSTALACIÓ SERVEI WEB APACHE
  
  Pas1: Instalació de Apache--->sudo apt update i sudo apt install apache2
  
  Pas2: Ajustar el firewall----> sudo ufw app list, sudo afw allow 'Apache' i per verificar el canvi --->sudo ufw status 
  
  Pas3: Comprobar el servei web----> sudo systemctl status apache2, http://ipdelservidor
  
  
  

  








