from selenium import webdriver
import random

import time

web = webdriver.Chrome()
web.get("https://docs.google.com/forms/d/e/1FAIpQLSeyA2GyWISebJxdDn1ZEeLrkjD6cyqfi2dDFjEtdn0Q8w16oA/viewform")
def fillform():
        
    email = ['north@mac.com',
    'thowell@optonline.net',
    'nimaclea@msn.com',
    'vsprintf@sbcglobal.net',
    'ngedmond@me.com',
    'shrapnull@att.net',
    'phyruxus@att.net',
    'heidrich@optonline.net',
    'british@verizon.net',
    'linuxhack@msn.com',
    'krueger@verizon.net',
    'garyjb@optonline.net']
    ran_email = random.randint(0,len(email))


    email_web = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    email_web.send_keys(email[ran_email])

    age = ['//*[@id="i9"]','//*[@id="i12"]','//*[@id="i15"]','//*[@id="i18"]']
    ran_age = random.randint(0,3)
    # print(ran_age)
    age_web = web.find_element('xpath', age[ran_age])
    age_web.click()

    gender = ['//*[@id="i28"]','//*[@id="i31"]']
    ran_gender = random.randint(0,1)
    gender_web = web.find_element('xpath',gender[ran_gender])
    gender_web.click()


    education = ['//*[@id="i41"]','//*[@id="i44"]','//*[@id="i47"]','//*[@id="i50"]','//*[@id="i53"]']
    ran_education = random.randint(0,4)
    education_web = web.find_element('xpath',education[ran_education])
    education_web.click()



    occupation = ['//*[@id="i60"]','//*[@id="i63"]','//*[@id="i66"]','//*[@id="i69"]','//*[@id="i72"]']
    ran_occupation = random.randint(0,4)
    occupation_web = web.find_element('xpath',occupation[ran_occupation])
    occupation_web.click()


    income =['//*[@id="i79"]','//*[@id="i82"]','//*[@id="i85"]','//*[@id="i88"]','//*[@id="i91"]']
    ran_income = random.randint(0,4)
    income_web = web.find_element('xpath',income[ran_income])
    income_web.click()


    religion = ['//*[@id="i98"]','//*[@id="i101"]','//*[@id="i104"]','//*[@id="i107"]']
    ran_religion = random.randint(0,3)
    religion_web = web.find_element('xpath',religion[ran_religion])
    religion_web.click()


    yourself = ['//*[@id="i117"]','//*[@id="i120"]','//*[@id="i123"]']
    ran_yourself =random.randint(0,2)
    yourself_web = web.find_element('xpath',yourself[ran_yourself])
    yourself_web.click()

    institution = ['//*[@id="i130"]','//*[@id="i133"]']
    ran_institution = random.randint(0,1)
    intstitution_web = web.find_element('xpath',institution[ran_institution])
    intstitution_web.click()


    practise = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_practise = random.randint(0,5)
    practise_web = web.find_element('xpath',practise[ran_practise])
    practise_web.click()


    places = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_places = random.randint(0,5)
    places_web = web.find_element('xpath',places[ran_places])
    places_web.click()


    prevail = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
            
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_prevail = random.randint(0,5)
    prevail_web = web.find_element('xpath',prevail[ran_prevail])
    prevail_web.click()

    remainplaces = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_remainplaces = random.randint(0,5)
    remainplaces_web = web.find_element('xpath',remainplaces[ran_remainplaces])
    remainplaces_web.click()



    electing = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_electing = random.randint(0,5)
    electing_web = web.find_element('xpath',electing[ran_electing])
    electing_web.click()


    worship = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_worship = random.randint(0,5)
    worship_web = web.find_element('xpath',worship[ran_worship])
    worship_web.click()


    nrel = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[17]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_nrel = random.randint(0,5)
    nrel_web = web.find_element('xpath',nrel[ran_nrel])
    nrel_web.click()


    purpose = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_purpose = random.randint(0,5)
    purpose_web = web.find_element('xpath',purpose[ran_purpose])
    purpose_web.click()


    ayodhya = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_ayodhya = random.randint(0,5)
    ayodhya_web = web.find_element('xpath',ayodhya[ran_ayodhya])
    ayodhya_web.click()



    hijab = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_hijab = random.randint(0,5)
    hijab_web = web.find_element('xpath',hijab[ran_hijab])
    hijab_web.click()



    up = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_up = random.randint(0,5)
    up_web = web.find_element('xpath',up[ran_up])
    up_web.click()



    inter = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_inter = random.randint(0,5)
    inter_web = web.find_element('xpath',inter[ran_inter])
    inter_web.click()

    mos = ['//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[2]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[4]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div',
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/span/div/label[6]/div[2]/div/div']
    ran_mos = random.randint(0,5)
    mos_web = web.find_element('xpath',mos[ran_mos])
    mos_web.click()


    submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()



    another_response = web.find_element('xpath','/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()


for i in range(0,2):
    fillform()

time.sleep(4)