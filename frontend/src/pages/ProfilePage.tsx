import React, { useState } from "react";
import { Avatar, Button, Box, Paper, Typography, Container } from "@mui/material";
import { LayoutComponent } from "../layout/DashboardLayout";
import { Camera, Dashboard, Person, Search, Translate } from "@mui/icons-material";
import useUser from "../hooks/useUser";

interface ProfilePageProps{
  title? : string
}


const ProfilePage: React.FC<ProfilePageProps> = ({ title = "SignClass"}) => {


  const { user } = useUser();
  const [open, setOpen] = useState(false);

  function toggleDrawer(newOpen: boolean) {
    setOpen(newOpen);
  } 

  const menuItemLinks: Array<[React.ReactNode, string]> = [
    [<Dashboard />, "Home"],
    [<Person />, "Profile"],
    [<Search />, "Search"],
    [<Camera />, "Video_Class"],
  ];

  return (
    <>
      <LayoutComponent
        title={title}
        open={open}
        onToggleDrawer={toggleDrawer}
        menuItemLinks={menuItemLinks}>
        
        <Container 
          maxWidth={false} 
          sx={{ 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center',
            minHeight: '100vh',
            py: 4,
            px: { xs: 2, sm: 3, md: 4 }
          }}
        >
          <Paper 
            elevation={8} 
            sx={{ 
              position: 'relative',
              display: "flex", 
              flexDirection: "column",
              alignItems: "center", 
              justifyContent: "flex-start",
              mx: 'auto', 
              mt: { xs: 8, md: 12 },
              mb: 4,
              height: { xs: "60vh", sm: "65vh", md: "70vh" },
              width: { 
                xs: "95vw", 
                sm: "90vw", 
                md: "85vw", 
                lg: "80vw",
                xl: "75vw"
              },
              maxWidth: "1200px",
              minHeight: "400px",
              pt: 8,
              pb: 4,
              px: { xs: 2, sm: 3, md: 4 }
            }}
          >
            <Avatar 
              sx={{
                width: { xs: 96, sm: 112, md: 128, lg: 144 },
                height: { xs: 96, sm: 112, md: 128, lg: 144 },
                position: 'absolute',
                top: 0,
                transform: 'translateY(-50%)',
                border: '4px solid white',
                boxShadow: 3
              }} 
              variant="rounded"
            >
              
            </Avatar>

            <Box 
              sx={{ 
                mt: { xs: 6, md: 8 },
                width: '100%',
                textAlign: 'center'
              }}
            >
              <Typography 
                variant="h4" 
                component="h1"
                sx={{
                  fontSize: { xs: '1.5rem', sm: '2rem', md: '2.5rem' },
                  mb: 2
                }}
              >
                {user ? `${user.first_name} ${user.last_name}` : "Nome do Usuário"}
              </Typography>
              
              <Typography 
                variant="body1"
                sx={{
                  fontSize: { xs: '0.9rem', sm: '1rem', md: '1.1rem' },
                  color: 'text.secondary',
                  maxWidth: '600px',
                  mx: 'auto'
                }}
              >
                Informações do perfil ou conteúdo adicional podem ser colocadas aqui.
              </Typography>

              {/* Botões responsivos */}
              <Box 
                sx={{ 
                  mt: 4,
                  display: 'flex',
                  flexDirection: { xs: 'column', sm: 'row' },
                  gap: 2,
                  justifyContent: 'center',
                  alignItems: 'center'
                }}
              >
                <Button 
                  variant="contained" 
                  size="small"
                  sx={{ 
                    minWidth: { xs: '100%', sm: '140px' }
                  }}
                >
                  Editar Perfil
                </Button>
                <Button 
                  variant="outlined" 
                  size="small"
                  sx={{ 
                    minWidth: { xs: '100%', sm: '140px' }
                  }}
                >
                  Configurações
                </Button>
              </Box>
            </Box>
          </Paper>
        </Container>
        
      </LayoutComponent>    
    </>
  );
}

export default ProfilePage;