import cv2
import mysql.connector
import os

# Connect to MySQL database
conn = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_username",
    password="your_mysql_password",
    database="your_database_name"
)
cursor = conn.cursor()

# Create a table to store face details if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS faces
             (id INT AUTO_INCREMENT PRIMARY KEY,
              name VARCHAR(255) NOT NULL,
              age INT,
              address VARCHAR(255),
              image_path VARCHAR(255) NOT NULL)''')
conn.commit()

# Function to add a face and its details to the database
def add_face_to_database(name, age, address, image_path):
    sql = '''INSERT INTO faces (name, age, address, image_path) VALUES (%s, %s, %s, %s)'''
    val = (name, age, address, image_path)
    cursor.execute(sql, val)
    conn.commit()

# Function to recognize face and retrieve details
def recognize_face():
    # Initialize face recognizer (you may need to install OpenCV's face recognition module)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # You need to have this XML file

    # Initialize video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Loop through detected faces
        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Recognize face and retrieve details from the database
            # Assuming you have a function get_details_from_database() that retrieves details from the database based on the recognized face
            details = get_details_from_database(frame[y:y+h, x:x+w]) # Pass the detected face region to the function

            # Display the retrieved details
            print(details) # You can modify this to display details on a GUI window or elsewhere

        # Display the resulting frame
        cv2.imshow('Face Recognition', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

# Example function to retrieve details from the database
def get_details_from_database(face_image):
    # In this example, we'll just print the details associated with the recognized face
    # You would replace this with code to query your database and retrieve the details
    # Assuming you have stored the face images and details in the database already
    # You would need to implement the logic to match the recognized face with the stored faces in the database
    # And retrieve the corresponding details
    return "Details: Name - John Doe, Age - 30, Address - 123 Main Street"

# Main function
if __name__ == "__main__":
    # Add some example faces to the database
    add_face_to_database("John Doe", 30, "123 Main Street", "john_doe.jpg")
    add_face_to_database("Jane Smith", 25, "456 Oak Avenue", "jane_smith.jpg")

    # Start face recognition
    recognize_face()
