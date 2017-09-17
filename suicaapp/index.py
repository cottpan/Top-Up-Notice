from bottle import route, run, template
import cv2
import numpy as np

#最低初乗り賃金
threshold_keio = 124
threshold_jr_east = 133
threshold_metro = 165

#数字画像セレクト
def num_select(number):
    if int(number) == 0:
        return "./0.png"
    if int(number) == 1:
        return "./1.png"
    if int(number) == 5:
        return "./5.png"


##API
# →http://(ip_address):8080/api/*　にリクエスト(*：残高)
# →残高と乗れる路線のポップアップ表示

@route('/api/<balance:int>')
def ring_app(balance):
    #ベース画像
    notice_img = cv2.imread("./notice.png")
    
    #通知用Yes/No画像
    ng_img = cv2.imread("./ng.png")
    ok_img= cv2.imread("./ok.png")
    
    #画像サイズ
    height, width = notice_img.shape[:2]

    #乗れる路線の表示
    if(balance < threshold_keio):
        notice_img[332:413, 423:732,0:3] = ng_img
    else:
        notice_img[332:413, 423:732,0:3] = ok_img
    if(balance < threshold_jr_east):
        notice_img[400:481, 423:732,0:3] = ng_img
    else:
        notice_img[400:481, 423:732,0:3] = ok_img
    if(balance < threshold_metro):
        notice_img[470:551, 423:732,0:3] = ng_img
    else:
        notice_img[470:551, 423:732,0:3] = ok_img

    #残高の表示
    zandaka_str = str(balance)
    zandaka_list = list(zandaka_str)
    pos = 0
    for char in zandaka_list:
        num_img = cv2.imread(num_select(char))
        notice_img[217:292, (557+pos*50):(632+pos*50),0:3] = num_img
        pos += 1

    #ポップアップの生成
    cv2.imshow("Api",notice_img)
    #キー入力待ち
    cv2.waitKey(0)
    #ウインドウ破棄
    cv2.destroyAllWindows()

##    color_img = np.zeros(((int)(height/2), width, 3), np.uint8)
##    color_img[:,:,0] = 255
##    color_img[:,:,1] = 0
##    color_img[:,:,2] = 128

##    while True:
##        hsv_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
##        hsv_img[:,:,0] += 1
##        #color_img[:,:,0] += 1
##        #color_img[:,:,1] += 1
##        #color_img[:,:,2] += 1
##        color_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
##        notice_img[0:(int)(height/2), 0:width, 0:3] = notice_img[0:(int)(height/2), 0:width, 0:3]+color_img
##        cv2.imshow("Test",notice_img)
##        c = cv2.waitKey(200)
##        if c == 13:
##            break
##    cv2.destroyAllWindows()
    
@route('/api/test22')
def ring_app2():
    img = cv2.imread("./test2.png")
    cv2.imshow("Test2", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

run(host='0.0.0.0', port=8080)
