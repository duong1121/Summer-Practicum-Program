import cv2 
import random
import numpy as np
import os
vid_capture = cv2.VideoCapture('c:/Users/ACER/Downloads/Intersection.mp4')

output_filename = 'street.mp4'
output_frames_per_second = 20.0
file_size = (1920, 1080)

#Add Gausian noise
#def add_gaussian_noise(image, mean=0, std_dev=10):
 #   noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint8)
    
 #   noisy_image = cv2.add(image, noise)
    
 #   return noisy_image

new = cv2.VideoWriter_fourcc(*'mp4v')
result = cv2.VideoWriter(output_filename, new, output_frames_per_second, file_size)

frame_count = 0
while(vid_capture.isOpened()):
	success, frame = vid_capture.read()
	if success == True:

		#Convert the frame to grayscale.
		frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		#Flip the frame horizontally.
		frame=cv2.flip(frame,1)

		#Rotate the frame by 90 degree.
		frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)

		#Add Gausian noise
		noise = np.random.normal(0, 1, frame.shape).astype(np.uint8)
		frame=cv2.add(frame, noise)

		save_path = os.path.join('c:/Users/ACER/Downloads/AI/Image',f'frame_{frame_count}.jpg')
		cv2.imwrite(save_path, frame)
		frame_count += 1

		key = cv2.waitKey(20)
		cv2.imshow("Frame", frame)
		if key == ord('q'):
			break
	else:
		break

# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()



