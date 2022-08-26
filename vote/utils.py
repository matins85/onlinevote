# from deepface import DeepFace
import os
import base64
import re
import uuid
import boto3


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# def recognize_face(image1, image2):
#     try:
#         result = DeepFace.verify(img1_path=image1, img2_path=image2, enforce_detection=True)['verified']
#         if os.path.exists(image1):
#             os.remove(image1)
#         if os.path.exists(image2):
#             os.remove(image2)
#         return result
#     except Exception as e:
#         if os.path.exists(image1):
#             os.remove(image1)
#         if os.path.exists(image2):
#             os.remove(image2)
#         raise e


def compare_faces(source_file: str, target_file: str):
    client = boto3.client('rekognition', region_name='us-east-1')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': base64.urlsafe_b64decode(source_file)},
                                    TargetImage={'Bytes': base64.urlsafe_b64decode(target_file)})

    for faceMatch in response['FaceMatches']:
        similarity = str(faceMatch['Similarity'])
        print(similarity)
        if float(similarity) < 89:
            raise TypeError("Picture does not correspond")
        else:
            pass
    # return len(response['FaceMatches'])


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
