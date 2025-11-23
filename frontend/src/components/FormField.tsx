import React from "react";
import { TextField } from "@mui/material";

interface FormFieldProps {
    sx?: object;
    label?: string;
    type?: string;
    required?: boolean;
    inputRef?: React.Ref<HTMLInputElement>; // Mudei para Ref em vez de RefObject
}

const FormField: React.FC<FormFieldProps> = ({ sx, label, type, required, inputRef }) => {
    return(
        <TextField 
            variant="outlined" 
            sx={{ margin: 1, width: "80%", ...sx }}
            label={label}
            type={type} 
            required={required}
            inputRef={inputRef}
        />
    );
}

export default FormField;