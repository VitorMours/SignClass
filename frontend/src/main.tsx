// main.tsx
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from "react-router-dom";
import App from './App'; // Importe o App aqui

createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);