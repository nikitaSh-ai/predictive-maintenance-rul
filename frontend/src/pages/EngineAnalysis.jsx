import { useLocation } from "react-router-dom";
import { useContext } from "react";
import { PredictionContext } from "../context/PredictionContext";
import DecisionIntelligence from "../components/analysis/DecisionIntelligence";
import EngineOverview from "../components/analysis/EngineOverview";
import ExplainabilityCard from "../components/analysis/ExplainabilityCard";
import NoPredictionCard from "../components/common/NoPredictionCard";

function EngineAnalysis() {

    const location = useLocation();

    const { selectedEngine } = useContext(PredictionContext);

    const prediction = location.state || selectedEngine;

    if (!prediction) {

        return <NoPredictionCard icon="🔧" />;

    }

    return (

        <div
            className="
                max-w-7xl
                mx-auto
                px-6
                py-8
                space-y-8
            "
        >

            <div>

                <h1 className="text-4xl font-bold">

                    Engine Analysis Workspace

                </h1>

                <p className="text-gray-500 mt-2">

                    Complete diagnostic and maintenance insights for the selected engine.

                </p>

            </div>

            <EngineOverview
                prediction={prediction}
            />

            <DecisionIntelligence
                prediction={prediction}
            />

            <ExplainabilityCard prediction={prediction} />

        </div>

    );

}

export default EngineAnalysis;