1a. 
Input Clip: https://drive.google.com/file/d/1-SDEzMYt4cBBVck6NRPHKzzvn3RW8hCH/view?usp=sharing
Use any suitable library/framework to decompose the input clip into individual frames. Perform the following image processing operations on each frame:

    Convert the frame to grayscale.

    Flip the frame horizontally.

    Rotate the frame by a random degree.

    Add random noise to the frame.

After processing each frame, save them as individual image files in JPG format.

1b.
Using YOLO5 to detect objects in the input clip and save  the detected information of objects (FrameID, Object’s class, Object’s bounding box, Confidence) into a JSON file.
