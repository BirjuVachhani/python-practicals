import time
import webbrowser

print('Welcome to "Take A Break" story.\n\nTo start timer...')
time_interval = float(input('Enter time interval in minutes: '))
break_interval = float(input('Enter break time interval in minutes: '))
favorite_video = input('Enter URL of your favourite video to play at break time: ')
print('\nTo stop timer, press ctrl+c on CMD..\nTimer Started...')
while(True):
    print("It's work time!")
    print('Working...')
    time.sleep(time_interval*60)
    print("It's break time!\nPlaying yor favorite video...")
    webbrowser.open(favorite_video)
    time.sleep(break_interval*60)
    print('Break time over!')