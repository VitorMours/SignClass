// LayoutComponent.tsx
import React from "react";
import { Box, Toolbar, useTheme } from "@mui/material";
import { HeaderComponent } from "../components/DashboardBar";
import { DrawerComponent } from "../components/DrawerComponent";

interface LayoutComponentProps {
  children: React.ReactNode;
  title?: string;
  open: boolean;
  onToggleDrawer: (newOpen: boolean) => void;
  menuItemLinks: Array<[React.ReactNode, string]>;
}

const drawerWidth = 240;

export const LayoutComponent: React.FC<LayoutComponentProps> = ({
  children,
  title,
  open,
  onToggleDrawer,
  menuItemLinks,
}) => {
  const theme = useTheme();

  return (
    <Box sx={{ display: "flex" }}>
      <HeaderComponent
        title={title}
        open={open}
        onMenuClick={() => onToggleDrawer(!open)}
      />
      
      <DrawerComponent menuItemLinks={menuItemLinks} open={open} />
      
      {/* Conteúdo principal */}
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          marginLeft: open ? `${drawerWidth}px` : 0,
          transition: (theme) => theme.transitions.create('margin', {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.enteringScreen,
          }),
        }}
      >
        <Toolbar /> {/* Espaço para a AppBar */}
        {children}
      </Box>
    </Box>
  );
};