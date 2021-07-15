from PIL import Image
import face_recognition
import glob

# All files ending with .txt
files = glob.glob("faces/*.JPG")
for file in files:
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)
    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        delta_x = (right - left)*0.2
        delta_y = (bottom - top)*0.2
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left,
                                                                                                    bottom, right))
        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save(file[:-4]+'_cut.jpg')