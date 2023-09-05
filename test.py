import JarvisAI
import re

obj = JarvisAI.JarvisAssistant()

def t2s(text):
    obj.text2speech(text)

def start():
    while True:
        print("Say your AI name to activate")
        status, command = obj.hot_word_detect()
        print(status, command)
        if status:
            while True:
                # use any one of them
                print("Continue listening, say- 'stop listening to stop continue listening'")
                res = obj.mic_input()
                # res = obj.mic_input_ai(debug=True)
                res = res.lower()
                print("You said: " + res)

                if re.search("jokes|joke|Jokes|Joke", res):
                    joke_ = obj.tell_me_joke('en', 'neutral')
                    print(joke_)
                    t2s(joke_)

        else:
            continue


if __name__ == "__main__":
    if not os.path.exists("configs/config.ini"):
        print(os.listdir())
        res = obj.setup()
        if res:
            print("Settings Saved. Restart your Assistant")
    else:
        start()
