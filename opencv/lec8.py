import cv2
import mediapipe as mp
import time

class PoseDetector:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            raise ValueError("Error: Could not open video.")
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.pTime = 0
    
    def process_frame(self, frame):
        # Chuyển ảnh sang RGB
        imRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Phát hiện tư thế
        results = self.pose.process(imRGB)
        return results
    
    def draw_landmarks(self, frame, results):
        if results.pose_landmarks:
            # Vẽ các điểm pose landmarks
            self.mpDraw.draw_landmarks(frame, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            h, w, _ = frame.shape
            for id, lm in enumerate(results.pose_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 4, (255, 0, 0), cv2.FILLED)
    
    def display_fps(self, frame):
        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime
        cv2.putText(frame, f"FPS: {int(fps)}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    def run(self):
        while True:
            success, frame = self.cap.read()
            if not success:
                print("Video ended or error in reading frame.")
                break
            
            results = self.process_frame(frame)
            self.draw_landmarks(frame, results)
            self.display_fps(frame)
            
            cv2.imshow("Pose Detection", frame)
            
            # Exit if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Sử dụng lớp
if __name__ == "__main__":
    video_path = 'D:/code/shimeji-main/opencv/vio/1.mp4'
    detector = PoseDetector(video_path)
    detector.run()
