from pygame import mixer

mixer.init()

mixer.music.set_volume(0.9)
mixer.music.load("dom.mp3")
mixer.music.play()



while True:

    print("WCIŚNIJ 'p' żeby zatrzymać \n WCIŚNIJ 'w' żeby wznowić")
    print("Aby wyjść wpisz 'opuszczanie'")

    wybor = input("  ")

    if wybor == 'p':

        # Pausing the music
        mixer.music.pause()
    elif wybor == 'w':

        # Resuming the music
        mixer.music.unpause()
    elif wybor== 'opuszczanie':

        # Stop the mixer
        mixer.music.stop()
        break
