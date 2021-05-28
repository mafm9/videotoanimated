import cv2 as cv
import pyopenpose as op
import time
start_time = time.time()

video = cv.VideoCapture('testvideos/test4.mp4')
params = dict()
params["model_folder"] = "/home/mafm9/openpose/models/"
params["face"] = True
params["face_detector"] = 1
params["body"] = 1
params["net_resolution"] = "-1x176"
params["face_net_resolution"] = "320x320"
params["write_json"] = "./jsons/"
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()
datum = op.Datum()
filenum = 0
while video.isOpened():
    ret, frame = video.read()
    if ret:
        datum = op.Datum()
        numstring = str(filenum).zfill(12)
        datum.name = "video_" + numstring
        filenum += 1
        imageToProcess = frame
        datum.cvInputData = imageToProcess
        opWrapper.emplaceAndPop(op.VectorDatum([datum]))
        print("Face keypoints: \n" + str(datum.faceKeypoints))
        cv.imshow("OpenPose 1.7.0 - Tutorial Python API", datum.cvOutputData)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
cv.destroyAllWindows()
print(f'{time.time() - start_time}Seconds: ')
