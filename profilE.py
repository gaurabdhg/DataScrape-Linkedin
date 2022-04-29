
def profilEx():    
    import csv
    import randomiser
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    #from selenium.webdriver.common.action_chains import ActionChains
    #from multiprocessing import Process

    
    #open browser enter site
    driver=webdriver.Chrome(executable_path="C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    driver.get("https://www.linkedin.com")
    
    
    #login details
    username=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='session_key'] ")))
    password=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='session_password'] ")))
    username.clear()
    password.clear()
    username.send_keys("")        #enter username/email address here between the quotes
    password.send_keys("")          #enter password here between the quotes

    
    #login
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[data-tracking-control-name='homepage-basic_signin-form_submit-button']"))).click()
    
    m=list()
    ct=0
    Rem=list()
    #wait=Process(target=randomiser.rndm())

    #read data file for crawl
    f= open('linkedin.csv','r') 
    startvalue=int(f.readline())            #read
    r=f.readlines()
    

    #open datafile and read boolean data
    B=open("boolfile.csv","r+")
    G=(B.readlines())
    counter=0
    for bool,link in zip(G,r):
        if bool=='0':
            Rem.append(counter)
            m.append(link.strip())
        counter  += 1    
    L=len(m)

            # if true:
            #    append to m
            #remember seek/position values and add to a list
            #remember p= len m

    for y in r:
        if ct>=startvalue:
            m.append(y.strip())    #parse
        ct +=1
    #write file
    
    w= open('write.csv','a')                          #needs update to append
    writer = csv.writer(w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #extraction
    count=0

    for loop in range(L):
        # try get data
        try:   
            driver.get(m[loop])
            randomiser.rndm()
            name=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[2]/div/div[1]/h1")))


            if EC.presence_of_element_located(driver.find_element_by_link_text('see more')):
                
                driver.find_element_by_link_text('see more').click()   

                data=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div/div[5]/span/div/section/div[1]/section/ul')

                poo=(data.text.split('\n'))
                poo.insert(0,name.text)

                poo.append(str(m[loop]))

                writer.writerow(poo)
                
                randomiser.rndm()
                        
    
        except:
            randomiser.rndm()
                        
        else:
            B.seek(Rem[loop])
            B.write('1')

    B.seek(L) 

    for count in range(L, (len(m)+1)):  # set range from p to len(m)+1
                
        try:   
            driver.get(m[count])
            randomiser.rndm()

            name=WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[2]/div/div[1]/h1")))

            data=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div/div[3]/div/div/main/div/div/div[5]/span/div/section/div[1]/section/ul')

            poo=(data.text.split('\n'))
            poo.insert(0,name.text)

            poo.append(str(m[count]))
            writer.writerow(poo)

            randomiser.rndm()
    
        except:  
            randomiser.rndm()
            B.write('0')
            
        else:
            B.write('1')

    
    
    #file close sequence            
    w.close()
    B.close()
    f.close()
    #close boolean file

    #driver close sequence
    driver.close()
    driver.quit()

    #setting memory of last read line
    with open("linkedin.csv","r+") as X:
        X.write(str(startvalue +count))
        X.close()

    
    return()
