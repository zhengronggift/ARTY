import os

# Begin of For Loop - Run three times
for x in range(0, 3):
    # Play Alarm_fade_out.wav first
    os.system("aplay /home/pi/Music/Alarm_fade_out.wav")
    # Play preset text-to-speech
    os.system("espeak -ven+f5 -s150 'Attention, this is a rescue device! Hold on to the handles' 2>/dev/null")
