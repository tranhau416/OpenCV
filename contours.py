import cv2 as cv
import numpy as np

img = cv.imread('Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray,125, 255, cv.THRESH_BINARY) # ret: ngưỡng, thresh: image
# cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

black = np.zeros(img.shape, dtype='uint8')
# cv.imshow("Black", black)

cv.drawContours(black, contours, -1, (0,0,255),1)
cv.imshow('Contours draw', black)


cv.waitKey(0)
#một đường cong liên kết toàn bộ các điểm liên tục (dọc theo đường biên) mà có cùng màu sắc hoặc giá trị cường độ
# image : hình ảnh cần tìm biên, là ảnh nhị phân.
# contours : lưu trữ các đường biên tìm được, mỗi đường biên được lưu trữ dưới dạng một vector của các điểm.
# hierarchy :  chứa thông tin về hình ảnh như số đường viền, xếp hạng các đường viền theo kích thước, trong ngoài, ..
# mode :
# CV_RETR_EXTERNAL : khi sử dựng cờ này nó chỉ lấy ra những đường biên bên ngoài, nhưng biên bên trong của vật thể bị loại bỏ.
# CV_RETR_LIST : Khi sử dụng cờ này nó lấy ra tất cả các đường viền tìm được.
# CV_RETR_CCOMP : khi sử dụng cờ này nó lấy tất cả những đường biên và chia nó làm 2 level, những đường biên bên ngoài đối tượng, và những đường biên bên trong đối tượng.
# CV_RETR_TREE : khi sử dụng cờ này nó lấy tất cả các đường biên và tạo ra một hệ thống phân cấp đầy đủ của những đường lồng nhau.
# method :
# CV_CHAIN_APPROX_NONE : sử dụng cờ này sẽ lưu trữ tất cả các điểm của đường viền .
# CV_CHAIN_APPROX_SIMPLE : nó sẽ nén đường viền trước khi lưu trữ, nén phân đoạn theo chiều ngang, chiều dọc và chéo . Ví dụ : một hình chữ nhật sẽ được mã hoá bằng toạ độ của 4 đỉnh.
# CV_CHAIN_APPROX_TC89_L1 or CV_CHAIN_APPROX_TC89_KCOS :  Áp dụng thuật toán xấp xỉ Teh-Chin.

