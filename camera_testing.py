import pyautogui as pya
import pydirectinput as pdi
import subprocess, time, os

def find_and_click(img_path):
    """ finds the image and clicks it 
    returns the location"""
    imgLocation = pya.locateOnScreen(img_path, confidence = 0.6) 
    #print(imgLocation) 
    imgLocation = pya.center(imgLocation)
    pdi.click(imgLocation[0],imgLocation[1])
    return imgLocation

# opens camera
subprocess.run('start microsoft.windows.camera:', shell=True)
time.sleep(2)
screen = pya.size()
pdi.click(int(screen[0]/2),int(screen[1]/2)) #gets rid of the text that may block the video icon
time.sleep(1)
pya.FAILSAFE = True
video_selected_path = "video_selected.png"
video_not_selected_path = "video_not_selected.png"
stop_recording_path = "stop_video.png"

# check to see if the video option is selected
try:
    if pya.locateOnScreen(video_not_selected_path,confidence = 0.6) != None:
        find_and_click(video_not_selected_path)
except:
    print("Video already selected!")

# start recording
time.sleep(0.5)
start_time = time.strftime("WIN_%Y%m%d_%H_%M_%S_Pro")
find_and_click(video_selected_path)
print(start_time)

# get start time +- 1 sec for file identification later
if int(start_time[-5]) != 0 and int(start_time[-5]) != 9:
    start_time_plus_1sec = start_time[:-5] + str(int(start_time[-5]) + 1) + start_time[-4:]
    start_time_minus_1sec= start_time[:-5] + str(int(start_time[-5]) - 1) + start_time[-4:]
elif int(start_time[-5]) == 0:
    start_time_plus_1sec = start_time[:-5] + str(int(start_time[-5]) + 1) + start_time[-4:]
    start_time_minus_1sec = start_time[:-5] + str(9) + start_time[-4:]
    start_time_minus_1sec = start_time_minus_1sec[:-6] + str(int(start_time_minus_1sec[-6]) - 1) + start_time_minus_1sec[-5:]
elif int(start_time[-5]) == 9:
    start_time_plus_1sec = start_time[:-5] + str(0) + start_time[-4:]
    start_time_plus_1sec = start_time_plus_1sec[:-6] + str(int(start_time_plus_1sec[-6]) + 1) + start_time_plus_1sec[-5:]
    start_time_minus_1sec= start_time[:-5] + str(int(start_time[-5]) - 1) + start_time[-4:]

#length of video
time.sleep(5)

# stop recording
find_and_click(stop_recording_path)
homedir = os.path.expanduser("~")
print(os.path.exists(f"{homedir}/Pictures/Camera Roll/{start_time}.mp4") or os.path.exists(f"{homedir}/Pictures/Camera Roll/{start_time_plus_1sec}.mp4") or os.path.exists(f"{homedir}/Pictures/Camera Roll/{start_time_minus_1sec}.mp4"))


subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)

#rename the video to whatever
new_name = "test_video"
if os.path.exists(f"{homedir}/Pictures/Camera Roll/{start_time}.mp4"):
    os.rename(f"{homedir}/Pictures/Camera Roll/{start_time}.mp4",f"{homedir}/Pictures/Camera Roll/{new_name}.mp4")
elif os.path.exists(f"{homedir}/Pictures/Camera Roll/{start_time_plus_1sec}.mp4"):
    os.rename(f"{homedir}/Pictures/Camera Roll/{start_time_plus_1sec}.mp4",f"{homedir}/Pictures/Camera Roll/{new_name}.mp4")
elif os.path.exists(f"{homedir}/Pictures/Camera Roll/{start_time_minus_1sec}.mp4"):
    os.rename(f"{homedir}/Pictures/Camera Roll/{start_time_minus_1sec}.mp4",f"{homedir}/Pictures/Camera Roll/{new_name}.mp4")

print("File created and renamed:", os.path.exists(f"{homedir}/Pictures/Camera Roll/{new_name}.mp4"))
os.remove(f"{homedir}/Pictures/Camera Roll/{new_name}.mp4")
print("file deleted")