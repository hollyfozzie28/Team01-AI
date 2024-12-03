import os
import azure.cognitiveservices.speech as speechsdk

speechKey= "4alzY2lwO0P9pCiwImOxviVclpiJ5poCBTtEC5EEUAaXLlb8ehomJQQJ99ALACmepeSXJ3w3AAAYACOG0HxR"
speechRegion= "uksouth"

def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=speechKey, region=speechRegion)
    speech_config.speech_recognition_language="en-US"
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        text = speech_recognition_result.text
        print("Recognized: {}".format(text))
        return(text)
    else:
        return "error"








