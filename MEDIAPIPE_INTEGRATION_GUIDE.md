# MediaPipe Integration Guide - Advanced Gesture Detection

## 📦 Passo 1: Instalar dependências

```bash
cd frontend
npm install @mediapipe/hands @mediapipe/camera_utils @mediapipe/drawing_utils
```

Ou com yarn:
```bash
yarn add @mediapipe/hands @mediapipe/camera_utils @mediapipe/drawing_utils
```

## 🎯 Passo 2: Integração no ClassPage.tsx

### 2.1 - Copie a função avançada de detecção

Abra o arquivo `/ADVANCED_GESTURE_DETECTION.ts` e copie a função `detectGestureAdvanced()` completa.

### 2.2 - Cole no ClassPage.tsx

Adicione a função dentro do componente ClassPage (depois da função `capture()`):

```tsx
// Advanced gesture detection (copie da ADVANCED_GESTURE_DETECTION.ts)
function detectGesture(landmarks: Array<{ x: number; y: number; z?: number }>, handedness: string) {
  if (!landmarks || landmarks.length < 21) return 'Unknown';

  try {
    const tipIndices = [4, 8, 12, 16, 20];
    const pipIndices = [3, 6, 10, 14, 18];

    const dist = (i: number, j: number) => {
      const p1 = landmarks[i];
      const p2 = landmarks[j];
      if (!p1 || !p2) return 0;
      const dx = p1.x - p2.x;
      const dy = p1.y - p2.y;
      const dz = (p1.z || 0) - (p2.z || 0);
      return Math.sqrt(dx * dx + dy * dy + dz * dz);
    };

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
    const palmCenter = landmarks[9];
    const wrist = landmarks[0];
    const thumbExtended = thumbTip && thumbIp && thumbTip.y < thumbIp.y;
    const thumbToRight = thumbTip && palmCenter && thumbTip.x > palmCenter.x + 0.05;
    const thumbToLeft = thumbTip && palmCenter && thumbTip.x < palmCenter.x - 0.05;
    const thumbUp = thumbTip && wrist && thumbTip.y < wrist.y - 0.1;
    const thumbDown = thumbTip && wrist && thumbTip.y > wrist.y + 0.1;

    // GESTURE RECOGNITION
    if (extendedCount === 0 && !thumbExtended) return '✊ Closed Fist';
    if (extendedCount === 4 && thumbExtended) return '✋ Open Palm';
    if (indexExt && middleExt && !ringExt && !pinkyExt && !thumbExtended) return '✌️ Peace';
    if (thumbUp && thumbExtended && extendedCount === 0) return '👍 Thumbs Up';
    if (thumbDown && thumbExtended && extendedCount === 0) return '👎 Thumbs Down';
    if (thumbTip && landmarks[8]) {
      const thumbIndexDist = dist(4, 8);
      if (thumbIndexDist < 0.05 && middleExt && ringExt && pinkyExt) return '👌 OK';
    }
    if (indexExt && !middleExt && !ringExt && !pinkyExt && !thumbExtended) return '☝️ Pointing';
    if (indexExt && !middleExt && !ringExt && pinkyExt && !thumbExtended) return '🤘 Rock';
    if (indexExt && middleExt && ringExt && !pinkyExt && !thumbExtended) return '3️⃣ Three';
    if (thumbExtended && pinkyExt && !indexExt && !middleExt && !ringExt) return '📞 Call Me';

    const totalExt = extendedCount + (thumbExtended ? 1 : 0);
    return `${totalExt} finger(s)`;
  } catch (e) {
    return 'Unknown';
  }
}
```

### 2.3 - Update refs/state (já deve estar feito)

Certifique-se de que você tem estes refs e estados:

```tsx
const overlayRef = useRef<HTMLCanvasElement | null>(null);
const handsRef = useRef<any | null>(null);
const mpCameraRef = useRef<any | null>(null);
const [gesture, setGesture] = useState<string | null>(null);
```

### 2.4 - Atualizar a área do vídeo

Substitua a seção do vídeo por:

```tsx
<Box sx={{ position: 'relative', width: '100%', height: '100%' }}>
  <video 
    ref={videoRef} 
    style={{ width: '100%', height: '100%', objectFit: 'contain', display: 'block' }} 
    playsInline 
    muted 
  />
  <canvas 
    ref={overlayRef} 
    style={{ position: 'absolute', left: 0, top: 0, pointerEvents: 'none' }} 
  />
</Box>

{/* Exibir gesto detectado */}
{gesture && (
  <Box sx={{ mt: 1, p: 1, bgcolor: '#e8f5e9', borderRadius: 1 }}>
    <Typography variant="body2" sx={{ fontWeight: 'bold' }}>
      🎯 Gesto: {gesture}
    </Typography>
  </Box>
)}
```

## 🎮 Gestos Reconhecidos

| Gesto | Descrição |
|-------|-----------|
| ✊ Closed Fist | Todos os dedos fechados |
| ✋ Open Palm | Mão totalmente aberta |
| ✌️ Peace / Victory | Index + middle estendidos |
| 👍 Thumbs Up | Polegar para cima |
| 👎 Thumbs Down | Polegar para baixo |
| 👌 OK | Polegar + index juntados, outros abertos |
| ☝️ Pointing | Apenas index estendido |
| 🤘 Rock / Horns | Index + pinky estendidos |
| 3️⃣ Three Fingers | Index + middle + ring estendidos |
| 📞 Call Me | Polegar + pinky na lateral |
| 👉 / 👈 | Polegar apontando |

## 🧪 Testando

1. Abra o navegador na página de classe (`/class` ou a rota que você definiu)
2. Clique em "Iniciar câmera" e permita o acesso
3. Faça gestos com a mão em frente à câmera
4. O gesto detectado aparecerá:
   - Desenhado com pontos vermelhos (landmarks) e linhas verdes (conexões)
   - Exibido em texto colorido abaixo do vídeo

## 🔧 Troubleshooting

**Câmera não inicia?**
- Permitir acesso à câmera no navegador
- Verificar se o navegador suporta getUserMedia

**Gestos não detectados?**
- Certificar-se de que as mãos estão bem iluminadas
- Posicionar a mão dentro do frame da câmera
- Tentar mover mais devagar

**Erro de módulos MediaPipe?**
- Rodar `npm install @mediapipe/hands @mediapipe/camera_utils @mediapipe/drawing_utils`
- Limpar node_modules e reinstalar: `rm -rf node_modules && npm install`

## 📝 Próximas Melhorias

- [ ] Salvar gesto detectado em histórico
- [ ] Integrar gestos com comandos da aplicação (ex: peace = mutar/desmutar)
- [ ] Suporte para ambas as mãos
- [ ] Reconhecimento de sequências de gestos
- [ ] Calibração de sensibilidade
