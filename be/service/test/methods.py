from imports import *


def speak(audio):
    engine = pyttsx3.init('dummy') 
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir !')

    if hour >= 12 and hour < 18:
        speak('Good Afternoon Sir !')

    else:
        speak('Good Evening Sir !')

    assname = ('Jarvis 1 point o')
    speak('I am your Assistant')
    speak(assname)


def username():
    speak('What should i call you sir')
    uname = takeCommand()
    speak('Welcome Mister')
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print('#####################'.center(columns))
    print('Welcome Mr.', uname.center(columns))
    print('#####################'.center(columns))

    speak('How can i Help you, Sir')


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        print(e)
        print('Unable to Recognize your voice.')
        return 'None'

    return query

def print(msg):
	mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
	host = "192.168.100.50" 
	port = 9100   
	try:           
		mysocket.connect((host, port)) #connecting to host
		mysocket.send(b"^XA^A0N,50,50^FO50,50^{0}^FS^XZ".format(msg))#using bytes
		mysocket.close () #closing connection
	except:
		print("Error with the connection")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


def wikipedia_(query):
    speak('Searching Wikipedia...')
    query = query.replace('wikipedia', '')
    results = wikipedia.summary(query, sentences=3)
    speak('According to Wikipedia')
    print(results)
    speak(results)


def play_music():
    speak('Here you go with music')
    # music_dir = 'G:\\Song'
    music_dir = 'C:\\Users\\GAURAV\\Music'
    songs = os.listdir(music_dir)
    print(songs)
    random = os.startfile(os.path.join(music_dir, songs[1]))


# if 'the time' in query:
def the_time():
    strTime = datetime.datetime.now().strftime('% H:% M:% S')
    speak(f'Sir, the time is {strTime}')


# if 'email to gaurav' in query:
def email_to():
    try:
        speak('What should I say?')
        content = takeCommand()
        to = 'Receiver email address'
        sendEmail(to, content)
        speak('Email has been sent !')
    except Exception as e:
        print(e)
        speak('I am not able to send this email')

# if 'send a mail' in query:


def send_a():
    try:
        speak('What should I say?')
        content = takeCommand()
        speak('whome should i send')
        to = input()
        sendEmail(to, content)
        speak('Email has been sent !')
    except Exception as e:
        print(e)
        speak('I am not able to send this email')

# if 'how are you' in query:


def how_are():
    speak('I am fine, Thank you')
    speak('How are you, Sir')

# if 'fine' in query or 'good' in query:


def fine_():
    speak('Its good to know that your fine')

# if 'change my name to' in query:
    query = query.replace('change my name to', '')
    assname = query

# if 'change name' in query:
    speak('What would you like to call me, Sir ')
    assname = takeCommand()
    speak('Thanks for naming me')

# if 'what's your name' in query or 'What is your name' in query:
    speak('My friends call me')
    speak(assname)
    print('My friends call me', assname)

# if 'exit' in query:


def exit_():
    speak('Thanks for giving me your time')
    exit()

# if 'who made you' in query or 'who created you' in query:
    speak('I have been created by Gaurav.')

# if 'joke' in query:


def joke_():
    speak(pyjokes.get_joke())

# if 'calculate' in query:


def calculate():
    app_id = 'Wolframalpha api id'
    client = wolframalpha.Client(app_id)
    indx = query.lower().split().index('calculate')
    query = query.split()[indx + 1:]
    res = client.query(' '.join(query))
    answer = next(res.results).text
    print('The answer is ' + answer)
    speak('The answer is ' + answer)

# if 'search' in query or 'play' in query:


def search_():
    query = query.replace('search', '')
    query = query.replace('play', '')
    webbrowser.open(query)

# if 'who i am' in query:
    speak('If you talk then definitely your human.')

# if 'why you came to world' in query:
    speak('Thanks to Gaurav. further Its a secret')

# if 'power point presentation' in query:


def power_point():
    speak('opening Power Point presentation')
    power = r'C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx'
    os.startfile(power)

# if 'is love' in query:


def is_love():
    speak('It is 7th sense that destroy all other senses')

# if 'who are you' in query:
    speak('I am your virtual assistant created by Gaurav')

# if 'reason for you' in query:


def reason_for():
    speak('I was created as a Minor project by Mister Gaurav ')

# if 'change background' in query:


def change_background():
    ctypes.windll.user32.SystemParametersInfoW(
        20,                                             0, 'Location of wallpaper', 0)
    speak('Background changed successfully')


# if 'news' in query:
def news_():

    try:
        jsonObj = urlopen(
            '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
        data = json.load(jsonObj)
        i = 1

        speak('here are some top news from the times of india')
        print('''=============== TIMES OF INDIA ============''' + '\n')

        for item in data['articles']:

            print(str(i) + '. ' + item['title'] + '\n')
            print(item['description'] + '\n')
            speak(str(i) + '. ' + item['title'] + '\n')
            i += 1
    except Exception as e:

        print(str(e))

# if 'lock window' in query:


def lock_window():
    speak('locking the device')
    ctypes.windll.user32.LockWorkStation()

# if 'shutdown system' in query:


def shutdown_system():
    speak('Hold On a Sec ! Your system is on its way to shut down')
    subprocess.call('shutdown / p /f')

# if 'empty recycle bin' in query:


def empty_recycle():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
    speak('Recycle Bin Recycled')

# if 'dont listen' in query or 'stop listening' in query:


def dont_listen():
    speak('for how much time you want to stop jarvis from listening commands')
    a = int(takeCommand())
    time.sleep(a)
    print(a)

# if 'where is' in query:


def where_is():
    query = query.replace('where is', '')
    location = query
    speak('User asked to Locate')
    speak(location)
    webbrowser.open(
        'https://www.google.nl / maps / place/' + location + '')

# # if 'camera' in query or 'take a photo' in query:
#     ec.capture(0, 'Jarvis Camera ', 'img.jpg')

# if 'restart' in query:


def restart_():
    subprocess.call(['shutdown', '/r'])

# if 'hibernate' in query or 'sleep' in query:


def hibernate():
    speak('Hibernating')
    subprocess.call('shutdown / h')

# if 'log off' in query or 'sign out' in query:


def log_off():
    speak('Make sure all the application are closed before sign-out')
    time.sleep(5)
    subprocess.call(['shutdown', '/l'])

# if 'write a note' in query:


def write_note():
    speak('What should i write, sir')
    note = takeCommand()
    file = open('jarvis.txt', 'w')
    speak('Sir, Should i include date and time')
    snfm = takeCommand()
    # if 'yes' in snfm or 'sure' in snfm:
    strTime = datetime.datetime.now().strftime('% H:% M:% S')
    file.write(strTime)
    file.write(' :- ')
    file.write(note)

# if 'show note' in query:


def show_note():
    speak('Showing Notes')
    file = open('jarvis.txt', 'r')
    print(file.read())
    speak(file.read(6))

# if 'update assistant' in query:


def update_assistant():
    speak(
        'After downloading file please replace this file with the downloaded one')
    url = '# url after uploading file'
    r = requests.get(url, stream=True)

    with open('Voice.py', 'wb') as Pypdf:

        total_length = int(r.headers.get('content-length'))

        for ch in progress.bar(r.iter_content(chunk_size=2391975),
                               expected_size=(total_length / 1024) + 1):
            if ch:
                Pypdf.write(ch)

# NPPR9-FWDCX-D2C8J-H872K-2YT43
# if 'jarvis' in query:


def jarvis_(assname):
    wishMe()
    speak('Jarvis 1 point o in your service Mister')
    speak(assname)

# if 'weather' in query:


def weather_():
    # Google Open weather website
    # to get API of Open weather
    api_key = 'Api key'
    base_url = 'http://api.openweathermap.org / data / 2.5 / weather?'
    speak(' City name ')
    print('City name : ')
    city_name = takeCommand()
    complete_url = base_url + 'appid =' + api_key + '&q =' + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x['cod'] != '404':
        y = x['main']
        current_temperature = y['temp']
        current_pressure = y['pressure']
        current_humidiy = y['humidity']
        z = x['weather']
        weather_description = z[0]['description']
        print(' Temperature (in kelvin unit) = ' + str(current_temperature)+'\n atmospheric pressure (in hPa unit) =' +
              str(current_pressure) + '\n humidity (in percentage) = ' + str(current_humidiy) + '\n description = ' + str(weather_description))

    else:
        speak(' City Not Found ')

# if 'send message ' in query:


def send_message():
    # You need to create an account on Twilio to use this service
    account_sid = 'Account Sid key'
    auth_token = 'Auth token'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=takeCommand(),
                        from_='Sender No',
                        to='Receiver No'
                    )

    print(message.sid)


# if 'Good Morning' in query:
def good_morning(assname, query):
    speak('A warm' + query)
    speak('How are you Mister')
    speak(assname)

# most asked question from google Assistant
# if 'will you be my gf' in query or 'will you be my bf' in query:


def will_you_be_my_gf():
    speak('Im not sure about, may be you should give me some time')

# if 'how are you' in query:


def how_are_you():
    speak('Im fine, glad you me that')

# if 'i love you' in query:


def i_love_you():
    speak('Its hard to understand')

# if 'what is' in query or 'who is' in query:


def what_is(query):
    # Use the same API key
    # that we have generated earlier
    client = wolframalpha.Client('API_ID')
    res = client.query(query)

    try:
        print(next(res.results).text)
        speak(next(res.results).text)
    except StopIteration:
        print('No results')


def analyse(methods, query):
    for each_command in methods:
        if each_command in query:
            filter(methods, lambda x: x['command']
                   == each_command)["method"](query)
            break


def menu_loop(methods):
    while True:
        query = takeCommand().lower()
        analyse(methods, query)


def clear(): return os.system('cls')


def open(url):
    def open_url():
        webbrowser.open(url)
    return open_url


methods = [
    {'command': 'jarvis', 'method': jarvis_},
    {'command': 'open google', 'method': open('google')},
    {'command': 'open youtube', 'method': open('youtube')},
    {'command': 'open stackoverflow', 'method': open('stackoverflow')},
    {'command': 'open github', 'method': open('github')},
    {'command': 'open facebook', 'method': open('facebook')},
    {'command': 'open twitter', 'method': open('twitter')},
    {'command': 'open linkedin', 'method': open('linkedin')},
    {'command': 'open instagram', 'method': open('instagram')},
    {'command': 'open whatsapp', 'method': open('whatsapp')},
    {'command': 'open snapchat', 'method': open('snapchat')},
    {'command': 'open tinder', 'method': open('tinder')},
    {'command': 'open gmail', 'method': open('gmail')},


]
