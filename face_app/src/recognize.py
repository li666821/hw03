import face_recognition
import os

def load_known_faces(folder="data/known_faces"):
    known_encodings = []
    known_names = []

    for file in os.listdir(folder):
        img_path = os.path.join(folder, file)
        image = face_recognition.load_image_file(img_path)
        enc = face_recognition.face_encodings(image)

        if enc:
            known_encodings.append(enc[0])
            known_names.append(os.path.splitext(file)[0])

    return known_encodings, known_names


def recognize_faces(unknown_encodings, known_encodings, known_names):
    results = []

    for face in unknown_encodings:
        matches = face_recognition.compare_faces(known_encodings, face)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]

        results.append(name)

    return results