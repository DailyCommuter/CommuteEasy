// App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import WelcomePage from "./pages/welcome-page";
import HomePage from "./pages/home";
import CommutingPage from "./pages/commuting-page";
import ProtectedRoute from "./context/ProtectedRoute";

function App() {
  return (

    <Routes>
      <Route path="/" element={<WelcomePage />} />
      <Route path="/home" element={<HomePage />} />
      <Route path="/commuting" element={<CommutingPage />} />


      {/* Catch-all route for 404s */}
      {/* <Route path="*" element={<NotFound />} /> */}
    </Routes>
  );
}

export default App;
