import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import { ChakraProvider } from "@chakra-ui/react";
// import system here
import { system } from "@chakra-ui/react/preset";
import { AuthProvider } from "./contexts/auth_context.jsx";
import LoginRedirect from "./components/login-redirect.jsx";
import { BrowserRouter } from "react-router-dom";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <ChakraProvider value={system}>
      <BrowserRouter>
        {" "}
        {/* ✅ Wrap here */}
        <AuthProvider>
          <LoginRedirect />
          <App />
        </AuthProvider>
      </BrowserRouter>
    </ChakraProvider>
  </StrictMode>
);
