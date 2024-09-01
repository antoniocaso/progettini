from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
import re
import calendar
end_of_year = False
is_next = True
i = 1

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
time.sleep(0.5)
button = driver.find_element(By.CSS_SELECTOR, 'button[role="button"].css-175oi2r.r-1phboty')
button.click()

# Premi Log in
time.sleep(0.5)
button = driver.find_element(By.XPATH, "//*[contains(text(), 'Log in')]")
button.click()


# Premi campo username
time.sleep(1)
username = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
username.send_keys('netih22156@dovinou.com')

# Premi Next
time.sleep(0.5)
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
print("\n\rOra entro nella parte di ricerca.")

time.sleep(1.5)
while (is_next == True):
    try:
        print("\n\r -------Ora cerco"+ str(i) + "-------")
        button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/button['+ str(i) +']')
        print("\n\r-------Trovato qualcosa.-------")
        i = i + 1
    except NoSuchElementException:
        print("\n\r------------Eh, non ho trovato oltre bestia Dio. Vuol dire che quello di prima era l'ultimo.----------------")
        is_next = False
        last = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/button['+ str(i-1) +']/div/div/div[1]/div/div/span')
        testo_completo = last.text
        print("\n\r Ultimo pubblicato: " + testo_completo)
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

#Ora entro qua dentro sapendo da dove devo partire a schedulare.
giorno = int(giorno) + 1
time.sleep(3)
while end_of_year == False:
    # Premi su Post
    button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
    button.click()

    # Premi su Calendario
    time.sleep(0.2)
    button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/nav/div/div[2]/div/div[5]/button')
    button.click()    

    if giorno == 31:
        if mese == 12:
            end_of_year == True
            break 
        mese = int(mese) + 1
        giorno = 1
    # Premi su Mese
    time.sleep(0.2)
    option_6 = driver.find_element(By.XPATH, "//option[@value='"+str(mese)+"']")
    option_6.click() 
    
    # Premi su Giorno
    time.sleep(0.2)
    option_6 = driver.find_element(By.XPATH, "//option[@value='"+ str(giorno) + "'and text()='"+ str(giorno) + "']")
    option_6.click() 
    giorno = int(giorno) + 1

    # Premi su Conferma
    time.sleep(0.2)
    button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div[3]/div/button')
    button.click()

    # Scrivi tragedia
    time.sleep(1)
    button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
    button.send_keys('Ancora chiuso.')

    # Conferma e pubblica
    time.sleep(0.2)
    button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
    button.click() 
    time.sleep(1)
driver.quit()
