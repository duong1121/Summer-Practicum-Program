1a. 
Input Clip: https://drive.google.com/file/d/1-SDEzMYt4cBBVck6NRPHKzzvn3RW8hCH/view?usp=sharing
Use any suitable library/framework to decompose the input clip into individual frames. Perform the following image processing operations on each frame:

    Convert the frame to grayscale.

    Flip the frame horizontally.

    Rotate the frame by a random degree.

    Add random noise to the frame.

After processing each frame, save them as individual image files in JPG format.

Some example of the output:

![image](https://github.com/duong1121/Summer-Practicum-Program/assets/75771867/28f35a89-75c8-4ac6-bce2-c6db295f8c40)

![image](https://github.com/duong1121/Summer-Practicum-Program/assets/75771867/cee812c8-6a0c-4ab7-925a-6bbb0d899c54)

![image](https://github.com/duong1121/Summer-Practicum-Program/assets/75771867/9f03c257-146a-4eda-bf9e-77107e43fc39)


1b.
Using YOLO5 to detect objects in the input clip and save  the detected information of objects (FrameID, Object’s class, Object’s bounding box, Confidence) into a JSON file.
