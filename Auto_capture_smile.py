import cv2
import mediapipe as mp
import winsound

x1=0
y1=0
x2=0
y2=0
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
camera = cv2.VideoCapture(0)#1 camera so zero
while True:
    _ , image = camera.read()
    image = cv2.flip(image, 1) # flip the image horizontally
    fh, fw, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_image)
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks):
            x=int(landmark.x * fw)
            y=int(landmark.y * fh)
            if id == 61:
                x1=x
                y1=y
            if id == 291:
                x2=x
                y2=y
        dist = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
        print(dist)
        #cv2.putText(image, f"Smile Width: {dist}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.circle(image, (x1, y1), 5, (255, 0, 0), -1)  # Left mouth corner
        cv2.circle(image, (x2, y2), 5, (0, 0, 255), -1)  # Right mouth corner

        if dist>77:
            cv2.imwrite("selfie.jpg", image)
            winsound.PlaySound("BAK.wav", winsound.SND_FILENAME)
            cv2.waitKey(100)
        
        cv2.imshow("Auto selfie for smiling faces using python", image)
    key = cv2.waitKey(100)
    if key == 27: # press escape to exit
        break
camera.release()
cv2.destroyAllWindows()
