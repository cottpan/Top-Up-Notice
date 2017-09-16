from bottle import route, run, template
import cv2

@route('/api/test1')
def ring_app():
    img = cv2.imread("./test1.png")
    cv2.imshow("Test1", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
@route('/api/test2')
def ring_app2():
    img = cv2.imread("./test2.png")
    cv2.imshow("Test2", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

run(host='0.0.0.0', port=8080)
 
