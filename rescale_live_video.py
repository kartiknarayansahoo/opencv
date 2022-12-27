import cv2 as cv


def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture(0)
changeRes(1280, 720)
while True:
    isTrue, frame = capture.read()
    # changeRes(1280, 720)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
