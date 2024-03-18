import copy
import json
from llama_cpp import Llama


from elevenlabs import generate, play, set_api_key

import speech_recognition as sr
import pyttsx3

import os
import pyaudio
# import openai
import replicate

from dotenv import load_dotenv

load_dotenv()



lang = 'en'
# OPENAI_KEY = os.getenv('OPENAI_KEY')


# OPENAI_KEY = keyy
# openai.api_key = OPENAI_KEY

def get_audio():
        r= sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said= r.recognize_google(audio)
                print(said)

                if "Friday" in said:

                    # Send to Replicate (paying)
                    # output = replicate.run("replicate/llama-7b:ac808388e2e9d8ed35a5bf2eaa7d83f0ad53f9e3df31a42e4eb0a0c3249b3165", 
                    #                        input={"debug": False,
                    #                               "top_p": 0.95,
                    #                               "prompt": said,
                    #                               "max_length": 50,
                    #                               "temperature": 0.9,
                    #                               "repetition_penalty": 1})



                    # The replicate/llama-7b model can stream output as it's running.
                    # The predict method returns an iterator, and you can iterate over that output.
                    
                    # mensaje = "" 
                    # for item in output:
                    #     # https://replicate.com/replicate/llama-7b/api#output-schema
                    #     print(item, end="")
                    #     mensaje = mensaje + " " + item

                    #   texto = mensaje
                    # audio2 = generate(
                    #      text=texto,
                    #      voice="Sam",
                    #      model= 'eleven_multilingual_v1'
                    # )
                    
                    print ("loading model...")
                    # "./models/ggml-vicuna-13b-4bit-rev1.bin""
                    llm= Llama(model_path= "./llama.cpp/models/dolphin-2.2.1-mistral-7b.Q5_0.gguf")
                    print("model loaded")

                    print("Running model...")
                    stream = llm(
                        "Question: {said} Answer:",
                        max_tokens=100,
                        stop=["\n", "Question:", "Q: "],
                        stream=True,
                    )

                    for output in stream:
                        completionFragment = copy.deepcopy(output)
                        print(completionFragment["choices"][0]["text"])

                    # completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0125", messages={"role": "user", "content": said})
                    # text = completion.choices[0].message.content
                    
                  

                    # audio2.save("output.wav")
                    
                    # play(audio2)

                    # speech = gTTS(text=texto, lang=lang, slow=False,tld="com.co")
                    # speech.save("welcome.mp3")
                    # playsound.playsound("welcome.mp3")
                    # os.remove("welcome.mp3")
            except Exception as e:
                print(e)
        return said 




while True:
    get_audio()




def alpaca(qq):
    print ("loading model...")
    # "./models/ggml-vicuna-13b-4bit-rev1.bin""
    llm= Llama(model_path= "./llama.cpp/models/dolphin-2.2.1-mistral-7b.Q5_0.gguf")
    print("model loaded")

    print("Running model...")
    stream = llm(
        "Question: {qq} Answer:",
        max_tokens=100,
        stop=["\n", "Question:", "Q: "],
        stream=True,
    )

    for output in stream:
        completionFragment = copy.deepcopy(output)
        print(completionFragment["choices"][0]["text"])

