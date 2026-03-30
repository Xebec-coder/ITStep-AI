import cv2

img = cv2.imread(
    'data/lesson1/Lenna.png',
    cv2.IMREAD_GRAYSCALE
)

mask_1 = cv2.imread(
    'data/lesson1/mask1.png',
    cv2.IMREAD_GRAYSCALE
)
mask_2 = cv2.imread(
    'data/lesson1/mask2.png',
    cv2.IMREAD_GRAYSCALE
)

print(type(img))
print(img)
print(img.shape)
print(img.dtype)

print(type(img))
print(img)
print(img.shape)
print(img.dtype)

masks = cv2.bitwise_or(mask_1, mask_2)
masks = cv2.resize(masks, (500, 500))
mask_1 = cv2.resize(mask_1, (500, 500))
mask_2 = cv2.resize(mask_2, (500, 500))
img = cv2.resize(img, (500, 500))

cv2.imshow('org', img)
mask_img_1 = cv2.bitwise_and(img, masks, mask=mask_1)
mask_img_2 = cv2.bitwise_and(img, masks, mask=mask_2)
mask_img_3 = cv2.bitwise_and(img, masks, mask=masks)

cv2.imshow('mask_1', mask_img_1)
cv2.imshow('mask_2', mask_img_2)
cv2.imshow('masks', mask_img_3)

# cv2.imshow('mask_1', mask_img_1)

cv2.waitKey(0)