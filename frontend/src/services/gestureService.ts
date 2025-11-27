// gestureService.ts
import { FilesetResolver, HandLandmarker } from "@mediapipe/tasks-vision";

class GestureService {
  private handLandmarker: HandLandmarker | null = null;
  private isInitialized = false;
  private lastVideoTime = -1;

  async initialize() {
    try {
      const vision = await FilesetResolver.forVisionTasks(
        "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@latest/wasm"
      );
      
      this.handLandmarker = await HandLandmarker.createFromOptions(vision, {
        baseOptions: { 
          modelAssetPath: "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task" 
        },
        numHands: 2,
        runningMode: "VIDEO"
      });
      
      this.isInitialized = true;
      console.log("Gesture Service initialized");
    } catch (error) {
      console.error("Error initializing Gesture Service:", error);
    }
  }

  detectGestures(video: HTMLVideoElement, callback: (gesture: string) => void) {
    if (!this.isInitialized || !this.handLandmarker || video.currentTime === this.lastVideoTime) {
      return;
    }

    this.lastVideoTime = video.currentTime;

    try {
      const results = this.handLandmarker.detectForVideo(video, Date.now());
      
      if (results.landmarks && results.landmarks.length > 0) {
        const gesture = this.analyzeHandGesture(results.landmarks[0]);
        if (gesture) {
          callback(gesture);
        }
      }
    } catch (error) {
      console.error("Error detecting gestures:", error);
    }
  }

  private analyzeHandGesture(landmarks: any[]): string | null {
    // Lógica básica de detecção de gestos - você pode expandir isso
    const thumbTip = landmarks[4];
    const indexTip = landmarks[8];
    const middleTip = landmarks[12];
    const ringTip = landmarks[16];
    const pinkyTip = landmarks[20];
    const wrist = landmarks[0];

    // Detectar mão fechada (punho)
    const fingersExtended = [indexTip, middleTip, ringTip, pinkyTip].filter(
      tip => tip.y < wrist.y
    ).length;

    if (fingersExtended === 0) {
      return "Mão Fechada";
    }

    // Detectar paz e amor (pinky e indicador)
    if (indexTip.y < wrist.y && pinkyTip.y < wrist.y && 
        middleTip.y > wrist.y && ringTip.y > wrist.y) {
      return "Paz e Amor";
    }

    // Detectar polegar para cima
    if (thumbTip.y < wrist.y && fingersExtended === 1) {
      return "Joinha";
    }

    // Detectar mão aberta
    if (fingersExtended >= 4) {
      return "Mão Aberta";
    }

    return null;
  }

  cleanup() {
    if (this.handLandmarker) {
      this.handLandmarker.close();
      this.handLandmarker = null;
    }
    this.isInitialized = false;
  }
}

export const gestureService = new GestureService();