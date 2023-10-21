import os #line:1
import random #line:2
import string #line:3
from rich .console import Console #line:4
from rich .prompt import IntPrompt #line:5
from playwright .sync_api import sync_playwright #line:6
console =Console ()#line:8
def generate_password (length =20 ):#line:11
    O00OOO00O00O00OOO =string .ascii_letters +string .digits +string .punctuation #line:12
    return ''.join (random .choice (O00OOO00O00O00OOO )for _OO0000O00O0O00O0O in range (length ))#line:13
def generate_nickname ():#line:16
    try :#line:18
        with open ('nicknames.txt','r')as O0O0O0OOOOOOO0OO0 :#line:19
            O0O00OOO0O00O0OOO =[O000O00000000OO0O .strip ()for O000O00000000OO0O in O0O0O0OOOOOOO0OO0 .readlines ()]#line:20
            return random .choice (O0O00OOO0O00O0OOO )+str (random .randint (10000 ,999999 ))#line:21
    except FileNotFoundError :#line:22
        console .log ('[bold red]Error:[/] nicknames.txt file not found!')#line:23
        console .print ('[bold]Press enter to exit...[/]')#line:24
        console .input ()#line:25
        exit ()#line:26
def clear ():#line:29
    os .system ('cls'if os .name =='nt'else 'clear')#line:31
    console .print ('MaskaGenerator')#line:32
def registration ():#line:35
    O0O0000O00O000OOO =console .status ('Generating ACCOUNTS!',spinner ='line')#line:36
    O0O0000O00O000OOO .start ()#line:37
    with sync_playwright ()as O0OOO0O00OO0O00OO :#line:39
        OOO00O00O000OOO00 =generate_nickname ()#line:40
        OO00OO0OOO0OOOO00 =generate_password ()#line:41
        O0O0OOO00O000O0OO =O0OOO0O00OO0O00OO .firefox .launch (headless =False )#line:42
        O0OO0O0O000OOO000 =O0O0OOO00O000O0OO .new_context ()#line:43
        O000OO000OOOOOO00 =O0OO0O0O000OOO000 .new_page ()#line:44
        O000OO000OOOOOO00 .set_viewport_size ({"width":640 ,"height":480 })#line:45
        O000OO000OOOOOO00 .route ('https://apis.roblox.com/universal-app-configuration/v1/behaviors/cookie-policy/content',lambda OOO0000000OO0000O :OOO0000000OO0000O .abort ())#line:46
        O000OO000OOOOOO00 .goto ('https://www.roblox.com')#line:47
        O000OO000OOOOOO00 .locator ('//*[@id="MonthDropdown"]').select_option ('January')#line:48
        O000OO000OOOOOO00 .locator ('//*[@id="DayDropdown"]').select_option ('01')#line:49
        O000OO000OOOOOO00 .locator ('//*[@id="YearDropdown"]').select_option ('1999')#line:50
        while True :#line:52
            with O000OO000OOOOOO00 .expect_response ('https://auth.roblox.com/v1/usernames/validate')as OOO0000O0OOO00O00 :#line:54
                O000OO000OOOOOO00 .locator ('//*[@id="signup-username"]').fill (OOO00O00O000OOO00 )#line:55
            if OOO0000O0OOO00O00 .value .json ().get ('code')==0 :#line:56
                break #line:57
            else :#line:58
                OOO00O00O000OOO00 =generate_nickname ()#line:59
        O000OO000OOOOOO00 .locator ('//*[@id="signup-password"]').fill (OO00OO0OOO0OOOO00 )#line:61
        O000OO000OOOOOO00 .locator ('//*[@id="MaleButton"]').click ()#line:62
        with O000OO000OOOOOO00 .expect_response ('https://auth.roblox.com/v2/signup')as OOOOOOOO00OO0O000 :#line:64
            O000OO000OOOOOO00 .locator ('//*[@id="signup-button"]').click (timeout =0 )#line:65
        if OOOOOOOO00OO0O000 .value .status ==429 :#line:66
            O0O0OOO00O000O0OO .close ()#line:67
            O0O0000O00O000OOO .stop ()#line:68
            console .log ('[bold red]Error:[/] too many requests! Try to change your IP (you can use VPN, preferably paid)')#line:69
            console .print ('[bold]Press enter to continue...[/]')#line:70
            console .input ()#line:71
            return None #line:72
        else :#line:73
            O000OO000OOOOOO00 .wait_for_url ('https://www.roblox.com/home?nu=true',timeout =0 )#line:74
        with open ('cookies.txt','a')as OOOOO00OO0000O0O0 :#line:76
            OO0O00O0OOOO0O00O =O0OO0O0O000OOO000 .cookies ()#line:77
            OO00O0OOO00OO0OO0 =next ((OOOOO00OOOO00O000 for OOOOO00OOOO00O000 in OO0O00O0OOOO0O00O if OOOOO00OOOO00O000 ['name']=='.ROBLOSECURITY'),None )#line:78
            if OO00O0OOO00OO0OO0 :#line:79
                OO0O0OOO0OOO000OO =OO00O0OOO00OO0OO0 ['value']#line:80
                OOOOO00OO0000O0O0 .write (f'{OO0O0OOO0OOO000OO}\n')#line:81
        with open ('accounts.txt','a')as OOOOO00OO0000O0O0 :#line:83
            OOOOO00OO0000O0O0 .write (f'{OOO00O00O000OOO00}:{OO00OO0OOO0OOOO00}\n')#line:84
        console .log ('[bold green]Account generated successfully[/]',':white_check_mark:')#line:85
        O0O0OOO00O000O0OO .close ()#line:86
        O0O0000O00O000OOO .stop ()#line:87
        return None #line:88
def main ():#line:91
    try :#line:92
        clear ()#line:93
        O00O0O00OOOO0OOOO =999 #line:94
        clear ()#line:95
        for _O0OO0O0O0O0OO00O0 in range (O00O0O00OOOO0OOOO ):#line:96
            registration ()#line:97
    except KeyboardInterrupt :#line:98
        exit ()#line:99
if __name__ =='__main__':#line:101
    main ()#line:102
