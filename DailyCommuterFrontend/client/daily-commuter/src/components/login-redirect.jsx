import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/auth_context";

const LoginRedirect = () => {
  const { userLoggedin } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (userLoggedin && location.pathname === "/") {
      navigate("/home");
    }
  }, [userLoggedin, navigate]);

  return null;
};

export default LoginRedirect;
