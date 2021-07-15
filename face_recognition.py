from PIL import Image
import face_recognition
from numpy import *
import glob

# All files ending with .txt

files = glob.glob("faces/*.JPG") + glob.glob("faces/*.jpg") + glob.glob("faces/*.jpeg")
for file in files:
    print(file)
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)
    for face_location in face_locations:
        # Print the location of each face in this image
        top, right, bottom, left = face_location
        delta_x = int((right - left)*0.3)
        delta_y = int((bottom - top)*0.4)
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left,
                                                                                                    bottom, right))
        # You can access the actual face itself like this:
        try:
            face_image = image[top-delta_y:bottom+delta_y, left-delta_x:right+delta_x]
            pil_image = Image.fromarray(face_image)
            pil_image.save('faces_cut/' + file[6:-4] + '_cut.jpg')
        except:
            continue

imbg = Image.open(r"faces_cut/profile_serious._cut.jpg").convert("RGBA")
blended = Image.blend(imbg, imbg, alpha=1)
imbg_width, imbg_height = blended.size

files = glob.glob("faces_cut/*_cut.jpg")
print('\nTotal archivos: ', len(files))
nofiles = 1.5/(len(files))

Fotos_resized = []
for file in files:
    imfg = Image.open(file).convert("RGBA")
    imfg_resized = imfg.resize((imbg_width, imbg_height), Image.LANCZOS)
    Fotos_resized.append(imfg_resized)

for j, fotos in enumerate(Fotos_resized):
    if j == 0:
        im1arr = asarray(fotos)
        im1arrF = im1arr.astype('float')
        additionF = im1arrF
    else:
        im1arr = asarray(fotos)
        im1arrF = im1arr.astype('float')
        additionF += im1arrF

additionF = additionF/len(Fotos_resized)
addition = additionF.astype('uint8')
resultImage = Image.fromarray(addition)
resultImage.save("blended.png")

blended = Image.blend(blended, resultImage,  alpha=0.9)
blended.save("blended_2.png")


