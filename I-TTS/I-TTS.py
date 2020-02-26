#INSTALL And IMPORT Neccesary Packages
#OpenCV
import cv2 as cv
#Import Tesseract OCR
import pytesseract
#Import TTS
import pyttsx3
#Import IO Buttons
import keyboard
#Import Camera

#RESTART PROGRAM
def main():
    while True:
        prog()

#MAIN PROGRAM
def prog():
    #CAMERA
    cap = cv.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('IP_PROTOTYPE', gray)
        if not ret:
            break
        k = cv.waitKey(1)
        #Press ESC = Exit/Use again the image after TTS
        if k == 27:
            break
        #Press SPACE = Capture Image
        elif k == 32:
            cv.imwrite('\nimage.jpg', gray)
            print('Captured Image!')
            break

    cap.release()
    cv.destroyAllWindows()

    # IMAGE TO TEXT
    print('\nPreprocessing Image...')

    def itt():
        # Preprocess Image
        img = cv.imread(r'image.jpg', 0)
        cv.imshow('Image', img)
        cv.waitKey(1)
        cv.destroyAllWindows()

        # IMAGE TO TEXT
        # OCR Directory
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        return pytesseract.image_to_string('image.jpg'
                                           )
    def tts():
        # TEXT TO SPEECH
        print('\n===TEXT===')
        print(f'\n{itt()}')
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)

        engine.say(itt())
        engine.runAndWait()

    while True:
        tts()



if __name__ == "__main__":


    main()
