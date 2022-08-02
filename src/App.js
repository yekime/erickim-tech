import React from "react";
import "./App.css";
import Home from "./components/pages/Home";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Demos from "./components/pages/Demos";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="demos" element={<Demos />}></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
