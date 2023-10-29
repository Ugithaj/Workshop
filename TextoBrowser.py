from flask import Flask, request, send_file
from gtts import gTTS
import tempfile

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]

        # Use gTTS to convert text to speech
        tts = gTTS(text, lang="en")
        #temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
        #tts.save(temp_file.name)
        tts.save('converted-file.mp3')

        return f"""
        <html>
        <body>
        <h1>Text to Speech Conversion</h1>
        <p>Input Text:</p>
        <p>{text}</p>
        <audio controls>
            <source src="{'converted-file.mp3'}" type="audio/mpeg">
         </audio>
        </body>
        </html>
        """
    else:
        return """
        <html>
        <body>
        <h1>Text to Speech Conversion</h1>
        <form method="POST">
            <label for="text">Enter text to convert to speech:</label><br>
            <textarea name="text" rows="4" cols="50"></textarea><br><br>
            <input type="submit" value="Submit">
        </form>
        </body>
        </html>
        """

if __name__ == "__main__":
    app.run()
