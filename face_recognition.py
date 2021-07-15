from PIL import Image
import face_recognition
import glob

# All files ending with .txt

files = glob.glob("faces/*.jpeg")
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


imfg = Image.open(r"faces/ATXME6008_cut.jpg").convert("RGBA")

imbg = Image.open(r"faces/DSC_0040_cut.jpg").convert("RGBA")

imbg_width, imbg_height = imbg.size
imfg_resized = imfg.resize((imbg_width, imbg_height), Image.LANCZOS)

#Test = Image.alpha_composite(imfg_resized, imbg_width)
#Test.save("test.png", format="png")

imbg = Image.open(r"faces/profile_smile._cut.jpg").convert("RGBA")
blended = Image.blend(imbg, imbg, alpha=1)
imbg_width, imbg_height = imbg.size

files = glob.glob("faces/*_cut.jpg")
for file in files:
    imfg = Image.open(file).convert("RGBA")
    imfg_resized = imfg.resize((imbg_width, imbg_height), Image.LANCZOS)
    blended = Image.blend(imbg, imbg, alpha=1)

blended = Image.blend(imfg_resized, imbg, alpha=1)
blended.save("blended.png")

