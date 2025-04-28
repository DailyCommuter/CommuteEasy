import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import { ChakraProvider } from "@chakra-ui/react";
// import system here
import { system } from "@chakra-ui/react/preset";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <ChakraProvider value={system}>
      {/* Firebase Auth Provider here wrapping arround <App/> */}
      <App />
    </ChakraProvider>
  </StrictMode>
);
