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
  Alert,
  CircularProgress,
} from '@mui/material';
import SendIcon from '@mui/icons-material/Send';
import CameraAltIcon from '@mui/icons-material/CameraAlt';
import StopIcon from '@mui/icons-material/Stop';
import PsychologyIcon from '@mui/icons-material/Psychology';

// Declarações TypeScript para Teachable Machine
declare global {
  interface Window {
    tmImage: any;
    tf: any;
  }
}

interface Message {
  id: number;
  text: string;
  type: 'gesture' | 'text';
}

const ClassPage: React.FC = () => {
  // Chat state
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');

  // Refs para containers do Teachable Machine
  const webcamContainerRef = useRef<HTMLDivElement | null>(null);
  const labelContainerRef = useRef<HTMLDivElement | null>(null);

  const [streamActive, setStreamActive] = useState(false);
  const [gesture, setGesture] = useState<string | null>(null);

  // Estados para IA
  const [isModelLoaded, setIsModelLoaded] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [predictions, setPredictions] = useState<Array<{className: string, probability: number}>>([]);
  const [debugInfo, setDebugInfo] = useState<string>('Aguardando inicialização...');

  // Referências para IA
  const lastGestureRef = useRef<string | null>(null);
  const gestureTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const modelRef = useRef<any>(null);
  const webcamRef = useRef<any>(null);
  const animationFrameRef = useRef<number | null>(null);

  // URL do modelo do Teachable Machine
  const MODEL_URL = "https://teachablemachine.withgoogle.com/models/pUDZjNc3s/";

  useEffect(() => {
    loadTeachableMachineScripts();

    return () => {
      stopCamera();
    };
  }, []);

  const loadTeachableMachineScripts = () => {
    if (window.tmImage) {
      setIsModelLoaded(true);
      setDebugInfo('✅ Teachable Machine já carregado');
      return;
    }

    setDebugInfo('🔄 Carregando bibliotecas...');

    const tfScript = document.createElement('script');
    tfScript.src = 'https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js';
    
    tfScript.onload = () => {
      setDebugInfo('🔄 TensorFlow.js OK, carregando Teachable Machine...');
      
      const tmScript = document.createElement('script');
      tmScript.src = 'https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js';
      
      tmScript.onload = () => {
        setIsModelLoaded(true);
        setDebugInfo('✅ Teachable Machine carregado!');
      };
      
      tmScript.onerror = () => {
        setError('❌ Erro ao carregar Teachable Machine');
        setDebugInfo('❌ Falha no carregamento do Teachable Machine');
      };
      
      document.head.appendChild(tmScript);
    };

    tfScript.onerror = () => {
      setError('❌ Erro ao carregar TensorFlow.js');
      setDebugInfo('❌ Falha no carregamento do TensorFlow.js');
    };

    document.head.appendChild(tfScript);
  };

  const init = async () => {
    if (!window.tmImage) {
      setError('Teachable Machine não está disponível');
      return;
    }

    try {
      setIsLoading(true);
      setError(null);
      setDebugInfo('🔄 Carregando modelo de IA...');

      const modelURL = MODEL_URL + "model.json";
      const metadataURL = MODEL_URL + "metadata.json";

      // Carregar o modelo
      const model = await window.tmImage.load(modelURL, metadataURL);
      modelRef.current = model;
      const maxPredictions = model.getTotalClasses();

      setDebugInfo(`✅ Modelo carregado! ${maxPredictions} classes detectadas`);

      // Setup da webcam do Teachable Machine
      const flip = true;
      const webcam = new window.tmImage.Webcam(480, 480, flip);
      await webcam.setup();
      await webcam.play();
      webcamRef.current = webcam;

      setDebugInfo('✅ Câmera iniciada, começando detecção...');

      // Adicionar canvas da webcam ao container
      if (webcamContainerRef.current) {
        webcamContainerRef.current.innerHTML = '';
        webcamContainerRef.current.appendChild(webcam.canvas);
      }

      // Criar labels no container
      if (labelContainerRef.current) {
        labelContainerRef.current.innerHTML = '';
        for (let i = 0; i < maxPredictions; i++) {
          const div = document.createElement("div");
          div.style.padding = "4px";
          div.style.fontSize = "12px";
          labelContainerRef.current.appendChild(div);
        }
      }

      setStreamActive(true);
      setIsLoading(false);

      // Iniciar loop de predição
      loop();

    } catch (err) {
      console.error('Erro na inicialização:', err);
      setError('Erro ao inicializar. Verifique as permissões da câmera.');
      setDebugInfo(`❌ Erro: ${err}`);
      setIsLoading(false);
    }
  };

  const loop = async () => {
    if (webcamRef.current && modelRef.current) {
      webcamRef.current.update();
      await predict();
      animationFrameRef.current = window.requestAnimationFrame(loop);
    }
  };

  const predict = async () => {
    if (!modelRef.current || !webcamRef.current) return;

    try {
      const prediction = await modelRef.current.predict(webcamRef.current.canvas);
      setPredictions(prediction);

      // Atualizar labels
      if (labelContainerRef.current) {
        for (let i = 0; i < prediction.length; i++) {
          const classPrediction =
            prediction[i].className + ": " + prediction[i].probability.toFixed(2);
          
          if (labelContainerRef.current.childNodes[i]) {
            (labelContainerRef.current.childNodes[i] as HTMLElement).innerHTML = classPrediction;
          }
        }
      }

      // Processar gestos detectados
      processDetectedGestures(prediction);

    } catch (error) {
      console.error('Erro na predição:', error);
    }
  };

  const processDetectedGestures = (prediction: any[]) => {
    if (!prediction || prediction.length === 0) return;

    let maxProbability = 0;
    let detectedGesture = '';

    for (let i = 0; i < prediction.length; i++) {
      const currentPred = prediction[i];
      if (currentPred.probability > maxProbability && currentPred.probability > 0.7) {
        maxProbability = currentPred.probability;
        detectedGesture = currentPred.className;
      }
    }

    setDebugInfo(`🎯 Detectando: ${detectedGesture || 'Nenhum gesto'} (${(maxProbability * 100).toFixed(1)}%)`);

    if (detectedGesture && detectedGesture !== lastGestureRef.current) {
      lastGestureRef.current = detectedGesture;
      setGesture(detectedGesture);

      if (gestureTimeoutRef.current) {
        clearTimeout(gestureTimeoutRef.current);
      }

      gestureTimeoutRef.current = setTimeout(() => {
        setGesture(null);
        lastGestureRef.current = null;
      }, 3000);

      // MUDANÇA: Em vez de adicionar ao chat, digita no input
      addGestureToInput(detectedGesture);
    }
  };

  const addGestureToInput = (detectedGesture: string) => {
    // Adiciona o nome do gesto ao input
    setInput(prev => {
      // Se o input estiver vazio, só adiciona o gesto
      if (!prev.trim()) {
        return detectedGesture;
      }
      // Se já tiver texto, adiciona um espaço e o gesto
      return prev + ' ' + detectedGesture;
    });
  };

  const stopCamera = () => {
    if (animationFrameRef.current) {
      window.cancelAnimationFrame(animationFrameRef.current);
      animationFrameRef.current = null;
    }

    if (webcamRef.current) {
      webcamRef.current.stop();
      webcamRef.current = null;
    }

    if (gestureTimeoutRef.current) {
      clearTimeout(gestureTimeoutRef.current);
      gestureTimeoutRef.current = null;
    }

    if (webcamContainerRef.current) {
      webcamContainerRef.current.innerHTML = '';
    }

    setStreamActive(false);
    setGesture(null);
    lastGestureRef.current = null;
    setDebugInfo('⏹️ Câmera parada');
  };

  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages((m) => [...m, { 
      id: Date.now(), 
      text: input.trim(),
      type: 'text' 
    }]);
    setInput('');
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h5" sx={{ mb: 2 }}>
        🎓 Aula - Chat com Detecção de Gestos IA
      </Typography>

      {error && (
        <Alert severity="error" sx={{ mb: 2 }} onClose={() => setError(null)}>
          {error}
        </Alert>
      )}

      <Alert severity="info" sx={{ mb: 2 }}>
        <Typography variant="body2">
          <strong>Status:</strong> {debugInfo}
        </Typography>
      </Alert>

      <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap' }}>
        {/* Chat */}
        <Box sx={{ flex: '1 1 60%', minWidth: 300 }}>
          <Paper sx={{ height: '70vh', display: 'flex', flexDirection: 'column', p: 2 }} elevation={2}>
            <Box sx={{ flex: 1, overflow: 'auto', mb: 2 }}>
              {messages.length === 0 ? (
                <Typography color="text.secondary">
                  Nenhuma mensagem ainda. Inicie a câmera para detectar gestos! 👋
                </Typography>
              ) : (
                messages.map((m) => (
                  <Box key={m.id} sx={{ mb: 1, display: 'flex', 
                    justifyContent: m.type === 'gesture' ? 'center' : 'flex-start' 
                  }}>
                    <Paper sx={{ 
                      p: 1.5, 
                      display: 'inline-block',
                      bgcolor: m.type === 'gesture' ? 'primary.light' : 'background.default',
                      color: m.type === 'gesture' ? 'primary.contrastText' : 'text.primary',
                      maxWidth: '80%',
                      borderRadius: 2
                    }}>
                      <Typography variant="body2" sx={{ 
                        fontWeight: m.type === 'gesture' ? 'bold' : 'normal',
                      }}>
                        {m.text}
                      </Typography>
                    </Paper>
                  </Box>
                ))
              )}
            </Box>
            <Box sx={{ display: 'flex', gap: 1 }}>
              <TextField
                placeholder="Digite uma mensagem ou faça um gesto..."
                fullWidth
                size="small"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={handleKeyPress}
              />
              <IconButton color="primary" onClick={sendMessage}>
                <SendIcon />
              </IconButton>
            </Box>
          </Paper>
        </Box>

        {/* Câmera */}
        <Box sx={{ flex: '1 1 38%', minWidth: 320 }}>
          <Card elevation={2} sx={{ height: '70vh', display: 'flex', flexDirection: 'column' }}>
            <CardHeader 
              title={
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <CameraAltIcon />
                  Detecção de Gestos por IA
                  {isModelLoaded && <PsychologyIcon color="success" fontSize="small" />}
                </Box>
              }
              subheader="Teachable Machine + TensorFlow.js"
            />
            <CardContent sx={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 2 }}>
              {/* Webcam Container */}
              <Box sx={{ 
                position: 'relative',
                bgcolor: 'grey.100',
                borderRadius: 1,
                overflow: 'hidden',
                minHeight: 320,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                border: '2px solid',
                borderColor: streamActive ? 'success.main' : 'grey.300'
              }}>
                <div ref={webcamContainerRef} style={{ 
                  width: '100%', 
                  height: '100%',
                  display: 'flex',
                  justifyContent: 'center',
                  alignItems: 'center'
                }} />
                
                {gesture && (
                  <Box sx={{
                    position: 'absolute',
                    bottom: 10,
                    left: '50%',
                    transform: 'translateX(-50%)',
                    bgcolor: 'rgba(0, 0, 0, 0.9)',
                    color: '#00ff00',
                    px: 3,
                    py: 1.5,
                    borderRadius: 2,
                    fontSize: 16,
                    fontWeight: 'bold',
                    border: '2px solid #00ff00',
                  }}>
                    🎯 {gesture}
                  </Box>
                )}

                {!streamActive && (
                  <Box sx={{ textAlign: 'center', color: 'text.secondary' }}>
                    <CameraAltIcon sx={{ fontSize: 48, mb: 1 }} />
                    <Typography>Clique em "Iniciar" para começar</Typography>
                  </Box>
                )}

                {isLoading && (
                  <Box sx={{ textAlign: 'center' }}>
                    <CircularProgress size={32} sx={{ mb: 1 }} />
                    <Typography variant="body2">Iniciando IA...</Typography>
                  </Box>
                )}
              </Box>

              {/* Previsões */}
              <Box sx={{ 
                p: 1.5, 
                bgcolor: 'grey.50', 
                borderRadius: 1,
                maxHeight: 150,
                overflow: 'auto'
              }}>
                <Typography variant="subtitle2" sx={{ mb: 1 }}>
                  📊 Previsões em Tempo Real:
                </Typography>
                <div ref={labelContainerRef} />
              </Box>

              {/* Botões */}
              <Box sx={{ display: 'flex', gap: 1, justifyContent: 'center' }}>
                <Button 
                  variant="contained" 
                  startIcon={isLoading ? <CircularProgress size={16} /> : <CameraAltIcon />}
                  onClick={init} 
                  disabled={streamActive || isLoading || !isModelLoaded}
                  size="medium"
                >
                  {isLoading ? 'Iniciando...' : 'Iniciar'}
                </Button>
                <Button 
                  variant="outlined" 
                  startIcon={<StopIcon />} 
                  onClick={stopCamera} 
                  disabled={!streamActive}
                  size="medium"
                >
                  Parar
                </Button>
              </Box>
            </CardContent>

            <CardActions>
              <Typography variant="caption" sx={{ ml: 1 }}>
                💡 Gestos com +70% aparecem no campo de texto
              </Typography>
            </CardActions>
          </Card>
        </Box>
      </Box>
    </Box>
  );
};

export default ClassPage;