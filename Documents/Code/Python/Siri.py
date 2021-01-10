import speech_recognition
import gtts #noi
import os #doc ghi file
import pyttsx3
from datetime import date , datetime #ngaygio



#Listening
while True:
    robot_brain = ""
    robot_ear= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("AI Listening: ")
        audio = robot_ear.record(mic, duration= 5) #sau 5s sẽ tự động đóng mic
        print("\nAI:")
    try:
        you = robot_ear.recognize_google(audio, language=" ")
        print("\n User: " + you)
    except:
        robot_brain = "I don't understand!!!"
        print("\n AI: " + robot_brain)

    #Understand
    if you == "":
        robot_brain = "Try again please ..."
    elif you =="hello":
        robot_brain = "Hi Trung"
    elif "today" in you:
        today = date.today()
        robot_brain=today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain=today.strftime("%H Hours %M minutes %S Seconds")
    elif "bye" in you:
        robot_brain="Bye Trung"
        robot_mouth = pyttsx3.init()
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else: 
        robot_brain="Thanks!"
    print("\n AI:" + robot_brain)

#Talking
robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

