import cv2
import sys
from random import randint

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']

def createTrackerByName(trackerType):
    # https://pt.stackoverflow.com/questions/565464/opencv-python-cv2-error-opencv4-6-0-1-error-5bad-argument-in-func
    if trackerType == tracker_types[0]:
        tracker = cv2.legacy.TrackerBoosting_create()
    elif trackerType == tracker_types[1]:
        tracker = cv2.legacy.TrackerMIL_create()
    elif trackerType == tracker_types[2]:
        tracker = cv2.legacy.TrackerKCF_create()
    elif trackerType == tracker_types[3]:
        tracker = cv2.legacy.TrackerTLD_create()
    elif trackerType == tracker_types[4]:
        tracker = cv2.legacy.TrackerMedianFlow_create()
    elif trackerType == tracker_types[5]:
        tracker = cv2.legacy.TrackerMOSSE_create()
    elif trackerType == tracker_types[6]:
        tracker = cv2.legacy.TrackerCSRT_create()
    else:
        tracker = None
        print('Nome incorreto')
        print('Os rastreadores disponíveis são: ')
        for t in tracker_types:
            print(t)

    return tracker

cap = cv2.VideoCapture("videos/race.mp4")
#cap = cv2.VideoCapture("videos/walking.avi")

ok, frame = cap.read()
if not ok:
    print('Não é possível ler o arquivo de vídeo')
    sys.exit(1)

bboxes = []
colors = []

while True:
    bbox = cv2.selectROI('MultiTracker', frame)
    bboxes.append(bbox)
    colors.append((randint(0, 255), randint(0,255), randint(0,255)))
    print('Pressione q para sair das caixas de seleção e começar a rastrear')
    print('Pressione qualquer outra tecla para selecionar o próximo objeto')
    k = cv2.waitKey(0) & 0XFF
    if (k == 113): # teclar q para mudar de ROI Region Of Interess
        break

print('Caixas delimitadoras selecionadas {}'.format(bboxes))
print('Cores {}'.format(colors))

# Specify the tracker type
#trackertype = 'CSRT'
trackertype = 'KCF'
# module 'cv2' has no attribute 'MultiTracker_create'
#print(cv2.getVersionString())
multiTracker = cv2.legacy.MultiTracker_create()
#multiTracker = cv2.MultiTracker_create()

for bbox in bboxes:
    # https://pt.stackoverflow.com/questions/565464/opencv-python-cv2-error-opencv4-6-0-1-error-5bad-argument-in-func
    multiTracker.add(createTrackerByName(trackertype), frame, bbox)

while cap.isOpened():
     ok, frame = cap.read()
     if not ok:
         break

     ok, boxes = multiTracker.update(frame)

     for i, newbox in enumerate(boxes):
         (x, y, w, h) = [int(v) for v in newbox]
         cv2.rectangle(frame, (x, y), (x + w, y + h), colors[i], 2, 1)

     cv2.imshow('MultiTracker', frame)

     if cv2.waitKey(1) & 0XFF == 27:
         break
