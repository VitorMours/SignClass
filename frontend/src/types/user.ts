export interface User {

    id: number,
    email: string,
    first_name: string,
    last_name: string,
}

export interface userState{
    user: User | null;
    isAuthenticated: boolean;

}


export type UserAction =
  | { type: 'SET_LOADING'; payload: boolean }
  | { type: 'SET_USER'; payload: User | null }
  | { type: 'UPDATE_USER'; payload: Partial<User> }
  | { type: 'UPDATE_PROFILE'; payload: Partial<User> }
  | { type: 'SET_ERROR'; payload: string | null }
  | { type: 'LOGOUT' }
  | { type: 'CLEAR_ERROR' };