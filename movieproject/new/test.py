import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice and properties for the TTS voice over
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 150)  # Set the speaking rate

# Generate the TTS voice over
text = "Hello  everyone,and welcome  to  our  channel   funfactz.   In today's video,   we'll be discussing the top 5 interesting facts about the brain   that you probably didn't know.   So, let's get started."
engine.say(text)
engine.runAndWait()