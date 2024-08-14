import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import subprocess  # Import subprocess for executing commands
import requests
import bs4
import pyjokes  # Import pyjokes for joke functionality
from sys import platform
import cv2  # Import OpenCV for camera functionality
import pywhatkit  # Import pywhatkit for playing YouTube videos

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Get the available voices and set the desired voice
voices = engine.getProperty('voices')
# Example: Set voice to female (assuming the second voice is female)
engine.setProperty('voice', voices[1].id)  # You may need to adjust the index based on available voices

def speak(text, volume=1):
    engine.setProperty('volume', volume)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()  # Convert to lowercase
        print(f"User said: {query}\n")  # For debugging purposes
    except Exception as e:
        print(f"Error: {e}")
        print("Say that again please...")
        return "None"
    return query

def search_google(query):
    try:
        url = f"https://www.google.com/search?q=query}"
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")

        # Try to find a concise answer
        answer = soup.find("div", class_="BNeawe").text
        return answer
    except Exception as e:
        print(f"Google search error: {e}")
        return None

def process_command(query):
    # Define a dictionary to store custom commands and their actions
    custom_commands = {
        'hello jarvis':  lambda: speak("Hello sir, how can I help you today?"),
        'hello jarvis how are you': lambda: speak("I am good what about you "),
        'i am also fine': lambda: speak("o really nice to meet you"),
        'thank you jarvis ': lambda: speak("welcome sir if you need any further help i am always their for you"),
        'how are you': lambda: speak("I am fine, sir. Thank you for asking. what about you"),
        'what is your name': lambda: speak("My name is Jarvis, your personal assistant."),
        'who made you': lambda: speak("I was created by Narayan."),
        'who is narayan': lambda: speak("Narayan is the person who created me."),
     'tell me about your self jarvis ': lambda: speak("i am jarvis your Personal assistant. i am hear to help you say waht can i do for you  "),
    'tell me about your self ': lambda: speak("i am jarvis your Personal assistant. i am hear to help you say waht can i do for you  "),
    'who is your father': lambda: speak("i am just set of instruction i do not have any father but i know narayan create me "),
    'who is narayan': lambda: speak("Narayan is the person who created me."),
    'you are ai': lambda: speak("no i am not ai i am just the set of instruction created by  narayan "),
    'what is computer': lambda: speak("computer an electroninc device which proces raw data to giving meaning full information using that program"),
      'who is narayan': lambda: speak("Narayan is the person who created me."),


        'time': lambda: speak(f'Sir, the time is {datetime.datetime.now().strftime("%H:%M:%S")}'),
        'open google': lambda: webbrowser.open('https://google.com'),
        'play music': lambda: os.startfile("C:\\Users\\King\\Desktop\\Jarvis\\jamvanaylaurala.mp3"),
        'shutdown': lambda: shutdown_system(),
        'stop the system': lambda: stop_jarvis(),
        'exit': lambda: stop_jarvis(),
          'can i ask some question': lambda: speak("off course why not what do you wan to know "),
       'tell me about you': lambda: speak("I am jarvis you personal assistant to provide you knowledge and do task execute through voice command "),
        'search in youtube': lambda: search_in_youtube(),
        'tell me a joke': lambda: tell_joke(),
        'search in google': lambda: search_in_google(),
        'open file': lambda: open_file_explorer(),
        'close file': lambda: close_file_explorer(),
        'open command': lambda: open_command_prompt(),
        'close command': lambda: close_command_prompt(),
        'open c drive': lambda: open_c_drive(),
        'open vs code': lambda: open_vs_code(),
        'open camera': lambda: open_camera(),
        'close camera': lambda: close_camera(),
        'who is rajendra': lambda: speak("I don't know but I think he is a graphic designer and he is from Arghakhanchi"), 
        'open facebook': lambda: speak_and_open('https://www.facebook.com', "Opening facebook"),
        'open instagram': lambda: webbrowser.open('https://www.instagram.com'),
        'open chatgpt': lambda: webbrowser.open('https://chat.openai.com'),
        'play the justin bieber song': lambda: j_song(),
        'play the relax song': lambda: play_relaxing_song(),
        'play the sushant kc song': lambda: sushant_kc_song(),
        'play the new nepali latest song': lambda: latest_nepali_song(),
        'play nepali song': lambda: latest_nepali_song(),
        'play neplai music': lambda: latest_nepali_song(),
        'good morning': lambda: good_morning_routine(),
        'good night' : lambda: good_night_routine(),
        'open my youtube channel': lambda: speak_and_open('https://www.youtube.com/@narayanbogati2191', "Opening your YouTube channel."),
        'show my github id': lambda: speak_and_open('https://github.com/Bogatinarayan', "Showing your GitHub profile."),
        'open github': lambda: speak_and_open('https://github.com/', "Opening GitHub."),
        'open my website': lambda: speak_and_open('https://www.narayanbogati.com.np/', "Opening your website."),
        'play the latest nepali news': lambda: news_nepal(),
        'play nepali news': lambda: news_nepal(),
        'play latest news': lambda: play_latest_news(),
          'play english news': lambda: play_latest_news(),
         'remember that': lambda: remember_action(),
        'do you remember anything': lambda: speak("You said me to remember that " + recall_message() if recall_message() else "I don't remember anything right now."),
     
 # this is for my friend detail
    'who is rajendra lamsal': lambda: speak("rajendra full name rajendra lamsal also call raju he is from butwal and email is rajendralamsal12@gmail.com he is intrested in graphic designer "),
    'who is aklesh': lambda: speak("aklesh full name Aklesh yadav he is from kapikvastu "),
    'who is nirdesh': lambda: speak("Nirdesh full name nirdesh shresthas he is from butwal and hava a lot of knowledge about compter"),
    'who is vishal': lambda: speak("Bishal full name Bishal Thapa he is from palpa he is talented person and having skill in all field "),
    'who is akash': lambda: speak("Akash full name akash tharu he is from bardiya nepal and he was also talented person "),
    'who is manish': lambda: speak("Manish full name Manish sanjali he has lot of knowledge including physic,chemistry,math and computer he wnat to make a software engineer"),
  'who is jambheshwar yadav ': lambda: speak("he is from kapilbastu nepal and he complete the 12 class from science faculty"),
    'who is sonu pal ': lambda: speak("He is bachlor running person and hava a lot of business ideas and he i  from kapilbastu"),
     
             

    }


    
    # Check for custom commands
    executed = False
    for command, action in custom_commands.items():
        if command in query:
            action()
            executed = True
            break
    
    # If no custom command is executed, perform a Google search
    if not executed:
        answer = search_google(query)
        if answer:
            print(f"Google search result: {answer}")
            speak(answer)
        else:
            speak("I don't understand, can you tell me again?")

# Shutdown the system function by Narayan for Windows and Linux
def shutdown_system():
    speak("Shutting down the system.")
    if platform == "win32":
        os.system('shutdown /p /f')
    elif platform in ["linux", "linux2", "darwin"]:
        os.system('poweroff')
    sys.exit()

# To stop the Jarvis program
def stop_jarvis():
    speak("Stopping the system. Goodbye, sir.")
    sys.exit()

# Search in YouTube function
def search_in_youtube():
    speak("What do you want to search for on YouTube?")
    search_query = take_command()
    if search_query != "None":
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    else:
        speak("Sorry, I didn't catch that. Please try again.")

# Function to fetch and tell a joke by PyJokes
def tell_joke():
    joke = pyjokes.get_joke()
    print(f"Here's a joke for you: {joke}")
    speak(f"Here's a joke for you: {joke}")

# Function to search in Google and open in a new tab
def search_in_google():
    speak("What do you want to search for on Google?")
    search_query = take_command()
    if search_query != "None":
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open_new_tab(url)
    else:
        speak("Sorry, I didn't catch that. Please try again.")

# Function to open a file specified by the user
def open_file_explorer():
    speak("Opening File Explorer.")
    if platform == "win32":
        os.startfile('explorer.exe')
    else:
        speak("Sorry, I can only open File Explorer on Windows.")

def close_file_explorer():
    speak("Closing File Explorer.")
    if platform == "win32":
        try:
            os.system('taskkill /F /IM explorer.exe')
            print("File Explorer closed successfully.")
            # Restart File Explorer if needed
            os.system('start explorer.exe')
        except Exception as e:
            print(f"Error closing File Explorer: {e}")
            speak("Failed to close File Explorer.")
    else:
        speak("Sorry, I can only close File Explorer on Windows.")

# Function to open the command prompt
def open_command_prompt():
    speak("Opening command prompt.")
    if platform == "win32":
        os.system('start cmd')
    elif platform == "darwin":
        os.system('open -a Terminal')
    elif platform.startswith("linux"):
        os.system('xdg-open terminal')

# Function to close the command prompt
def close_command_prompt():
    speak("Closing command prompt.")
    if platform == "win32":
        try:
            os.system('taskkill /IM cmd.exe /F')
            print("Command Prompt closed successfully.")
        except Exception as e:
            print(f"Error closing Command Prompt: {e}")
            speak("Failed to close Command Prompt.")
    else:
        speak("Sorry, I can only close Command Prompt on Windows.")

# Function to open the C drive
def open_c_drive():
    speak("Opening C drive.")
    if platform == "win32":
        os.system('start C:')
    else:
        speak("Sorry, I can't open C drive on this platform.")


# Function to open Visual Studio Code
def open_vs_code():
    speak("Opening Visual Studio Code.")
    if platform == "win32":
        os.system('code')  # Assumes VS Code is in the PATH
    elif platform == "darwin":
        subprocess.call(['open', '-a', 'Visual Studio Code'])
    elif platform.startswith("linux"):
        subprocess.call(['code'])

# Function to open the camera
def open_camera():
    speak("Opening the camera.")
    cap = cv2.VideoCapture(0)  # 0 is typically the index for the default camera

    if not cap.isOpened():
        speak("Sorry, I couldn't access the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            speak("Failed to grab frame.")
            break

        cv2.imshow('Camera', frame)

        # Press 'q' to close the camera window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to close the camera
def close_camera():
    speak("Closing the camera.")
    # Assuming this will be called in context where the camera is being displayed
    cv2.destroyAllWindows()

# Function to play the relaxing song on YouTube
def play_relaxing_song():
    speak("Playing relaxing song on YouTube.")
    pywhatkit.playonyt("relaxing music")  # This will play the first video that matches "relaxing music" on YouTube

# Function to play the Justin Bieber song on YouTube
def j_song():
    speak("Playing Justin Bieber song on YouTube.")
    pywhatkit.playonyt("Justin Bieber music")  

def sushant_kc_song():
    speak("Playing Sushant KC song.")
    pywhatkit.playonyt("Sushant KC song")  

def latest_nepali_song():
    speak("Playing latest Nepali song for you.")
    pywhatkit.playonyt("nepali latest song")

# Function to play Nepali news
def news_nepal():
    speak("Playing the latest Nepali news.")
    pywhatkit.playonyt("play the latest nepali news")

# Function to fetch weather information
def fetch_weather(city, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            speak(f"The weather in {city} is {weather_description}. The temperature is {temp} degrees Celsius.")
        else:
            speak("Unable to fetch weather information at the moment.")
    except Exception as e:
        speak(f"Error fetching weather information: {str(e)}")

# Function to open the latest news in the browser
def open_latest_news():
    speak("Opening the latest news in the browser.")
    webbrowser.open('https://news.google.com')

# Function to execute the "good morning" routine
def good_morning_routine():
    speak("Good morning! Have a great day ahead.")
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")
    fetch_weather("Butwal", "") 
    play_latest_news()

# Function to play the latest news
def play_latest_news():
    speak("Fetching the latest news for you.", volume=0.5)  # Lower volume
    # Replace 'YOUR_API_KEY' with your actual API key
    url = f"http://newsapi.org/v2/top-headlines?country=us&apiKey="
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        if articles:
            for article in articles[:5]:  # Read out the top 5 articles
                speak(article['title'], volume=0.5)
                speak("Next news.", volume=0.5)
        else:
            speak("Sorry, I couldn't find any news at the moment.")
    else:
        speak("Sorry, I'm unable to fetch the news at the moment.")
    speak("see more in website thank you")
    # Code to turn off the microphone (if applicable)
    # Example: Stop listening or deactivate the voice recognition

# This is for sound for opening 
def speak_and_open(url, message):
    print(f"Opening URL: {url}")
    webbrowser.open(url)
    speak(message)

# This is for good night 
def good_night_routine():
    speak("Good night, sir. Have a wonderful night.")
    # Ask for tomorrow's schedule
    speak("What's the schedule for tomorrow?")
    tomorrow_schedule = take_command()

    # Store tomorrow's schedule in a variable (you can store in a file or database for persistence)
    if tomorrow_schedule != "None":
        schedule_text = f"Ok sir, I will {tomorrow_schedule}. I remain at your service tomorrow."
        print("Tomorrow's schedule:", schedule_text)
        speak(schedule_text)

    pywhatkit.playonyt("good night song")

#this is for test 

def remember_message(rememberMessage):
    try:
        with open('data.txt', 'w') as remember:
            remember.write(rememberMessage)
    except Exception as e:
        print(f"Error saving message: {e}")

def recall_message():
    try:
        with open('data.txt', 'r') as remember:
            remembered_message = remember.read()
            return remembered_message
    except Exception as e:
        print(f"Error recalling message: {e}")
        return None

def remember_action():
    speak("What do you want me to remember, Sir?")
    rememberMessage = take_command()
    remember_message(rememberMessage)


#this is the meaning blcock narayan bogati 

if __name__ == '__main__':
    while True:
        query = take_command()
        if query != "None":
            process_command(query)

