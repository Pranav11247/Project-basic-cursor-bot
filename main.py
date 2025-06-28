import pyautogui
import pyperclip
import time
from openai import OpenAI


print("You have 5 seconds to place the mouse where needed...")
time.sleep(5)

pyautogui.click(2080, 1723)
# I have my note pad open in this position below it click there and open it up
pyautogui.moveTo(35, 151, duration=0.5)
time.sleep(0.5)

pyautogui.mouseDown()  # press the mouse
pyautogui.moveTo(2600, 1680, duration=1.5)
pyautogui.mouseUp()  # release the mouse

pyautogui.hotkey("ctrl", "c")

time.sleep(0.5)

copied_text = pyperclip.paste()

client = OpenAI(
    api_key="",
    base_url="https://api.sambanova.ai/v1",
)

response = client.chat.completions.create(
    model="Llama-4-Maverick-17B-128E-Instruct",
    messages=[{"role": "user", "content": f"tell me about {copied_text} in one line) "}],
    temperature=0.1,
    top_p=0.1,
)
pyautogui.click(2652,29,duration=0.5)
print(response.choices[0].message.content)
