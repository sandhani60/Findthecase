import cv2
import os
import pickle

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize variables to store face details
face_details = {}

n = int(input("Enter 1 to store the values or 0 to retrieve the values: "))

if n == 1:
    def capture_faces(name):
        global face_details

        # Initialize the webcam
        cap = cv2.VideoCapture(0)

        # Check if the directory exists, if not create one
        if not os.path.exists('dataset'):
            os.makedirs('dataset')

        # Create a directory for the person if not exists
        person_dir = os.path.join('dataset', name)
        if not os.path.exists(person_dir):
            os.makedirs(person_dir)

        face_id = 0

        while True:
            # Read the frame
            ret, frame = cap.read()

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the faces and capture images
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

                # Save the captured face in the dataset directory
                face_id += 1
                cv2.imwrite(os.path.join(person_dir, str(face_id) + ".jpg"), gray[y:y+h, x:x+w])

                # Update face_details
                if name not in face_details:
                    face_details[name] = []
                face_details[name].append(face_id)

            # Display the frame
            cv2.imshow('Capture Faces', frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close OpenCV windows10
        
        cap.release()
        cv2.destroyAllWindows()

        # Save face details using pickle
        with open('face_details.pkl', 'wb') as f:
            pickle.dump(face_details, f)

    def main():
        # Input name of the person
        name = input("Enter the name of the person: ")
        age=int(input("enter the age"))
        place=input("enter the place")
        capture_faces(name)

    if __name__ == "__main__":
        main()
else:
    def display_images(name):
        # Iterate over the 'dataset' directory
        for root, dirs, files in os.walk('dataset'):
            for dirname in dirs:
                if dirname == name:
                    person_dir = os.path.join(root, name)
                    print("Displaying images for", name)
                    # Iterate over the images in the person's directory
                    for filename in os.listdir(person_dir):
                        if filename.endswith('.jpg'):
                            img_path = os.path.join(person_dir, filename)
                            img = cv2.imread(img_path)

                            # Overlay text (person's name) on the image
                            font = cv2.FONT_HERSHEY_SIMPLEX
                            bottom_left_corner = (10, img.shape[0] - 10)
                            font_scale = 0.5
                            font_color = (255, 255, 255)
                            line_type = 1
                            cv2.putText(img, name, bottom_left_corner, font, font_scale, font_color, line_type)

                            # Display the image with the overlaid text
                            cv2.imshow('Image', img)
                            cv2.waitKey(1000)  # Display each image for 1 second

                    cv2.destroyWindow('Image')  # Close the window after displaying all images for a person

    def main():
        # Input name of the person
        name = input("Enter the name of the person to retrieve details: ")
        display_images(name)

    if __name__ == "__main__":
        main()
