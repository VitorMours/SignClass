// HeaderComponent.tsx
import React from "react";
import {
  AppBar,
  Toolbar,
  Typography,
  IconButton,
  useTheme,
} from "@mui/material";
import { Menu } from "@mui/icons-material";

interface HeaderComponentProps {
  title?: string;
  open: boolean;
  onMenuClick: () => void;
}

export const HeaderComponent: React.FC<HeaderComponentProps> = ({
  title = "SignClass",
  open,
  onMenuClick,
}) => {
  const theme = useTheme();

  return (
    <AppBar
      position="fixed"
      sx={{
        width: '100%',
        zIndex: (theme) => theme.zIndex.drawer + 1,
        backgroundColor: theme.palette.background.paper,
        color: theme.palette.text.primary,
      }}
    >
      <Toolbar>
        <IconButton onClick={onMenuClick} sx={{ mr: 2 }}>
          <Menu />
        </IconButton>
        <Typography variant="h5">{title}</Typography>
      </Toolbar>
    </AppBar>
  );
};