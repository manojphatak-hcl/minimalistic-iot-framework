'''
Reads frames from a video stream & compares with known faces
For now, simply prints "Found Match", when it finds the face in known-faces
This function is configured to run as part of one of the nodes in node-red IoT platform
The code "prints" the message, because node-red can pipe console output of one node into the next node.
'''

import os
import logging
import fnmatch

import cv2
import face_recognition

logging.root.setLevel(logging.DEBUG)
MAX_NUM_FRAMES_TO_PROCESS = 2  


def read_movie(movie_file):
    assert os.path.exists(movie_file)
    input_movie = cv2.VideoCapture(movie_file)
    numframes = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
    logging.debug("number of frames: %d" % (numframes))
    
    num_frames = 0
    while True:
        ret, frame = input_movie.read()
        num_frames += 1
        
        if not ret:
            break
        if num_frames > MAX_NUM_FRAMES_TO_PROCESS:  #This code to be removed from the production code
            break
       
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]
        yield rgb_frame
        
    

def load_reference_faces(dirpath):
    def load_images():
        assert os.path.exists(dirpath)
        imgs = fnmatch.filter(os.listdir(dirpath), "*.jpg")
        names = [os.path.splitext(f)[0] for f in imgs]
        imgs = [os.path.join(dirpath, img) for img in imgs]
        return zip(names, imgs)
    
    def get_face_encoding(imagefile):
        image = face_recognition.load_image_file(imagefile)
        face_encoding = face_recognition.face_encodings(image)[0]
        return face_encoding
    
    face_encodings = [(name_image[0],get_face_encoding(name_image[1])) for name_image in load_images()]
    return dict(face_encodings)
    
    
    

def recoginze_faces(frame, known_faces):
    known_face_encodings = [f[1] for f in list(known_faces.values())]
    
    face_locations = face_recognition.face_locations(frame, model="cnn")
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    for fncod in face_encodings:
        match = face_recognition.compare_faces(known_face_encodings, fncod, tolerance=0.50)
        print(match)
        

if __name__ == "__main__":
    movie_file = r"movie.webm"
    FACE_COMPARE_TOL = 0.50
    known_faces_dict = load_reference_faces("./ref_images")
    known_faces = list(known_faces_dict.values())
    
    for frame in read_movie(movie_file):
        logging.debug("Processing frame...")
        face_locations = face_recognition.face_locations(frame, model="cnn")
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for encod in face_encodings:
            match = face_recognition.compare_faces(known_faces, encod, FACE_COMPARE_TOL)
            if match:
                print("Found Match")
            else:
                print("No Match")
