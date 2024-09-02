from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import re
import calendar
procedura_avvio = False
end_of_year = False
is_next = True
i = 1
is_true_last = False

now = datetime.datetime.now()
giorno_avvio = now.day
mese_avvio = now.month
minuti_avvio = now.minute
print("Oggi è il giorno", giorno_avvio, "del mese", mese_avvio)

# Inizializzazione del driver (Chrome senza bisogno di specificare il WebDriver)
driver = webdriver.Edge()

# Apri la pagina web
driver.get('https://x.com/tunnelavellino/status/1824849419508039757')  # Sostituisci con l'URL della pagina che vuoi visitare

# Attendi il caricamento della pagina (opzionale, modifica in base ai tuoi bisogni)
time.sleep(1)

# Premi cookies
button = driver.find_element(By.XPATH, '//span[text()="Refuse non-essential cookies"]/ancestor::button')
button.click()

# Premi X
time.sleep(1)
button = driver.find_element(By.CSS_SELECTOR, 'button[role="button"].css-175oi2r.r-1phboty')
button.click()

# Premi Log in
time.sleep(1)
button = driver.find_element(By.XPATH, "//*[contains(text(), 'Log in')]")
button.click()


# Premi campo username
time.sleep(1)
username = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
username.send_keys('netih22156@dovinou.com')

# Premi Next
time.sleep(1)
button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
button.click()

# Metti nickname per controllo
time.sleep(1)
passw = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
passw.send_keys('@tunnelavellino')
passw.send_keys(Keys.RETURN)


# Metti Password
time.sleep(1)
passw = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
passw.send_keys('!!nEtih12345!!')
passw.send_keys(Keys.RETURN)

# Premi su Post
time.sleep(2)
button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
button.click()

# Premi su Calendario
time.sleep(0.2)
button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[5]/button')
button.click()

# Premi su Post Schedulati
time.sleep(1)
button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/button')
button.click()
print("\n\rInizio la ricerca delle vecchie schedulazioni.")

time.sleep(1.5)
while (is_next == True):
    try:
        print("\n\rOra cerco la "+ str(i) + " schedulazione!")
        button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/button['+ str(i) +']')
        print("\n\rTrovata, è " + button.text + " !")
        i = i + 1
    except NoSuchElementException:
        is_next = False
        try:
            last = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/button['+ str(i-1) +']/div/div/div[1]/div/div/span')
            testo_completo = last.text
            print("\n\r Ho terminato la ricerca, l'ultima schedulazione è la seguente: " + testo_completo)
            pattern = r"(\w{3}) (\d{1,2})"
            match = re.search(pattern, testo_completo)
            if match:
                mese_stringa, giorno = match.groups()
                mesi_abbreviati = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, 
                        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
                # Ottieni il numero del mese dal dizionario
                mese = mesi_abbreviati[mese_stringa]
                print("Giorno:", giorno)
                print("Mese:", mese)
            else:
                print("Non sono riuscito a trovare il mese e il giorno nel testo.")
        except NoSuchElementException:
            print("\n\rNon ho trovato nessuna schedulazione precedente!.")
            giorno = giorno_avvio
            mese = mese_avvio
            procedura_avvio = True

#Mo dobbiamo tornare indietro alla schermata principale, premi freccia indietro
button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[1]/button')
button.click()

#Premi su X
time.sleep(0.2)
button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/button')
button.click()

#Premi su X
time.sleep(0.2)
button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/button')
button.click()

if(procedura_avvio == False):
    giorno = int(giorno) + 1 #Nella procedura normale io esco dal while sapendo il girono di ultima schedulazione e per questo faccio +1. 
time.sleep(3)



#Entri qua dentro avendo già il numero del giorno da schedulare, ovvero se sto al 31 entro con 32, se sto con 30 entro con 31.
while end_of_year == False:
   # if (mese == 4 or mese == 6 or mese == 9 or mese == 11) and giorno == 30:
     #   is_true_last = True
     #   print("Ultimo giorno del mese di 30 giorni!")
   # if(giorno == 31):
       # print("Ultimo giorno del mese!")
        #is_true_last = True
    # Premi su Post
    button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
    button.click()

    # Premi su Calendario
    time.sleep(0.2)
    button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[5]/button')
    button.click()    

    #Con Novembre, Aprile, Giugno, Settembre io mi devo fermare a 30. Con febbraio va bene 28 giorni fino al 2028. 
    #Questi sono casi in cui io devo schedulare per questo giorno, ma al giro dopo devo partire col nuovo mese, per cui io metto la verifica alla fine.
    #Così intanto ottengo che viene scritto quel giorno, e non si sfora oltre perché alla fine sistemo.
    #Non succede che scrivo il 32 di agosto perché io, nel flusso delle cose, quando giorno è 30 io entro con 31 e lo scrivo, poi scendo giù e metto in uscita mese nuovo e giorno 1,
    #ed è giusto.

    if(procedura_avvio == False): #il normale svolgimento è solo se non siamo in procedura d'avvio
        # Premi su Mese
        time.sleep(0.2)
        option_6 = driver.find_element(By.XPATH, "//option[@value='"+str(mese)+"']")
        option_6.click() 
        
        # Premi su Giorno
        time.sleep(0.2)
        option_6 = driver.find_element(By.XPATH, "//option[@value='"+ str(giorno) + "'and text()='"+ str(giorno) + "']")
        option_6.click()
        giorno = int(giorno) + 1

    if(procedura_avvio == True):
        # Premi su Mese
        time.sleep(0.2)
        option_6 = driver.find_element(By.XPATH, "//option[@value='"+str(mese_avvio)+"']")
        option_6.click() 
        
        # Premi su Giorno
        time.sleep(0.2)
        print("\n\rNon avendo trovato alcuna schedulazione precedente, iniziamo da oggi che è" + str(giorno_avvio)+"/"+str(mese_avvio))
        option_6 = driver.find_element(By.XPATH, "//option[@value='"+ str(giorno_avvio) + "'and text()='"+ str(giorno_avvio) + "']")
        option_6.click()
        giorno = int(giorno) + 1

        # Premi su Minuti

        time.sleep(0.2)
        option_6 = driver.find_element(By.XPATH, "//option[@value='"+ str(33) + "'and text()='"+ str(33) + "']")
        option_6.click() 

        if(33 < minuti_avvio):
            time.sleep(0.2)
            option_6 = driver.find_element(By.XPATH, "//option[@value='"+ str(59) + "'and text()='59']")
            option_6.click()       
        procedura_avvio = False

    # Premi su Conferma
    time.sleep(0.2)
    button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div[3]/div/button')
    button.click()

    # Scrivi tragedia
    time.sleep(0.2)
    button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
    button.send_keys('Ancora chiuso.')

    # Conferma e pubblica
    time.sleep(0.2)
    button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
    button.click() 
        

    if (mese == 4 or mese == 6 or mese == 9 or mese == 11) and giorno == 31: #and is_true_last == True:
        mese = int(mese) + 1
        giorno = 1
        print("E' finito un mese particolare di 30 giorni!")
    if mese == 2 and giorno == 29: # and is_true_last == True:
        mese = int(mese) + 1
        giorno = 1
        print("E' finito Febbraio!")
    if mese == 12 and giorno ==  32: # and is_true_last == True:
        mese = 1
        giorno = 1
        end_of_year = True
        print("Anno concluso!")
    if giorno == 32: # and is_true_last == True: 
        mese = int(mese) + 1
        giorno = 1
        print("E' finito il mese!")
    time.sleep(0.3)
driver.quit()
