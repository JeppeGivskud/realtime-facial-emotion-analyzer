from video_main import EmotionAnalysisVideo
import os
print("Starting")
print("Video file exists:", os.path.exists('/realtime-facial-emotion-analyzer/data/input.mp4'))
print("Video file exists:", os.path.exists('data/input.mp4'))

print("Current working directory:", os.getcwd())
# You can pick a face detector depending on Acc/speed requirements
print("Making analyser")
emotion_recognizer = EmotionAnalysisVideo(
    face_detector="dlib",
    model_loc="models",
    face_detection_threshold=0.0,
)
print("Analyser made")



print("Starting Emotion Analysis on Video")
# Using relative paths for file access
print("Starting")
print("Video file exists:", os.path.exists('data/input.mp4'))
print("Output file exists:", os.path.exists('data/output.mp4'))

print("Current working directory:", os.getcwd())

emotion_recognizer.emotion_analysis_video(
    video_path='/realtime-facial-emotion-analyzer/data/input.mp4',
    detection_interval=1,
    save_output=True,
    preview=False,  # Ensure this is set to False
    output_path="/realtime-facial-emotion-analyzer/data/output.mp4",
    resize_scale=0.5,
)
print("Video file exists:", os.path.exists('data/input.mp4'))
print("Output file exists:", os.path.exists('data/output.mp4'))


