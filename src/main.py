import cv2


gscale_long = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale_short = '@%#*+=-:. '


def main():
    print("The begginning.")

    cap = cv2.VideoCapture("videos/wallpaper.mkv")

    if (cap.isOpened() == False):
        raise "Something is wrong with the file"

    while(cap.isOpened()):
        ret, frame = cap.read()
        grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # resized = cv2.resize(grayscaled, (960, 540))
        if ret == True:
            frame_w = frame.shape[0]
            frame_h = frame.shape[1]
            cv2.imshow("Frame", grayscaled)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

main()