import cv2
import datetime
print(cv2.__version__)
vidcap = cv2.VideoCapture('dev/Data/video/mydata.mov')
class_name = "female"
success,image = vidcap.read()
count = 0
success = True
while success:
  # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  count += 1
  print count
  date_and_time = datetime.datetime.now()
  d_t = date_and_time.isoformat()
  d_t = str(d_t)
  d_t = d_t.replace(".", "")
  d_t = d_t.replace(":", "")
  d_t = d_t.replace("-", "")
  savepath = "/Users/pallawi/dev/attendance/Data/video/" + class_name + "/"+class_name + '_' + d_t + '.jpg'
  cv2.imwrite(savepath,image)
