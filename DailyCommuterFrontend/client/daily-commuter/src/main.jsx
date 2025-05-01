import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import { ChakraProvider, extendTheme } from "@chakra-ui/react";
// import system here
import { system } from "@chakra-ui/react/preset";

//Firebase Auth Context
import { AuthProvider } from "./context/AuthContext";

// Extend Chakra UI theme with system preset
const theme = extendTheme(system);

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <ChakraProvider theme={theme}>
      <AuthProvider> 
        {/* Firebase Auth Provider here wrapping arround <App/> */}
        <App />
      </AuthProvider>
    </ChakraProvider>
  </StrictMode>
);
