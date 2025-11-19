import React from "react";
import { Box, Skeleton, useTheme } from "@mui/material";

const SignCardSkeleton: React.FC = () => {
  const theme = useTheme();

  return (
    <Box
      sx={{
        width: 345,
        height: 360,
        borderRadius: 0,
        borderWidth: 1,
        borderStyle: "solid",   // necessário
        borderColor: theme.palette.divider, // usa a cor de borda padrão do tema
        backgroundColor: theme.palette.background.paper,
        display: "flex",
        flexDirection: "column",
        gap: 1.5,
      }}
    >
      {/* Imagem/vídeo */}
      <Skeleton sx={{ bgcolor: "whitesmoke" }} variant="rectangular" height={150}/>

      {/* Título */}
      <Skeleton sx={{ marginLeft: 1 }} variant="rectangular" width="70%" height="10%" animation="wave" />
      <Skeleton sx={{ marginLeft: 1 }} variant="text" width="70%" animation="wave" />

      {/* Descrição */}
      <Skeleton sx={{ marginLeft: 1 }} variant="text" width="50%" animation="wave" />
      <Skeleton sx={{ marginLeft: 1 }} variant="text" width="70%" animation="wave" />
      <Skeleton sx={{ marginLeft: 1 }} variant="text" width="60%" animation="wave" />
      <Skeleton sx={{ marginLeft: 1, marginBottom: 1 }} variant="text" width="30%" animation="wave" />
    </Box>
  );
};

export default SignCardSkeleton;
