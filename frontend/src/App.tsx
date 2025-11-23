import { ThemeProvider } from "@mui/material/styles";
import { CssBaseline } from "@mui/material";
import { Routes, Route } from "react-router-dom";
import { QueryClientProvider, QueryClient } from "@tanstack/react-query";
import LoginPage from "./pages/LoginPage";
import IndexPage from "./pages/IndexPage";
import SigninPage from "./pages/SigninPage";
import DashboardPage from "./pages/DashboardPage";
import { UserProvider } from "./contexts/UserContext";
import theme from "./utils/theme";
import ProfilePage from "./pages/ProfilePage";
import ClassPage from "./pages/ClassPage";

function App() {
  return (
    <QueryClientProvider client={new QueryClient()}>
      
      <UserProvider>  
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <div className="App">
              <Routes>
                <Route path="/" element={<IndexPage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/signin" element={<SigninPage />} />
                <Route path="/home" element={<DashboardPage />} />
                <Route path="/profile" element={<ProfilePage />} />
                <Route path="/video_class" element={<ClassPage />} />
              </Routes>
          </div>
        </ThemeProvider>
      </UserProvider>  
    </QueryClientProvider>
  );
}

export default App;
