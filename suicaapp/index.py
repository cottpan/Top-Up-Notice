from bottle import route, run, template
import cv2

@route('/api/test1', method='GET')
def ring_app():
    img = cv2.imread("./test1.png")
    cv2.imshow("Test", img)
    cv2.waitKey(0)

@route('/api/test2', method='GET')
def ring_app():
    cv2.img = imread("./test2.png")
    cv2.imshow("Test", img)
    cv2.waitKey(0)

run(host='localhost', port=8080)
