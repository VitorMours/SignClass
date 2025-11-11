// authService.ts
import type { 
    LoginCredentialsInterface, 
    AuthApiResponse, 
    SignUpCredentials,
    User
} from "../interfaces/authInterface";

import userService from "./userService";

const authService = {

    login: async (data: LoginCredentialsInterface): Promise<AuthApiResponse> => {
        const response = await fetch('/api/auth/login', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: data.email,
                password: data.password,
            })
        });
        
        const responseData = await response.json().catch(() => null);
        
        if (!response.ok) {
            throw new Error(responseData?.message || `HTTP error! status: ${response.status}`);
        }

        return {
            data: responseData,
            status: response.status,
            statusText: response.statusText,
            ok: response.ok
        };
    },

    signup: async (data: SignUpCredentials): Promise<AuthApiResponse> => {
        const response = await fetch('/api/auth/signup', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const responseData = await response.json().catch(() => null);

        if (!response.ok) {
            throw new Error(responseData?.message || `HTTP error! status: ${response.status}`);
        }

        return {
            data: responseData,
            status: response.status,
            statusText: response.statusText,
            ok: response.ok
        };
    },

    authorize: async (data: AuthApiResponse): Promise<User | string> => {
        localStorage.setItem("refresh", data.data.refresh);
        localStorage.setItem("access", data.data.access);
        localStorage.setItem("email", data.data.email);

        try{
            const response = await userService.getUserData(data.data.email);
            const userData = response.data[0];
            return userData;

        }catch(error){
            console.log(error);
            return "Visitante";
        }

    }
};

export default authService;