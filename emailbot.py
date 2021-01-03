import smtplib
# smtplib mean simple mail transfer protocal """
#""" next step is to create a server,server acts like a middle person betweeen the sender and rhe smtplib"""
from email.message import EmailMessage
def send_email(receiver,subject,body) : 
    with smtplib.SMTP(host ="smtp.gmail.com",port=587) as server :
        #""" smtp.gmail.com is the server name,and port is like the door no"""
        server.starttls() 
        #"""it mean that we are saying the server that i am secure ,you can trust me"""
        #""" TLS mean transfer layer security,we are saying server to start the transfer layer"""
        server.login("angajalaanuradha@gmail.com","8688136687") 
        #"""saying the server ,who we are"""
        #server.sendmail("angajalaanuradha@gmail.com","angajalasaisri2000@gmail.com","hello how are you...") 
        #sendmail takes 3 arguments sender mail addresss,recevier mail address,and message..
        #thats it ..Note in this mail ther is no subject..
        email = EmailMessage()
        email['From'] = "angajalaanuradha@gmail.com"
        email['To']   =  receiver
        email['Subject'] = subject
        email.set_content(body)
        server.send_message(email)
        #here message is the whole email.
        print("Email sent successfully")
import speech_recognition as sr
listener = sr.Recognizer()
#this lestens whatever the we say..
def get_info() :

    try :
        with sr.Microphone() as source :
            print("listening....")
            voice = listener.listen(source)
            #we are making listener to listen whatever the source say that is the microphone...
            info = listener.recognize_google(voice)
            #we are converting the ausdio heard into text using the google API..
            print(info)
            return info.lower()

    except :
        pass

email_list = {
              "pinky"  : 'angajalasaisri2000@gmail.com'  ,
              'yamuna' : 'yamunaangajala8@gmail.com' ,
              'charan' : 'angajalaanuradha@gmail.com',
              'ram'    : '2019med1003@iitrpr.ac.in' ,
            }
  
import pyttsx3
def talk(text) :
     engine = pyttsx3.init()
     engine.say(text) 
     engine.runAndWait()  
def get_email_info() :
    talk("To whom you want to send the mail")
    name = get_info() 
    #calling the get info function inorder to get the receivers name..note that it is not the valid emailaddress,
    # so using dictonary we assign corresponding email adresss as value to his name ..
    receiver = email_list[name]
    print(receiver)
    talk("What is the subject of the Emial")
    subject = get_info()
    #getting the subject of the email using get_info function..
    talk("Tell me the body of the email")
    body = get_info()
    #getting the body of the email using get_info function..
    send_email(receiver,subject,body)
    talk("do you want to send another email")
    choice = get_info()
    print(choice)
    if choice in ['yes','s'] :
        get_email_info()

get_email_info()