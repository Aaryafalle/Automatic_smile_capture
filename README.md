✅ Prerequisites
Before running the program, make sure the following Python libraries are installed:
pip install opencv-python
pip install mediapipe
If you're using sound alerts (like BAK.wav), also ensure you're on Windows, since the winsound module is built-in for Windows only.

You’ll also need:
A working webcam

Python 3.7 or higher
# Automatic_smile_capture
📸 Smile-Based Selfie Capture – How It Works
This Python program uses your webcam and Mediapipe's FaceMesh to detect your face in real time. It tracks two specific landmark points on the corners of your mouth — points 61 (left) and 291 (right).

🧠 Facial Landmarks Detection:

Mediapipe scans your face and finds 468 facial landmarks.

Landmark 61 is on the left corner of the mouth, and 291 is on the right corner.
 
When you smile, this distance increases, because your mouth stretches wider.

📸 Automatic Selfie & Sound:

If the distance crosses a certain threshold (e.g., 70 pixels), it means you're smiling.

The program saves a photo and plays a sound (BAK.wav) to notify you.

🔁 Runs Continuously:

It keeps checking for your smile in real time.

You can press Esc to exit the program.
