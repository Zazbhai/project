from keras.models import load_model
import numpy as np
import cv2
import requests

classes = ["Ripe", "Unripe"]
model = load_model(r"C:\Users\zgarm\Desktop\Smart_crop\keras_model.h5", compile=False)


threshold = 0.97  

def crop_model(video=r"C:\Users\zgarm\Desktop\Smart_crop\ripe4.mp4"):
    vid = cv2.VideoCapture(video)
    try:
        while True:
            ret, feed = vid.read()
            feed = cv2.resize(feed, (720, 720))

            if not ret:
                print("Video ended. Triggering action...")
                # requests.get("http://192.168.1.12/nofeed")
                break
            image_path = cv2.resize(feed, (224, 224))

            image = cv2.cvtColor(image_path, cv2.COLOR_BGR2RGB)
            image = image /255
            image = np.expand_dims(image, axis=0)

            prediction_probs = model.predict(image)
            max_prob = np.max(prediction_probs)
            predicted_class = classes[np.argmax(prediction_probs)]  

            
            if max_prob >= threshold:
                prediction = predicted_class
            else:
                prediction = "Detecting"  

           
                # requests.get("http://172.20.10.14/uncertain")
                

            cv2.putText(feed, f"Prediction: {prediction}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
            cv2.imshow("Video", feed)
            print(f"Result: {prediction} (Confidence: {max_prob:.2f})")

            key = cv2.waitKey(1)
            if key == 27:
                # requests.get("http://172.20.10.14/nofeed")
                break

        vid.release()

        cv2.destroyAllWindows()
    except Exception as e:
        pass
    finally:
        # requests.get("http://192.168.1.12/nofeed")
        pass


