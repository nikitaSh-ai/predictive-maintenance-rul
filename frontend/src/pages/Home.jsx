import PageHeader from "../components/common/PageHeader";
import MetricCard from "../components/common/MetricCard";
import PipelineStep from "../components/common/PipelineStep";
import QuickActionCard from "../components/common/QuickActionCard";

function Home() {
  return (
    <div className="space-y-8">

      {/* Page Heading */}
      <PageHeader
    title="Dashboard Overview"
    description="Industrial AI Decision Support System for Remaining Useful Life Prediction."
/>


<div
    className="
        rounded-2xl
        bg-gradient-to-r
        from-blue-600
        to-cyan-500
        text-white
        p-8
        shadow-lg
    "
>

    <p className="text-lg">

        🚀 AI Powered Predictive Maintenance

    </p>

    <h2
        className="
            text-4xl
            font-bold
            mt-3
        "
    >

        Remaining Useful Life Estimation &
        Maintenance Decision Support

    </h2>

    <p className="mt-5 text-blue-100 leading-7">

        This dashboard predicts the Remaining Useful
        Life of turbofan engines using a GRU based deep
        learning model together with Explainable AI,
        Monte Carlo Dropout uncertainty estimation,
        and an intelligent maintenance recommendation
        engine.

    </p>

</div>




      {/* Metrics */}
      <div className="grid grid-cols-1  md:grid-cols-2
lg:grid-cols-4 gap-6">

        <MetricCard
          title="Production Model"
          value="GRU"
        />

        <MetricCard
          title="System Status"
          value="Online"
          color="text-green-600"
        />

        <MetricCard
          title="Best R² Score"
          value="0.9019"
        />

        <MetricCard
    title="Input Features"
    value="17"
/>

      </div>


      {/* AI Pipeline */}

      <div>

        <h2 className="text-2xl font-bold text-gray-800">
        AI Prediction Workflow
        </h2>

         <p className="text-gray-500 mb-8">

The complete industrial prediction pipeline,
from raw engine sensor data to intelligent
maintenance recommendations.

</p>

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

          <div className="grid grid-cols-1 md:grid-cols-2
lg:grid-cols-4 gap-6">

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

          <QuickActionCard
    title="Decision Intelligence"
    description="View AI generated maintenance recommendations."
    icon="🛠"
    to="/decision-intelligence"
/>

          </div>

      </div>

      <div className="text-center pt-8">

    <p className="text-sm text-gray-400">

        Powered by PyTorch, FastAPI, React, Captum,
        Monte Carlo Dropout and NASA C-MAPSS Dataset.

    </p>

</div>

    </div>
  );
}

export default Home;  