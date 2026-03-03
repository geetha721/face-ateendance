import cv2
import os

name = input("Enter person name: ")
save_path = f"dataset/{name}"

if not os.path.exists(save_path):
    os.makedirs(save_path)

cap = cv2.VideoCapture(0)
count = 0

print("Press S to save image, Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Faces", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        img_name = f"{save_path}/{name}_{count}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Saved {img_name}")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

