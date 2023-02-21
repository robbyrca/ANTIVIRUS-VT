# ANTIVIRUS-VT

En este Readme estara escrito todas las herramientas que hemos utilizado e implementando para poner nuestro proyecto en marcha
(los codigos que hemos utlizado en lenguaje pyhton estan escritos en 3 carpetas diferentes).

# BASE DE DADES 
 
  Pas1: Instalar MySql
 
  Tindrem que fer un sudo apt update y a continuació posarem sudo apt install mysql-server
  
  Pas2: Configuració MySql
  
  Quan ya el tindrem instalat tindrem que modificar el nostre mySql al nostre gust i aixó es fa amb la comanda sudo mysql_secure_installation
  
  Pas3: Ajustar la autenticació i els privilegis de usuari (aixó no es obligatori)
  
  Per poder fer-ho tindrem que obrir la consola MySQl amb la comanda sudo mysql
  
  Ara comprobarem el metode de autenticació utilizat per unes dels nostres usuaris amb la següent comanda:
  mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
  
  Ara cambiarem el password per una contrasenya segura de la nostre elecció, tenint en compte que aquesta comanda
  pot cambiar la contrasenya "raiz": mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH csching_sha2_password BY 'password';
  
  Ara executarem FLUSH PRIVILEGES per indicar al servidor que torni a cargar la taula de permisos y apliqui el nous canvis
  
  Despres de això posarem la següent comanda mysql> SELECT user,authentication_string,plugin,host FROM mysql.user;
  i despres un exit.

  Pas4:Probar MariaDB 
  
  Posarem aquesta comanda: systemctl status mysql.service per poder comprobar el seu estat 
  
  Ahora intentarem establir una conexió amb la base de dades utilizant la eina mysqladmin(es un client que permet executar comandes administratives). Per exemple, aquesta comanda ens dira conectar MySql com root: sudo mysqladmin -p -u root version

# REVISAR LINK -GESTIÓ USB-
  
  Pas1: Creació del directori per montar la memoria USB-->mkdir /media/usb
  
  Pas2: Identificació del nom de la unitat que volem montar ---> ls-l /dev/sd
  
  Pas3: Montar la memoria USB amb la terminal-->sudo mount , mount -t vfat /dev/sdb1 /media/usb, mount -t nfts-3g /dev/sdb1 /media/usb, mount -t ext4 /dev/sdb1  /media/usb
  
  Pas4: Realitzar les operacions que tenim que realitzar --->ls media/usb
  
  Pas5: Desmontar la memoria USB ---->umount /media/usb








