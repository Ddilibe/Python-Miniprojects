#!/bin/usr/env python3
"""
    Whisper

    Whisper is an automatic speech recongnition system which is used to transcribe and translate audio data into text format. 
    It use a wide range of language ranging from english to french and others.
    One advantage of whisper is it can be used as a command line program and it can be import in a script to be initialiatedi.

"""
"""
    Testing and using Whisper
"""

"""
    To get started
        pip install git+https://github.com/openai/whisper.git 
"""
import whisper
"""
    Whisper has 5 models on which it can be used to trnasscribe an audio to text.
    They include tiny, base, small, meduim, large. 
    Each of them in heirachy of arccuracy and computing power.
    The model, tiny will be less acurrate but a lot fast while the model large will be more arcurate but less fast.
    
    The load_model function is used to load a prefereable model of your choice
    Each depending on the device and the length in time you would want it to work out.
"""
model = whisper.load_model("base")
"""
    The load function is used to import the audio which would be used to make the animation
"""

audio = whisper.load_audio("audio_file.mp3")
audio = whisper.pad_or_trim(audio)
mel = whisper.log_mel_spectrogram(audio).to(model.device)

"""
    The detect_language  function is used to detect the language of the audio input
"""
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

"""
    the decode function is ued to decode the audio into text
"""
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)
"""
    Print the text generated from the audio
"""
print(result.text)
