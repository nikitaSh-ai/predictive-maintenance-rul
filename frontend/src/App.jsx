import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import PredictRUL from "./pages/PredictRUL";
import ModelComparison from "./pages/ModelComparison";
import Explainability from "./pages/Explainability";
import Uncertainty from "./pages/Uncertainty";
import DecisionIntelligence from "./pages/DecisionIntelligence";
import About from "./pages/About";

import EngineAnalysis from "./pages/EngineAnalysis";


import MainLayout from "./layouts/MainLayout";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout><Home /></MainLayout>} />
        <Route path="/predict" element={<MainLayout><PredictRUL /></MainLayout>} />
        <Route path="/comparison" element={<MainLayout><ModelComparison /></MainLayout>} />
        <Route path="/explainability" element={<MainLayout><Explainability /></MainLayout>} />
        <Route path="/uncertainty" element={<MainLayout><Uncertainty /></MainLayout>} />
        <Route path="/decision-intelligence" element={<MainLayout><DecisionIntelligence /></MainLayout>} />
        <Route path="/about" element={<MainLayout><About /></MainLayout>} />
        <Route
    path="/engine-analysis"
    element={<EngineAnalysis />}
/>
   <Route
    path="/explainability"
    element={<Explainability />}
/>

   <Route
    path="/uncertainty"
    element={<Uncertainty />}
/>

      </Routes>
    </BrowserRouter>
  );
}

export default App;