import React, { useState, useRef } from "react";
import { Box, Paper, CardMedia, Typography, Button, Link, CircularProgress } from "@mui/material";
import { Link as RouterLink, useNavigate } from "react-router";
import FormField from "../components/FormField";
import Navbar from "../components/NavBar";
import authService from "../services/authService";

const SigninPage: React.FC = () => {
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const emailRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);
  const firstNameRef = useRef<HTMLInputElement>(null);
  const lastNameRef = useRef<HTMLInputElement>(null);


  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setIsLoading(true)

    const email = emailRef.current?.value || "";
    const password = passwordRef.current?.value || "";
    const firstName = firstNameRef.current?.value || "";
    const lastName = lastNameRef.current?.value || "";

    if(!email || !password || !firstName || !lastName ){
      
      setIsLoading(false);
      setError(null);
      return;
    }
    console.log("vai recebendo");
    
    try{
      const signUpResponse = await authService.signup({
        first_name: firstName, 
        last_name: lastName, 
        email: email,
        password: password
      })
      const loginResponse = await authService.login({
        email: email, 
        password: password
      })

      if(signUpResponse.ok && loginResponse.ok && loginResponse.data.access ){
        navigate("/dashboard");
      } else {
        console.log('Falha no login:')
      }
    }catch(error){
      const errorMessage = "Erro ao fazer login";
      setError(errorMessage);
      console.error(`Houve um erro de carregamento: ${errorMessage}`);
    } finally {
      setIsLoading(false);
    } 
  }

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
            image="src/assets/login_form_image.jpg"
            alt="login_form_image"
            sx={{ width: "50%", objectFit: "cover" }}
          ></CardMedia>
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
            <Box sx={{ textAlign: "center", marginBottom: 2 }}>
              <Typography variant="h4" sx={{ margin: 1 }}>
                Sign in
              </Typography>
              <Typography variant="caption">
                Aprenda a ouvir oque as pessoas tem a falar, com os olhos...
              </Typography>
            </Box>

            <Box
              component="form"
              onSubmit={handleSubmit}
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                width: "100%",
              }}
            >
              <Box
                sx={{
                  display: "flex",
                  justifyContent: "space-between",
                  width: "80%",
                  gap: 1,
                }}
              >
                <FormField
                  sx={{ margin: 0, marginBottom: 1 }}
                  label={"Nome"}
                  type={"text"}
                  required={true}
                  inputRef={firstNameRef}
                />
                <FormField
                  sx={{ margin: 0, marginBottom: 1 }}
                  label={"Sobrenome"}
                  type={"text"}
                  required={false}
                  inputRef={lastNameRef}
                />
              </Box>
              <FormField label={"Email"} type={"email"} required={true}  inputRef={emailRef}/>
              <FormField label={"Senha"} type={"password"} required={true} inputRef={passwordRef}/>
              <Link
                component={RouterLink}
                to="/login"
                sx={{
                  marginX: "10%",
                  display: "flex",
                  alignSelf: "end",
                  fontSize: "80%",
                }}
              >
                Ja possui uma conta? Entao faca login
              </Link>
              <Button
                variant="contained"
                color="primary"
                type="submit"
                disabled={isLoading}
                sx={{ marginTop: 5, width: "50%" }}
              >
                {isLoading ? <CircularProgress size={24} />: "Submit"}
              </Button>
            </Box>
          </Box>
        </Paper>
      </Box>
    </>
  );
};

export default SigninPage;
