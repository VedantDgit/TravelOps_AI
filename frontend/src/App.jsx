import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import FlightPrediction from "./pages/FlightPrediction";
import GenderPrediction from "./pages/GenderPrediction";
import HotelRecommendation from "./pages/HotelRecommendation";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/flight" element={<FlightPrediction />} />
        <Route path="/gender" element={<GenderPrediction />} />
        <Route path="/recommendation" element={<HotelRecommendation />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;