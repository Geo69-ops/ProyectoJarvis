import playsound
from gtts import gTTS 


from elevenlabs import generate, play, set_api_key



import speech_recognition as sr
import pyttsx3

import os
import pyaudio
import openai
import replicate

from dotenv import load_dotenv

load_dotenv()

#replicate
os.environ["REPLICATE_API_TOKEN"] = "r8_QL07w7CVjVjTsQCIY1tKlK0a9MjTDtK35tiWk"

API_KEY = os.environ.get("API_KEYS_ELEVENLABS")
set_api_key = API_KEY


API_KEY_OPENAI = os.environ.get("APIKEYS_CHAT_GPT")

lang = 'en'
# OPENAI_KEY = os.getenv('OPENAI_KEY')


# OPENAI_KEY = keyy
# openai.api_key = OPENAI_KEY

def get_audio():
        r= sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said= r.recognize_google(audio)
                print(said)

                if "Friday" in said:
                    output = replicate.run("replicate/llama-7b:ac808388e2e9d8ed35a5bf2eaa7d83f0ad53f9e3df31a42e4eb0a0c3249b3165", 
                                           input={"debug": False,
                                                  "top_p": 0.95,
                                                  "prompt": said,
                                                  "max_length": 50,
                                                  "temperature": 0.9,
                                                  "repetition_penalty": 1})

                    # The replicate/llama-7b model can stream output as it's running.
                    # The predict method returns an iterator, and you can iterate over that output.
                    mensaje = "" 
                    for item in output:
                        # https://replicate.com/replicate/llama-7b/api#output-schema
                        print(item, end="")
                        mensaje = mensaje + " " + item

                    # completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0125", messages={"role": "user", "content": said})
                    # text = completion.choices[0].message.content
                    
                    texto = mensaje
                    audio2 = generate(
                         text=texto,
                         voice="Sam",
                         model= 'eleven_multilingual_v1'
                    )

                    # audio2.save("output.wav")
                    
                    play(audio2)

                    speech = gTTS(text=texto, lang=lang, slow=False,tld="com.co")
                    speech.save("welcome.mp3")
                    playsound.playsound("welcome.mp3")
                    os.remove("welcome.mp3")
            except Exception as e:
                print(e)
        return said 




while True:
    get_audio()






# def SpeakText(command):
#     engine= pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()

# r= sr.Recognizer()




# def record_text():
#     while(1):
#         try:
#             with sr.Microphone() as source:
#                 r.adjust_for_ambient_noise(source,duration=0.2)
#                 print ("i'm listening")
                
#                 audio2= r.listen(source)

#                 MyText = r.recognize_google(audio2)
#                 print(MyText)
#                 return MyText
                
            
#         except sr.RequestError as e:
#             print("could not request results; {0}", format(e))
        
#         except sr.UnknownValueError:
#             print("Unknow error ocurred")
# record_text()

# def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
#     response= openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )    

#     message = response.choice[0].message.content
#     messages.append(response.choices[0].message)
#     return message

# messages= []
# while(1):
#     text = record_text()
#     messages.append({"role":"user","content": text})
#     response = send_to_chatGPT(messages)
#     SpeakText(response)

#     print(response)