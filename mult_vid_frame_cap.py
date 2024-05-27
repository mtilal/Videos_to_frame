import cv2
import numpy as np
import os

# Function definition to load videos sequentially and extract frames
def mult_vid(file,batch_num):
    #===================================================================================#
    # Video Load and Information summary
    vid = cv2.VideoCapture(file,)
    # Total frame count and fps
    frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    print('Total Frames: ',frames,'Frame Rate: ',fps)
    #=====================================================================================#
    # Function definition to create new directory
    def path_creator(bnum,NFTC):
        # Parent Directory path 
        parent_dir = 'Path_to_folder_to_save_the_captured_frames' # Replace this with the path to the folder where you want to create the batchwise folders for videos
        # Path 
        path = os.path.join(parent_dir, 'Batch_%s_%s Frames' % (bnum,NFTC)) 
        # Creatnig a new directory
        os.makedirs(path, exist_ok= True) 
        print("Directory created") 
        return path
    #======================================================================================#
    # Frame Capture Parameter
    nftc = 100      # Total number of frames to be captured
    n_consec = 2    # Number of consecutive frames required. Set this to '1' if you need to capture single frame after regular intervals

    run_count = int(nftc/n_consec)      # Determining Total number of runs to capture desired number of frames
    #print('run_count: ', run_count)
    frame_skip = int(frames/run_count) # Calculating number of frames to skip
    #print('Frame Skip: ',frame_skip)

    frame_num= 0            # Initial valun of frame to be captured    
    frame_counter = 0       # Initializing frame counter
    #======================================================================================#
    # Creating New Folder for Saving Images
    fpath= path_creator(batch_num,nftc)
    #======================================================================================#
    # Frame capture code
    for x in range(run_count):
        if frame_num < frames:
            for count in range (n_consec):
                vid.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
                ret, frame = vid.read()
                cv2.imwrite(os.path.join(fpath, f'Frame_{frame_num + 1}.jpg'), frame)
                print("Frame Number", frame_num)
                frame_num = frame_num + 1
            frame_num = frame_num + frame_skip
            print('Skipping Frames')
        else:
            print('Max frames reached')
            break
    #=====================================================================================#        
    vid.release()
btn = 0 
for file in os.listdir("Path_to_the_folder_conataining_input_videos"):
    if file.endswith(".avi"):
        path=os.path.join("Path_to_the_folder_conataining_input_videos", file)
        btn = btn + 1
        # Function call to load videos sequentially and extract frames
        mult_vid(path,btn)
