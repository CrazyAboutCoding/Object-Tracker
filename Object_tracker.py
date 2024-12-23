import cv2

"""when running the program:
after the Tracker screen is visible,
press esc and you'll get a window "ROI selector"
mark the object you want then press enter
you'll get the Tracker screen with object being tracked
"""

tracker = cv2.TrackerKCF_create()
video = cv2.VideoCapture(0)

#initialize variables for tracking success
total_frames = 0
successful_frames = 0

while True:
    k, frame = video.read()
    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

bbox = cv2.selectROI(frame, False)
ok = tracker.init(frame, bbox)
cv2.destroyWindow("ROI selector")

while True:
    ok, frame = video.read()
    ok, bbox = tracker.update(frame)
    total_frames += 1

    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 0, 255), 2, 2)
        successful_frames += 1
    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

#calculate success rate
success_rate = (successful_frames / total_frames) * 100 if total_frames > 0 else 0
print(f"Tracking Success Rate: {success_rate}%")
