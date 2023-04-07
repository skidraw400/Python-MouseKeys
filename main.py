import pyautogui
from pynput.keyboard import Key, Listener

shift = False
r_control = False

def movement(slow, fast, dir):
    size = 50
    if fast:
        size = 200
    if slow:
        size = 5
    match dir:
        case 0:
            pyautogui.moveRel(-size, 0)
        case 1:
            pyautogui.moveRel(0, -size)
        case 2:
            pyautogui.moveRel(size, 0)
        case 3:
            pyautogui.moveRel(0, size)

def on_press(key):
    global r_control, shift
    # print('{0} pressed'.format(
    #     key))
    match key:
        case Key.ctrl_r:
            r_control = True
            if shift:
                pyautogui.click()
        case Key.shift_r:
            shift = True
        case Key.left:
            movement(shift, r_control, 0)
        case Key.up:
            movement(shift, r_control, 1)
        case Key.right:
            movement(shift, r_control, 2)
        case Key.down:
            movement(shift, r_control, 3)
        case Key.menu:
            pyautogui.click(button='right')

def on_release(key):
    global r_control, shift
    match key:
        case Key.ctrl_r:
            r_control = False
        case Key.shift_r:
            shift = False
        case Key.esc:
            if r_control == True:
                return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()