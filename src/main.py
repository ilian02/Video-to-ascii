import cv2
import numpy as np
import sys
import time

gscale_long = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale_short = '@%#*+=-:. '


def frame_to_ascii(frame, gscale=gscale_short, width=100):
    """Converts an OpenCV frame to ASCII art."""
    height, original_width = frame.shape[:2]
    aspect_ratio = height / original_width
    new_height = int(aspect_ratio * width * 0.55)
    resized_frame = cv2.resize(frame, (width, new_height))
    
    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    
    normalized = (gray_frame / 255) * (len(gscale) - 1)
    ascii_art = np.array([gscale[int(val)] for val in normalized.flatten()])
    
    ascii_art = ascii_art.reshape(new_height, width)
    return "\n".join(["".join(row) for row in ascii_art])


def display_ascii(ascii_art):
    """Displays ASCII art efficiently by repositioning the cursor."""
    sys.stdout.write("\033[H" + ascii_art + "\n")
    sys.stdout.flush()


def videoToAscii(filename, gscale):

    cap = cv2.VideoCapture(filename)

    if (cap.isOpened() == False):
        raise "Something is wrong with the file"

    while(cap.isOpened()):
        ret, frame = cap.read()
        ascii_art = frame_to_ascii(frame, gscale, 100)
        if ret == True:
            time.sleep(0.2)
            display_ascii(ascii_art)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()



def main():
    print("The begginning.")
    videoToAscii("videos/hand.mp4", gscale_long)

main()