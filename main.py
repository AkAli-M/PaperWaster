import paper_detect
import Imagelocation
import CameraFeed

file_name = CameraFeed.CaptureImage()


paper_detect.ShowImage2(paper_detect.BlackFilter(file_name),Loop=True)
paper_detect.ShowImageRaw(file_name,Loop=True)


# paper_detect.ShowImage(paper_detect.Filter3(file_name),Loop=True)

