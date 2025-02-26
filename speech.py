from gtts import gTTS
from pydub import AudioSegment

f = open("story.txt", "r")

mytext = f.read()


# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("story.mp3")