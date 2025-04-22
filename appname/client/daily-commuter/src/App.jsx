// App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import WelcomePage from "./pages/welcome-page";
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />

        {/* Catch-all route for 404s */}
        {/* <Route path="*" element={<NotFound />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
