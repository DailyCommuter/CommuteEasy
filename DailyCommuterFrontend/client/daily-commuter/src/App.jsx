// App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import WelcomePage from "./pages/welcome-page";
import HomePage from "./pages/home";
import CommutingPage from "./pages/commuting-page";
import ProtectedRoute from "./context/ProtectedRoute";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        
        {/* Protected Routes*/}
        <Route path="/home" element={<ProtectedRoute> <HomePage /> </ProtectedRoute>} />
        <Route path="/commuting" element={<ProtectedRoute> <CommutingPage /> </ProtectedRoute>} />

        {/* Catch-all route for 404s */}
        {/* <Route path="*" element={<NotFound />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
