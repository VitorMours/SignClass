// Advanced Gesture Detection Function for MediaPipe Hands
// Cole esta função no seu ClassPage.tsx para substituir a detectGesture simples

export function detectGestureAdvanced(
  landmarks: Array<{ x: number; y: number; z?: number }>,
  handedness: string
): string {
  if (!landmarks || landmarks.length < 21) return 'Unknown';

  try {
    // Landmark indices (MediaPipe Hand)
    const tipIndices = [4, 8, 12, 16, 20];        // thumb, index, middle, ring, pinky tips
    const pipIndices = [3, 6, 10, 14, 18];        // proximal interphalangeal joints
    const mcpIndices = [2, 5, 9, 13, 17];         // metacarpophalangeal joints

    // Helper: Euclidean distance between two landmarks
    const dist = (i: number, j: number) => {
      const p1 = landmarks[i];
      const p2 = landmarks[j];
      if (!p1 || !p2) return 0;
      const dx = p1.x - p2.x;
      const dy = p1.y - p2.y;
      const dz = (p1.z || 0) - (p2.z || 0);
      return Math.sqrt(dx * dx + dy * dy + dz * dz);
    };

    // Helper: check if finger is extended (tip above pip in y-axis)
    // Note: y increases downward in MediaPipe, so extended = tip.y < pip.y
    const isFingerExtended = (tipIdx: number, pipIdx: number) => {
      const tip = landmarks[tipIdx];
      const pip = landmarks[pipIdx];
      return tip && pip && tip.y < pip.y;
    };

    // Count extended fingers (index through pinky)
    const indexExt = isFingerExtended(8, 6);
    const middleExt = isFingerExtended(12, 10);
    const ringExt = isFingerExtended(16, 14);
    const pinkyExt = isFingerExtended(20, 18);
    const extendedCount = [indexExt, middleExt, ringExt, pinkyExt].filter(Boolean).length;

    // Thumb analysis
    const thumbTip = landmarks[4];
    const thumbIp = landmarks[3];
    const thumbMcp = landmarks[2];
    const palmCenter = landmarks[9];  // middle MCP as palm reference
    const wrist = landmarks[0];

    const thumbExtended = thumbTip && thumbIp && thumbTip.y < thumbIp.y;

    // Thumb position (for directional gestures)
    const thumbToRight = thumbTip && palmCenter && thumbTip.x > palmCenter.x + 0.05;
    const thumbToLeft = thumbTip && palmCenter && thumbTip.x < palmCenter.x - 0.05;
    const thumbUp = thumbTip && wrist && thumbTip.y < wrist.y - 0.1;
    const thumbDown = thumbTip && wrist && thumbTip.y > wrist.y + 0.1;

    // ===== GESTURE RECOGNITION LOGIC =====

    // 1. CLOSED FIST
    if (extendedCount === 0 && !thumbExtended) {
      return '✊ Closed Fist';
    }

    // 2. OPEN PALM
    if (extendedCount === 4 && thumbExtended) {
      return '✋ Open Palm';
    }

    // 3. PEACE / VICTORY (index + middle up, ring + pinky down)
    if (indexExt && middleExt && !ringExt && !pinkyExt && !thumbExtended) {
      return '✌️ Peace / Victory';
    }

    // 4. THUMBS UP (thumb pointing up, other fingers closed)
    if (thumbUp && thumbExtended && extendedCount === 0) {
      return '👍 Thumbs Up';
    }

    // 5. THUMBS DOWN (thumb pointing down, other fingers closed)
    if (thumbDown && thumbExtended && extendedCount === 0) {
      return '👎 Thumbs Down';
    }

    // 6. OK SIGN (thumb + index pinched together, other fingers extended)
    if (thumbTip && landmarks[8]) {
      const thumbIndexDist = dist(4, 8);
      // thumbs and index tips close to each other
      if (thumbIndexDist < 0.05 && middleExt && ringExt && pinkyExt) {
        return '👌 OK';
      }
    }

    // 7. POINTING (only index extended, others closed)
    if (indexExt && !middleExt && !ringExt && !pinkyExt && !thumbExtended) {
      return '☝️ Pointing';
    }

    // 8. ROCK / HORNS (index + pinky extended, middle + ring closed, thumb closed)
    if (indexExt && !middleExt && !ringExt && pinkyExt && !thumbExtended) {
      return '🤘 Rock / Horns';
    }

    // 9. THREE FINGERS (index + middle + ring extended, pinky closed)
    if (indexExt && middleExt && ringExt && !pinkyExt && !thumbExtended) {
      return '3️⃣ Three Fingers';
    }

    // 10. CALL ME (thumb + pinky extended to the side)
    if (thumbExtended && pinkyExt && !indexExt && !middleExt && !ringExt) {
      if (thumbToLeft || thumbToRight) {
        return '📞 Call Me';
      }
    }

    // 11. STOP SIGN (all fingers extended, spread open)
    if (extendedCount === 4 && thumbExtended) {
      return '🛑 Stop / All Fingers';
    }

    // 12. INDEX + MIDDLE (like "2" or "scissors")
    if (indexExt && middleExt && !ringExt && !pinkyExt) {
      return '2️⃣ Two Fingers';
    }

    // 13. FIST WITH THUMB OUT (thumbs sideways)
    if (thumbExtended && !indexExt && !middleExt && !ringExt && !pinkyExt) {
      if (thumbToLeft) return '👈 Left Thumb';
      if (thumbToRight) return '👉 Right Thumb';
      return '👍 Thumb Up';
    }

    // Fallback: describe by finger count
    const totalExt = extendedCount + (thumbExtended ? 1 : 0);
    return `${totalExt} finger(s) extended`;
  } catch (e) {
    console.error('Gesture detection error:', e);
    return 'Unknown';
  }
}

// ===== USAGE IN CLASSPAGE.TSX =====
/*
Replace your simple detectGesture function with:

function detectGesture(landmarks: Array<{ x: number; y: number; z?: number }>, handedness: string) {
  return detectGestureAdvanced(landmarks, handedness);
}

Or import and use directly in the hands.onResults callback:
  const gestureName = detectGestureAdvanced(l, handednessLabel);
*/
