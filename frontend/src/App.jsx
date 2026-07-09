import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import PredictRUL from "./pages/PredictRUL";
import ModelComparison from "./pages/ModelComparison";
import Explainability from "./pages/Explainability";
import Uncertainty from "./pages/Uncertainty";
import DecisionIntelligence from "./pages/DecisionIntelligence";
import About from "./pages/About";



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
        <Route path="/decision" element={<MainLayout><DecisionIntelligence /></MainLayout>} />
        <Route path="/about" element={<MainLayout><About /></MainLayout>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;