import React from "react";
import {
  Drawer,
  Toolbar,
  ListItem,
  ListItemIcon,
  ListItemButton,
  List,
  Box,
  ListItemText,
  useTheme,
} from "@mui/material";
import { Link, NavLink } from "react-router-dom"; // Corrigido a importação

const drawerWidth = 240;

interface DrawerProps {
  menuItemLinks: Array<[React.ReactNode, string]>;
  open: boolean;
}

export const DrawerComponent: React.FC<DrawerProps> = ({
  menuItemLinks,
  open,
}) => {
  const theme = useTheme();
  const appBarHeight = theme.mixins.toolbar.minHeight;
  
  return (
    <Drawer
      variant="persistent"
      open={open}
      sx={{
        width: open ? drawerWidth : 0,
        flexShrink: 0,
        [`& .MuiDrawer-paper`]: {
          width: drawerWidth,
          boxSizing: "border-box",
          top: appBarHeight,
          height: `calc(100vh - ${appBarHeight})`,
          transition: (theme) =>
            theme.transitions.create("transform", {
              easing: theme.transitions.easing.sharp,
              duration: theme.transitions.duration.enteringScreen,
            }),
          transform: open ? "translateX(0)" : `translateX(-${drawerWidth}px)`,
        },
      }}
    >
      <Box sx={{ overflow: "auto" }}>
        <List>
          {menuItemLinks.map((item) => (
            <NavLink 
              to={`/${item[1]}`.toLowerCase()} 
              key={item[1]}
              style={{ 
                textDecoration: "none", 
                color: "inherit" 
              }}
            >
              <ListItem 
                sx={{
                  color: theme.palette.text.primary,
                  textDecoration: "none",
                  fontWeight: "bold"
                }} 
                disablePadding
              >
                <ListItemButton>
                  <ListItemIcon>{item[0]}</ListItemIcon>
                  <ListItemText primary={item[1].replace("_", " ")} />
                </ListItemButton>
              </ListItem>
            </NavLink>
          ))}
        </List>
      </Box>
    </Drawer>
  );
};