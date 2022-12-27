from logging import captureWarnings
import cv2 as cv

# img = cv.imread('cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)
# reading videos


# rescaling function
def rescaleFrame(frame, scale=0.75):
    # works for both images and videos and live videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # works for live videos
    capture.set(3, width)
    capture.set(4, height)
# only for videos


capture = cv.VideoCapture('flowers.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resized)
    # it breaks when d key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# after the video is done playing, it will show -215 assertion error
# which basically means that opencv could not find the video frame or img at the given path
# for a video it ran out of frames so it
