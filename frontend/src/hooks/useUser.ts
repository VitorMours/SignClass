import { useUserContext } from '../contexts/UserContext';

export default function useUser() {
  const context = useUserContext();
  
  return {
    user: context.user,
    isAuthenticated: context.isAuthenticated,
    login: context.login,
    logout: context.logout,
    setUser: context.setUser
  };
}