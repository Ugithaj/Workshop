
from gtts import gTTS

# enter text-to-speech
my_text = input(' Enter text-to-speech:\n > ')

tts = gTTS(text=my_text, lang='en', slow=False)
tts.save('converted-file.mp3')   # save file as ... (here saving as mp3)


print("\n [ Done! ]")


# exit
input('\n'*2 + ' [!] Hit enter to exit...')
