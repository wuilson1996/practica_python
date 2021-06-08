
import pyautogui, time

time.sleep(6)

while not pyautogui.keyUp("esc"):

	pyautogui.typewrite("te volviste loco")
	pyautogui.press("enter")