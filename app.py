import cv2
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, Response
import atexit
import threading

app = Flask(__name__)

# Load the trained model at the start
model = tf.keras.models.load_model('model/sign_language_model.keras')

# Initialize video capture
cap = cv2.VideoCapture(0)

# Release the video capture on exit
def release_cap():
    cap.release()

atexit.register(release_cap)

# Define a function to preprocess the frames
def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28))
    normalized = resized / 255.0
    reshaped = np.reshape(normalized, (1, 28, 28, 1))
    return reshaped

# Define a function to get the label from the model's prediction
def get_label(prediction):
    class_names = list('ABCDEFGHIKLMNOPQRSTUVWXY')  # Exclude 'J' and 'Z' due to motion
    return class_names[np.argmax(prediction)]

# Generate frames from the webcam
def generate_frames():
    while True:
        try:
            success, frame = cap.read()
            if not success:
                break
            processed_frame = preprocess_frame(frame)
            prediction = model.predict(processed_frame)
            label = get_label(prediction)
            cv2.putText(frame, label, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            print(f"Error: {e}")
            break

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()

