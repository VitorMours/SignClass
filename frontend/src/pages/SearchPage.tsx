import React, { useState, useEffect } from "react";
import { LayoutComponent } from "../layout/DashboardLayout";
import { Camera, Dashboard, Person, Search } from "@mui/icons-material";
import { Box, Container, Autocomplete, TextField } from "@mui/material";
import signService from "../services/signService";

interface SearchOption {
  id: number;
  name: string;
  meaning?: string;
}

const SearchPage: React.FC = () => {
  const [open, setOpen] = useState(false);
  const [searchInput, setSearchInput] = useState("");
  const [searchOptions, setSearchOptions] = useState<SearchOption[]>([]); // Adicione o tipo aqui  const [loading, setLoading] = useState(false);

  function toggleDrawer(newOpen: boolean) {
    setOpen(newOpen);
  }

  const menuItemLinks: Array<[React.ReactNode, string]> = [
    [<Dashboard />, "Home"],
    [<Person />, "Profile"],
    [<Search />, "Search"],
    [<Camera />, "Video_Class"],
  ];

  async function fetchSearchInput(searchInput: string) {
    if (!searchInput.trim()) {
      setSearchOptions([]);
      return;
    }
    
    try {
      const response = await signService.searchSigns(searchInput);
      
      // REMOVA a verificação response.ok - response já é o JSON
      console.log("Resposta da API:", response);
      
      // Verifique se response é um array
      if (Array.isArray(response)) {
        const options: any = response.map((item: any) => ({
          id: item.id,
          name: item.name, 
          meaning: item.meaning // fallback
        }));
        setSearchOptions(options);
        console.log("Opções mapeadas:", options);
      } else {
        console.error("Resposta não é um array:", response);
        setSearchOptions([]);
      }

    } catch (error) {
      console.error(`Erro ao buscar os dados: ${error}`);
      setSearchOptions([]);
    } finally {
    }
  }

  useEffect(() => {
    const timer = setTimeout(() => {
      fetchSearchInput(searchInput);
    }, 500);

    return () => clearTimeout(timer);
  }, [searchInput]);

  return (
    <>
      <LayoutComponent
        title={"SignClass"}
        open={open}
        onToggleDrawer={toggleDrawer}
        menuItemLinks={menuItemLinks}
      >
        <Container>
          <Box sx={{ display: "flex", justifyContent: "center", mt: 4 }}>
            <Autocomplete 
              sx={{ width: 300 }} 
              options={searchOptions}
              onInputChange={(event, newValue) => {
                setSearchInput(newValue);
              }}
              getOptionLabel={(option) => `${option.name}: ${option.meaning}` || ""}
              renderInput={(params) => (
                <TextField 
                  {...params} 
                  label="Search a Sign..." 
                 
                />
              )}
            />
          </Box>
        </Container>
      </LayoutComponent>
    </>
  );
};

export default SearchPage;