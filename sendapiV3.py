import shutil,os,requests,json,time
from urllib import response
from filereportV1 import main_filereport

timesleepcount=0

file_source = '/home/robbyrca/ANTIVIRUS-VT/virustotal/'
file_destination1 = '/home/robbyrca/ANTIVIRUS-VT/procesandoid/'
file_destination2 = '/home/robbyrca/ANTIVIRUS-VT/verificado/'
file_destination3 = '/home/robbyrca/ANTIVIRUS-VT/cuarentena/'
file_destination4 = '/home/robbyrca/ANTIVIRUS-VT/id/'
file_destination5 = '/home/robbyrca/ANTIVIRUS-VT/procesandorep/'
file_here = '/home/robbyrca/ANTIVIRUS-VT/'

def upload(file):
    global timesleepcount
    global bucle
    url = "https://www.virustotal.com/api/v3/files"
    files = {"file": open(file, "rb")}
    headers = {
        "accept": "application/json",
        "x-apikey": "206706e5d63a9393a5786e3191ba9c471dcbb00305f4a32d49de38c45f20c4c7"
    }
    timesleepcount = timesleepcount + 1
    if timesleepcount == 5:
        print('Control de tiempo de 60 segundos')
        logtime()
        time.sleep(60)
        timesleepcount=0
    else:
        response = requests.post(url, files=files, headers=headers)
        if(response.status_code == 429):
            print("Error de cuota excedida :! o Error de demasiadas solicitudes controlate ;)")
            print("Codigo de error : " + str(response.status_code))
            exit()
        if response.status_code == 200:
            jsonresp = response.json()
            idget = jsonresp.get("data").get("id")
            print(file_destination1+filename + " sended")
            shutil.move(file_destination1+filename, file_destination5)
            idsave(idget,file_destination5+filename)
            log(filename)
            bucle = True
        else:
            print ("No s'ha pogut obtenir la URL :(")
            print ("ERROR al pujar el archiu :!")
            print ("Status code: " + str(response.status_code))

def uploadbig(file):
        global timesleepcount
        global buclebig
        files = {"file": open(file, "rb")}
        url = "https://www.virustotal.com/api/v3/files/upload_url"
        headers = {
            "accept": "application/json",
            "x-apikey": "206706e5d63a9393a5786e3191ba9c471dcbb00305f4a32d49de38c45f20c4c7"
        }
        timesleepcount = timesleepcount + 1
        if timesleepcount == 5:
            print('Control de tiempo de 60 segundos')
            logtime()
            time.sleep(60)
            timesleepcount=0

        else:
            response = requests.get(url, headers=headers)
            if(response.status_code == 429):
                print("Error de cuota excedida :! o Error de demasiadas solicitudes controlate ;)")
                print("Codigo de error : " + str(response.status_code))
                exit()

            if response.status_code == 200:
                result = response.json()
                url_upload = result.get("data")

            else:
                print ("No s'ha pogut obtenir la URL :(")
                print ("ERROR al pujar el archiu :!")
                print ("Status code: " + str(response.status_code))
        
            #Obtenim una id
            response = requests.post(url_upload, files=files, headers=headers)
            if(response.status_code == 429):
                print("Error de cuota excedida :! o Error de demasiadas solicitudes controlate ;)")
                print("Codigo de error : " + str(response.status_code))
                exit()

            if response.status_code == 200:
                result = response.json()
                idbig = result.get("data").get("id")
                print(file_destination1+filename + " sended")
                shutil.move(file_destination1+filename, file_destination5)
                idsave(idbig,file_destination5+filename)
                logbig(filename)
                buclebig=True

def idsave(id,file):
    with open(file_destination4+id, "w") as fp:
        json.dump(file+":"+id, fp, indent=2)

def logbig(file):
    with open(file_here+'logsfile', "a") as fp:
        fp.write(file_destination1+filename + " sended\n")
def logbigp(filename):
    with open(file_here+'logsfile', "a") as fp:
        fp.write(file_destination1+filename + " processing\n")        
def log(file):
    with open(file_here+'logsfile', "a") as fp:
        fp.write(file_destination1+filename + " sended\n")
def logp(filename):
    with open(file_here+'logsfile', "a") as fp:
        fp.write(file_destination1+filename + " processing\n")
def logtime():
    with open(file_here+'logsfile', "a") as fp:
        fp.write("Control de tiempo de 60 segundos\n")
def logpy():
    with open(file_here+'logsfile', "a") as fp:
        fp.write("\n#sendapiV3.py\n")

def checkFileExistance(enviocheck):
    try:
        with open(enviocheck, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

logpy()
for root, dirs, files in os.walk(file_source):
    for filename in files:
        filepath = os.path.join(root, filename)
        shutil.copy(filepath, file_destination1)
for root, dirs, files in os.walk(file_destination1):
    for filename in files:
        if (os.path.getsize(os.path.join(root, filename)) >> 20) > 32:  
            print("\n"+file_destination1+filename + " processing")
            logbigp(filename)
            buclebig = False
            while buclebig == False:
                uploadbig(file_destination1+filename)
        else:
            print("\n"+file_destination1+filename + " processing")
            logp(filename)
            bucle = False
            while bucle == False:
                upload(file_destination1+filename)

main_filereport()
