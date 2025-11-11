import React, { useState } from "react";
import { Avatar, Button, Box, Paper } from "@mui/material";
import { LayoutComponent } from "../layout/DashboardLayout";
import { Camera, Dashboard, Person, Search, Translate } from "@mui/icons-material";


interface ProfilePageProps{
  title? : string
}

const ProfilePage: React.FC<ProfilePageProps> = ({ title = "SignClass"}) => {

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
          <Paper elevation={8} sx={{ display:"flex", justifyContent:"center", mx:'auto', mt:12, height:"70vh", width:"80vw", }}>
            <Avatar sx={{width:  128, height: 128, transform:'translateY(-50%)' }} variant="rounded">

            </Avatar>

          </Paper>
        
      </LayoutComponent>    
    </>
  );

}

export default ProfilePage;
