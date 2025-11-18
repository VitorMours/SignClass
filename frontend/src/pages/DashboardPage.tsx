// DashboardPage.tsx
import React, { useState } from "react";
import {
  Box,
  CssBaseline,
  Typography,
  Stack,
  Divider,
  useTheme,
} from "@mui/material";

import { Camera, Dashboard, Person, Search } from "@mui/icons-material";
import { LayoutComponent } from "../layout/DashboardLayout";
import SignCard from "../components/SignCard";
import useUser from "../hooks/useUser";

interface DashboardBarProps {
  title?: string;
}

export const DashboardPage: React.FC<DashboardBarProps> = ({
  title = "SignClass",
}) => {
  const theme = useTheme();
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

  // Função para renderizar os cards
  const renderSignCards = () => {
    const cards = [];
    for (let i = 0; i < 10; i++) {
      cards.push(
        <SignCard
          key={i}
          name={`Reptile ${i + 1}`}
          meaning="The reptile is a incredible animal"
          hand_configuration="gesto italiano"
          articulation_point="head"
          movement="circular"
          body_expression="expressivamente"
          direction_and_orientation="em direcao aa testa"
        />
      );
    }
    return cards;
  };

  return (
    <>
      <CssBaseline />
      <LayoutComponent
        title={title}
        open={open}
        onToggleDrawer={toggleDrawer}
        menuItemLinks={menuItemLinks}
      >
        <Stack direction="column" spacing={3} sx={{ width: "100%" }}>
          <Typography variant="h4">
            Bem vindo, {user?.first_name || "Visitante"}!
          </Typography>

          <Box
            sx={{
              display: "flex",
              gap: 2,
              flexWrap: "wrap",
              alignItems: "flex-start",
              width: "100%",
            }}
          >
            <Box sx={{ flex: 1, minWidth: 280 }}>
              <Typography
                variant="h6"
                sx={{ color: theme.palette.primary.main, mb: 2 }}
              >
                Últimas pesquisas
              </Typography>
              <Box
                sx={{
                  display: "grid",
                  gap: 2,
                  gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
                }}
              >
                {renderSignCards()}
              </Box>
            </Box>

            <Divider orientation="vertical" flexItem />

            <Box sx={{ flex: 1, minWidth: 280 }}>
              <Typography
                variant="h6"
                sx={{ mb: 2, color: theme.palette.primary.main }}
              >
                Seus sinais
              </Typography>
              <Box
                sx={{
                  display: "grid",
                  gap: 2,
                  gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
                }}
              >
                {renderSignCards()}
              </Box>
            </Box>
          </Box>
        </Stack>
      </LayoutComponent>
    </>
  );
};

export default DashboardPage;
