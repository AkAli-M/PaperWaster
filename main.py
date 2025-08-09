import paper_detect
import Imagelocation
import CameraFeed
import cv2


# file_name = CameraFeed.CaptureImage()

for file_name in Imagelocation.image_paths:
    paper_detect.ShowImage2(paper_detect.BlackFilter(file_name))
    paper_detect.ShowImageRaw(file_name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
