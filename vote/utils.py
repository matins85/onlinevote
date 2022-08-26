from deepface import DeepFace
import os
import base64
import re
import uuid


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def recognize_face(image1, image2):
    result = DeepFace.verify(img1_path=image1, img2_path=image2, enforce_detection=True)['verified']
    return result


def save_image(src):
    result = re.search("data:image/(?P<ext>.*?);base64,(?P<data>.*)", str(src), re.DOTALL)
    ext = result.groupdict().get("ext")
    data = result.groupdict().get("data")
    # 2, base64 decoding
    img = base64.urlsafe_b64decode(data)
    # 3, the binary file is saved
    filename = "{}.{}".format(uuid.uuid4(), ext)
    complete_name = os.path.join(base_dir, 'templates', filename)
    with open(complete_name, "wb") as f:
        f.write(img)
    return filename
