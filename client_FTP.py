#!/usr/bin/env python  
# --*-- coding: UTF-8 --*--  

from ftplib import FTP

# on démarre une connexion ftp à la machine "debian02" en créant une instance ftp
ftp=FTP('ftp-server')				

# authentification au serveur ftp avec un login et mot de passe
ftp.login(user='anonymous', passwd='', acct='')

# renvoie le message de bienvenue du serveur ftp
ftp.getwelcome()

# change de repertoire
ftp.cwd("debian/user/")  			 

# supprime le fichier "filename"
ftp.delete("filename")	 

# Renvoie la liste des fichiers du répertoire courant et leurs informations
ftp.retrlines('LIST', callback=None) 	

# crée un répertoire sur le serveur au chemin indiqué
ftp.mkd("pathname")				

# supprime le répertoire "dirname"
ftp.rmd("dirname")				

# renome le fichier "fromname" en "toname"
ftp.rename("fromname", "toname")	

# avec la cmd "STOR" envoie un fichier sur le server
ftp.storlines(cmd, file, callback=None)	

#ftp.storbinary(cmd, file, blocksize=8192, callback=None, rest=None)

# on termine la session de connexion
ftp.quit()		
