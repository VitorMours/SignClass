import React, { useRef, useState, useEffect } from 'react';
import {
  Box,
  Paper,
  Typography,
  TextField,
  IconButton,
  Button,
  Card,
  CardHeader,
  CardContent,
  CardActions,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
} from '@mui/material';
import SendIcon from '@mui/icons-material/Send';
import CameraAltIcon from '@mui/icons-material/CameraAlt';
import StopIcon from '@mui/icons-material/Stop';

const ClassPage: React.FC = () => {
  // Chat state
  const [messages, setMessages] = useState<Array<{ id: number; text: string }>>([]);
  const [input, setInput] = useState('');

  // Camera refs/state
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const overlayRef = useRef<HTMLCanvasElement | null>(null);
  const handsRef = useRef<any | null>(null);
  const mpCameraRef = useRef<any | null>(null);
  const [streamActive, setStreamActive] = useState(false);
  const [snapshot, setSnapshot] = useState<string | null>(null);
  const [gesture, setGesture] = useState<string | null>(null);
  // eslint-disable-next-line react-hooks/rules-of-hooks
  const lastGestureRef = useRef<string | null>(null);
  // eslint-disable-next-line react-hooks/rules-of-hooks
  const gestureTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Dialog to show camera helper code
  const [openCode, setOpenCode] = useState(false);

  useEffect(() => {
    return () => {
      // cleanup on unmount
      stopCamera();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Handle gesture detection - add to input field
  useEffect(() => {
    if (gesture && gesture !== 'Unknown' && gesture !== lastGestureRef.current && streamActive) {
      lastGestureRef.current = gesture;

      // Clear previous timeout if exists
      if (gestureTimeoutRef.current) {
        clearTimeout(gestureTimeoutRef.current);
      }

      // Add gesture to input field
      setInput((prev) => (prev ? `${prev} ${gesture}` : gesture));

      // Reset gesture detection after 500ms to allow new gestures
      gestureTimeoutRef.current = setTimeout(() => {
        lastGestureRef.current = null;
      }, 500);
    }
  }, [gesture, streamActive]);

  function sendMessage() {
    if (!input.trim()) return;
    setMessages((m) => [...m, { id: Date.now(), text: input.trim() }]);
    setInput('');
  }

  async function startCamera() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        await videoRef.current.play();
      }
      setStreamActive(true);

      // try to initialize MediaPipe Hands (dynamic import)
      try {
        // @ts-ignore - dynamic import, package may not be present in all environments
        const HandsModule = await import('@mediapipe/hands');
        // @ts-ignore
        const CameraUtils = await import('@mediapipe/camera_utils');
        // @ts-ignore
        const DrawingUtils = await import('@mediapipe/drawing_utils');

        const hands = new HandsModule.Hands({
          locateFile: (file: string) => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`,
        });

        hands.setOptions({
          maxNumHands: 1,
          modelComplexity: 1,
          minDetectionConfidence: 0.7,
          minTrackingConfidence: 0.5,
        });

        hands.onResults((results: any) => {
          const canvas = overlayRef.current;
          const video = videoRef.current;
          if (!canvas || !video) return;
          const ctx = canvas.getContext('2d');
          if (!ctx) return;
          canvas.width = video.videoWidth;
          canvas.height = video.videoHeight;
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          if (results.image) ctx.drawImage(results.image, 0, 0, canvas.width, canvas.height);

          if (results.multiHandLandmarks && results.multiHandLandmarks.length > 0) {
            for (const landmarks of results.multiHandLandmarks) {
              DrawingUtils.drawConnectors(ctx, landmarks, HandsModule.HAND_CONNECTIONS, { color: '#00FF00', lineWidth: 2 });
              DrawingUtils.drawLandmarks(ctx, landmarks, { color: '#FF0000', lineWidth: 1 });
            }
            const l = results.multiHandLandmarks[0];
            if (l) {
              const gestureName = detectGesture(l);
              setGesture(gestureName);
            }
          } else {
            setGesture(null);
          }
        });

        const camera = new CameraUtils.Camera(videoRef.current!, {
          onFrame: async () => {
            await hands.send({ image: videoRef.current! });
          },
          width: videoRef.current!.videoWidth || 640,
          height: videoRef.current!.videoHeight || 480,
        });

        camera.start();
        handsRef.current = hands;
        mpCameraRef.current = camera;
      } catch (err) {
        console.warn('MediaPipe init failed:', err);
      }
    } catch (err) {
      // Could show a toast or set error state
      console.error('Erro ao acessar a câmera:', err);
      setStreamActive(false);
    }
  }

  function stopCamera() {
    const stream = videoRef.current?.srcObject as MediaStream | null;
    if (stream) {
      stream.getTracks().forEach((t) => t.stop());
      if (videoRef.current) videoRef.current.srcObject = null;
    }
    setStreamActive(false);
  }

  function capture() {
    if (!videoRef.current) return;
    const video = videoRef.current;
    const canvas = canvasRef.current || document.createElement('canvas');
    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const data = canvas.toDataURL('image/png');
    setSnapshot(data);
  }

  // Simple gesture detection based on hand landmarks (MediaPipe)
  function detectGesture(landmarks: Array<{ x: number; y: number; z?: number }>) {
    if (!landmarks || landmarks.length < 21) return 'Unknown';

    try {
      const isFingerExtended = (tipIdx: number, pipIdx: number) => {
        const tip = landmarks[tipIdx];
        const pip = landmarks[pipIdx];
        return tip && pip && tip.y < pip.y;
      };

      const indexExt = isFingerExtended(8, 6);
      const middleExt = isFingerExtended(12, 10);
      const ringExt = isFingerExtended(16, 14);
      const pinkyExt = isFingerExtended(20, 18);
      const extendedCount = [indexExt, middleExt, ringExt, pinkyExt].filter(Boolean).length;

      const thumbTip = landmarks[4];
      const thumbIp = landmarks[3];
      const wrist = landmarks[0];
      const thumbExtended = thumbTip && thumbIp && thumbTip.y < thumbIp.y;
      const thumbUp = thumbTip && wrist && thumbTip.y < wrist.y - 0.1;
      const thumbDown = thumbTip && wrist && thumbTip.y > wrist.y + 0.1;

      if (extendedCount === 0 && !thumbExtended) return '✊ Closed Fist';
      if (extendedCount === 4 && thumbExtended) return '✋ Open Palm';
      if (indexExt && middleExt && !ringExt && !pinkyExt && !thumbExtended) return '✌️ Peace';
      if (thumbUp && thumbExtended && extendedCount === 0) return '👍 Thumbs Up';
      if (thumbDown && thumbExtended && extendedCount === 0) return '👎 Thumbs Down';
      if (indexExt && !middleExt && !ringExt && !pinkyExt && !thumbExtended) return '☝️ Pointing';
      if (indexExt && !middleExt && !ringExt && pinkyExt && !thumbExtended) return '🤘 Rock';
      if (indexExt && middleExt && ringExt && !pinkyExt && !thumbExtended) return '3️⃣ Three';

      const totalExt = extendedCount + (thumbExtended ? 1 : 0);
      return `${totalExt} finger(s)`;
    } catch (e) {
      return 'Unknown';
    }
  }

  const cameraHelperCode = `// Exemplo de funções que este componente usa para acessar a câmera\nasync function startCamera() {\n  const stream = await navigator.mediaDevices.getUserMedia({ video: true });\n  videoElement.srcObject = stream;\n  await videoElement.play();\n}\n\nfunction stopCamera() {\n  const stream = videoElement.srcObject;\n  if (stream) stream.getTracks().forEach(t => t.stop());\n  videoElement.srcObject = null;\n}\n\nfunction capture() {\n  const canvas = document.createElement('canvas');\n  canvas.width = videoElement.videoWidth;\n  canvas.height = videoElement.videoHeight;\n  canvas.getContext('2d').drawImage(videoElement, 0, 0);\n  return canvas.toDataURL('image/png');\n}`;

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h5" sx={{ mb: 2 }}>
        Aula / Sala - Chat e Câmera
      </Typography>

      <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap' }}>
        {/* Left: Chat area */}
        <Box sx={{ flex: '1 1 60%', minWidth: 280 }}>
          <Paper sx={{ height: '70vh', display: 'flex', flexDirection: 'column', p: 2 }} elevation={2}>
            <Box sx={{ flex: 1, overflow: 'auto', mb: 2 }}>
              {messages.length === 0 ? (
                <Typography color="text.secondary">Nenhuma mensagem ainda. Use o campo abaixo para enviar.</Typography>
              ) : (
                messages.map((m) => (
                  <Box key={m.id} sx={{ mb: 1 }}>
                    <Paper sx={{ p: 1, display: 'inline-block' }}>
                      <Typography variant="body2">{m.text}</Typography>
                    </Paper>
                  </Box>
                ))
              )}
            </Box>
            <Box component="form" onSubmit={(e) => { e.preventDefault(); sendMessage(); }} sx={{ display: 'flex', gap: 1 }}>
              <TextField
                placeholder="Escreva uma mensagem..."
                fullWidth
                size="small"
                value={input}
                onChange={(e) => setInput(e.target.value)}
              />
              <IconButton color="primary" onClick={sendMessage} aria-label="send">
                <SendIcon />
              </IconButton>
            </Box>
          </Paper>
        </Box>

        {/* Right: Camera card */}
        <Box sx={{ flex: '1 1 38%', minWidth: 280 }}>
          <Card elevation={2} sx={{ height: '70vh', display: 'flex', flexDirection: 'column' }}>
            <CardHeader title="Câmera do usuário" subheader="Permita o acesso ao dispositivo" />
            <CardContent sx={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 1 }}>
              <Box sx={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', bgcolor: 'grey.100', position: 'relative' }}>
                <video ref={videoRef} style={{ maxWidth: '100%', maxHeight: '100%' }} playsInline muted />
                <canvas
                  ref={overlayRef}
                  style={{
                    position: 'absolute',
                    top: 0,
                    left: 0,
                    maxWidth: '100%',
                    maxHeight: '100%',
                    pointerEvents: 'none',
                  }}
                />
                {gesture && (
                  <Box
                    sx={{
                      position: 'absolute',
                      bottom: 10,
                      left: '50%',
                      transform: 'translateX(-50%)',
                      bgcolor: 'rgba(0, 0, 0, 0.7)',
                      color: 'white',
                      px: 2,
                      py: 1,
                      borderRadius: 1,
                      fontSize: 14,
                      fontWeight: 'bold',
                    }}
                  >
                    {gesture}
                  </Box>
                )}
              </Box>

              <Box sx={{ display: 'flex', gap: 1, mt: 1, alignItems: 'center' }}>
                <Button variant="contained" startIcon={<CameraAltIcon />} onClick={startCamera} disabled={streamActive}>
                  Iniciar câmera
                </Button>
                <Button variant="outlined" startIcon={<StopIcon />} onClick={stopCamera} disabled={!streamActive}>
                  Parar câmera
                </Button>
                <Button variant="contained" onClick={capture} disabled={!streamActive}>
                  Capturar
                </Button>
                <Button variant="text" onClick={() => setOpenCode(true)}>
                  Ver código da câmera
                </Button>
              </Box>

              {snapshot && (
                <Box sx={{ mt: 1 }}>
                  <Typography variant="subtitle2">Última captura:</Typography>
                  <Box component="img" src={snapshot} alt="snapshot" sx={{ width: '100%', mt: 1 }} />
                </Box>
              )}

              <canvas ref={canvasRef} style={{ display: 'none' }} />
            </CardContent>

            <CardActions>
              <Typography variant="caption" sx={{ ml: 1 }}>
                Dica: permita o acesso à câmera no navegador.
              </Typography>
            </CardActions>
          </Card>
        </Box>
      </Box>

      <Dialog open={openCode} onClose={() => setOpenCode(false)} maxWidth="md" fullWidth>
        <DialogTitle>Código de acesso à câmera</DialogTitle>
        <DialogContent>
          <Box component="pre" sx={{ whiteSpace: 'pre-wrap', fontFamily: 'monospace', fontSize: 13 }}>{cameraHelperCode}</Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenCode(false)}>Fechar</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};


export default ClassPage;