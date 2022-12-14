# cv2  نستدعي المكتبه  لتعطينا جميع الوظائف  لتسمح لنا بتحويل الصور 
import cv2
#imread لقراءة الصور التي تريد تعديل لونها نحتاج خاصية 
originalImage = cv2.imread(r'CodeRk\Tkinter\achraf.jpg')
# تحكم في لون 
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 #عرض الصوره 
cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('Original image',originalImage)
cv2.imshow('Gray image', grayImage)

#لمنع الانتضار وعرضها عند ضغط اي زر من ازرار
cv2.waitKey(0)
#لازالة نوافذ السابقا
cv2.destroyAllWindows()
