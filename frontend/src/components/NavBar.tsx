import React from "react";
import { NavLink } from "react-router-dom";
import { 
  AppBar, 
  Box, 
  Toolbar, 
  Typography, 
  useTheme, 
  Container 
} from "@mui/material";

interface NavbarProps {
  logoText?: string;
}

const Navbar: React.FC<NavbarProps> = ({ logoText = "SignClass" }) => {
  const theme = useTheme();

  return (
    <AppBar 
      position="fixed"
      sx={{
        backgroundColor: theme.palette.background.paper,
        color: theme.palette.text.primary,
      }}
    >
      <Container maxWidth="xl" sx={{ padding: "0 !important" }}>
        <Toolbar sx={{ justifyContent: "space-between", padding: "0 !important" }}>
          <Typography 
            variant="h5" 
            sx={{
              fontWeight: "bold",
              whiteSpace: "nowrap",
            }}
          >
            {logoText}
          </Typography>
          <Box sx={{ display: "flex", gap: 3, alignItems: "center" }}>
            <NavLink
              to="/login"
              style={({ isActive }) => ({
                color: isActive ? theme.palette.primary.main : theme.palette.text.primary,
                fontWeight: isActive ? "bold" : "normal",
                textDecoration: "none",
                whiteSpace: "nowrap",
                padding: "8px 0",
              })}
            >
              Login
            </NavLink>
            <NavLink
              to="/signin"
              style={({ isActive }) => ({
                color: isActive ? theme.palette.primary.main : theme.palette.text.primary,
                fontWeight: isActive ? "bold" : "normal",
                textDecoration: "none",
                whiteSpace: "nowrap",
                padding: "8px 0",
              })}
            >
              Signin
            </NavLink>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Navbar;