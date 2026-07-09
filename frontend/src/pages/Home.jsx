import MetricCard from "../components/common/MetricCard";
import PipelineStep from "../components/common/PipelineStep";
import QuickActionCard from "../components/common/QuickActionCard";

function Home() {
  return (
    <div className="space-y-8">

      {/* Page Heading */}
      <div>
        <h1 className="text-3xl font-bold text-gray-800">
          Dashboard Overview
        </h1>

        <p className="text-gray-500 mt-2">
          Industrial AI Decision Support System for Remaining Useful Life Prediction.
        </p>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <MetricCard
          title="Primary Model"
          value="GRU"
        />

        <MetricCard
          title="Backend Status"
          value="Online"
          color="text-green-600"
        />

        <MetricCard
          title="Best R² Score"
          value="0.9019"
        />

      </div>


      {/* AI Pipeline */}

      <div>

        <h2 className="text-2xl font-bold text-gray-800 mb-8">
        AI Prediction Pipeline
        </h2>

        <div className="flex flex-col items-center">

          <PipelineStep title="NASA C-MAPSS Dataset" />

          <PipelineStep title="Data Preprocessing" />

          <PipelineStep title="Feature Engineering" />

          <PipelineStep title="GRU Prediction Model" />

          <PipelineStep title="Explainable AI (Captum)" />

          <PipelineStep title="Uncertainty Estimation" />

           <PipelineStep title="Decision Intelligence" />

           <PipelineStep title="Maintenance Recommendation" isLast={true}/>

        </div>

      </div>


      {/* Quick Actions */}

      <div>

          <h2 className="text-2xl font-bold text-gray-800 mb-8">
            Quick Actions
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

          <QuickActionCard
            title="Predict RUL"
            description="Run AI prediction on engine data."
            icon="🤖"
            to="/predict"
          />

          <QuickActionCard
            title="Explainability"
            description="Understand model predictions using Captum."
            icon="🧠"
            to="/explainability"
          />

          <QuickActionCard
            title="Model Comparison"
            description="Compare Random Forest, XGBoost and GRU."
            icon="📊"
            to="/comparison"
          />

          </div>

      </div>

    </div>
  );
}

export default Home;  