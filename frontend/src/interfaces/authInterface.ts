export interface LoginCredentialsInterface {
    email: string;
    password: string;
}

export interface LoginResponseInterface{
    access: string;
    refresh: string;
    email: string;
    status?: string;
}

export interface AuthApiResponse {
    data: LoginResponseInterface;
    status: number;
    statusText: string;
    ok: boolean;
}

export interface SignUpCredentials {
    first_name: string;
    last_name: string;
    email: string;
    password: string;
}

export interface User {
    id: string;
    email: string;
    first_name: string;
    last_name: string;
}


