from bs4 import BeautifulSoup
import requests


urlWC = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/main-quest-line-wizard-city/'
urlKT = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/main-quest-line-krokotopia/'
urlMB = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/marleybone-main-quest-line-guide/'
urlMS = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/mooshu-main-quest-line-guide/'
urlDS = 'https://finalbastion.com/wizard101-guides/w101-spell-guides/dragonspyre-main-quest-line-guide/'
urlCS = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/celestia-main-quest-line/'
urlZF = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/zafaria-main-quest-line-guide/'
urlAV = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/avalon-main-quest-line-guide/'
urlAZ = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/azteca-main-quest-line/'
urlKR = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/khrysalis-main-quest-line-guide/'
urlPL = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/polaris-main-quest-line-guide/'
urlMR = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/mirage-main-quest-line/'
urlEM = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/empyrea-main-quest-line/'
urlWS = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/wysteria-main-quest-line-guide/'
urlGH = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/grizzleheim-main-quest-line-guide/'
urlWT = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/wintertusk-main-quest-line-guide/'
urlWCU = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/wizard-city-underground-quest-line/'
urlKM = 'https://finalbastion.com/wizard101-guides/w101-quest-guides/karamelle-main-quest-line-guide/'

urlList = [urlWC, urlKT, urlMB, urlMS, urlDS, urlCS, urlZF, urlAV, urlAZ, urlKR, urlPL, urlMR, urlEM, urlWS, urlGH, urlWT, urlWCU, urlKM]
worldList = ['Wizard City', 'Krokotopia', 'Marleybone', 'Mooshu', 'Dragonspyre', 'Celestia', 'Zafaria', 'Avalon', 'Azteca', 'Khrysalis', 'Polaris', 'Mirage', 'Empyrea', 'Wysteria', 'Grizzleheim', 'Wintertusk', 'Wizard City Underground', 'Karamelle']
questNumList = [39, 65, 50, 88, 106, 95, 148, 161, 197, 277, 99, 115, 149, 38, 68, 51, 19, 88]
def getNum(string):
    return ''.join(x for x in string if x.isdigit())

def questSearch(input):
    x = 0
    for url in urlList:
        response = requests.get(url)
        r = response.text
        soup = BeautifulSoup(r, 'html.parser')
        for p in soup.findAll('p', attrs = {'style': 'padding-left: 30px'}):
            for quest in (p.text).split('\n'):
                if input in quest.lower():
                    questNum = ''
                    for char in quest:
                        if char == '.':
                            break
                        questNum += char
                    return quest, questNum, questNumList[x], worldList[x], urlList[x]
        for p in soup.findAll('p', attrs = {'style': 'padding-left: 30px;'}):
            for quest in (p.text).split('\n'):
                if input in quest.lower():
                    questNum = ''
                    for char in quest:
                        if char == '.':
                            break
                        questNum += char
                    return quest, questNum, questNumList[x], worldList[x], urlList[x]
        for p in soup.findAll('p', attrs = {'style': 'padding-left: 40px'}):
            for quest in (p.text).split('\n'):
                if input in quest.lower():
                    questNum = ''
                    for char in quest:
                        if char == '.':
                            break
                        questNum += char
                    return quest, questNum, questNumList[x], worldList[x], urlList[x]
        for p in soup.findAll('p', attrs = {'style': 'padding-left: 40px;'}):
            for quest in (p.text).split('\n'):
                if input in quest.lower():
                    questNum = ''
                    for char in quest:
                        if char == '.':
                            break
                        questNum += char
                    return quest, questNum, questNumList[x], worldList[x], urlList[x]
        x += 1
    return None, None, None, None, None
        
quest = str(input()).lower()
questName, questNum, questNumMax, world, url = questSearch(quest)
if world == None:
    print("I couldn't find that quest. Please make sure it's a main quest and that you typed it in correctly.")
else:
    x = 1
    print(questName)
    for char in questName:
        if char == ' ':
            start = x
            break
        x += 1
    x = -1
    for char in questName:
        if char == '(' or char == '–':
            end = x
            break
        x += 1
    print(questName[start:end], questNum, questNumMax, world, (url + "#post_body:~:text=" + questName[:end].replace(" ", "%20")))
