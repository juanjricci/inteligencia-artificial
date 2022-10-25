import cv2
import matplotlib.pyplot as plt

expressions = ['angry', 'happy', 'joy', 'sad', 'serious_closed', 'serious', 'surprised', 'worried']

for exp in expressions:

    image = cv2.imread(f'images/persona1/{exp}.jpg')

    width = 80
    height = 96
    dim = (width, height)

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # resize image
    resized = cv2.resize(grey, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)
    cv2.imwrite(f'images/persona1/{exp}.jpg', resized)
    #cv2.imshow("Resized image", resized)
    # plt.imshow(resized)
    # plt.show()