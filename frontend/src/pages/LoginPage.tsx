import React, { useRef, useState } from "react";
import type { User } from "../interfaces/entityInterface";
import type { LoginResponseInterface } from "../interfaces/authInterface";
import {
  Box,
  Paper,
  CardMedia,
  Typography,
  Button,
  Link,
  CircularProgress,
  Alert,
} from "@mui/material";

import { Link as RouterLink, useNavigate } from "react-router-dom";
import FormField from "../components/FormField";
import authService from "../services/authService";
import Navbar from "../components/NavBar";
import useUser from "../hooks/useUser";

const LoginPage: React.FC = () => {

  const user = useUser();
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setIsLoading(true);
    setError(null);

    const email = emailRef.current?.value || "";
    const password = passwordRef.current?.value || "";

    if (!email || !password) {
      setError("Por favor, preencha todos os campos");
      setIsLoading(false);
      return;
    }

    try {
      const response = await authService.login({
        email: email,
        password: password
      });
      
      if (response.ok && response.data.access) {
        const userData = await authService.authorize(response);
        

        if (typeof userData  === 'object'){
          user.setUser(userData);        
        } else{
          user.setUser(null);        
        }
        
        navigate("/home");
      } else {
        console.log('Falha no login:', {
          ok: response.ok,
          hasToken: Boolean(response.data?.access)
        });
      }
    } catch (error: any) {
      const errorMessage =
        error.response?.data?.message || "Erro ao fazer login";
      setError(errorMessage);
      console.error(`Houve um erro de carregamento: ${errorMessage}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <Navbar />
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100dvh",
          padding: 2,
        }}
      >
        <Paper
          elevation={2}
          sx={{ display: "flex", height: "65%", width: "65%" }}
        >
          <CardMedia
            component="img"
            image="src/assets/signin_form_image.webp"
            alt="signin_form_image"
            sx={{ width: "50%", objectFit: "cover" }}
          />
          <Box
            sx={{
              padding: "12px",
              border: "1px solid lightgray",
              display: "flex",
              width: "50%",
              flexDirection: "column",
              justifyContent: "space-evenly",
              alignItems: "center",
            }}
          >
            <Box sx={{ textAlign: "center", marginBottom: 2, height: "10%" }}>
              <Typography variant="h4" sx={{ margin: 1 }}>
                Login
              </Typography>
              <Typography variant="caption">
                Vendo oque as pessoas tem a dizer
              </Typography>
            </Box>

            <Box
              component="form"
              onSubmit={handleSubmit}
              method="post"
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                width: "100%",
                height: "50%",
              }}
            >
              {error && (
                <Alert severity="error" sx={{ width: "80%", mb: 2 }}>
                  {error}
                </Alert>
              )}

              <FormField
                label={"Email"}
                type={"email"}
                required={true}
                inputRef={emailRef}
              />
              <FormField
                label={"Password"}
                type={"password"}
                required={true}
                inputRef={passwordRef}
              />
              <Link
                component={RouterLink}
                to="/signin"
                sx={{
                  marginX: "10%",
                  display: "flex",
                  alignSelf: "end",
                  fontSize: "80%",
                }}
              >
                nao possui cadastro? Faca a sua conta.
              </Link>
              <Button
                variant="contained"
                color="primary"
                type="submit"
                disabled={isLoading}
                sx={{ marginTop: 5, width: "50%" }}
              >
                {isLoading ? <CircularProgress size={24} /> : "Log in"}
              </Button>
            </Box>
          </Box>
        </Paper>
      </Box>
    </>
  );
};

export default LoginPage;
