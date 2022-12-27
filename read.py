from logging import captureWarnings
import cv2 as cv

# img = cv.imread('cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)
# reading videos


capture = cv.VideoCapture('flowers.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    # it breaks when d key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# after the video is done playing, it will show -215 assertion error
# which basically means that opencv could not find the video frame or img at the given path
# for a video it ran out of frames so it
