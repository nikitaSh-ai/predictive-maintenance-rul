import { useEffect, useState } from "react";

import ErrorCard from "../components/common/ErrorCard";

import { getExplainability } from "../services/api";

import LoadingSpinner from "../components/common/LoadingSpinner";


import FeatureImportanceCard from "../components/explainability/FeatureImportanceCard";

function Explainability() {

    const [featureImportance, setFeatureImportance] = useState({});

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    useEffect(() => {

        async function fetchExplainability() {

            try {

const data = await getExplainability();

if (!data.feature_importance) {

    setFeatureImportance({});

    return;

}

                setFeatureImportance(
                    data.feature_importance
                );

            }

            catch (error) {

                console.error(error);

setError(
    "Unable to load feature importance."
);
            }

            finally {

                setLoading(false);

            }

        }

        fetchExplainability();

    }, []);


   return (

    <div className="p-8">

        <h1
            className="
                text-3xl
                font-bold
                mb-8
            "
        >

            Explainability

        </h1>

    
{

loading

? (

    <LoadingSpinner
        title="Generating feature importance..."
    />

)

: error

? (

    <ErrorCard

        title="Explainability Error"

        message={error}

    />

)

: Object.keys(featureImportance).length === 0

? (

    <div
        className="
            mt-10
            bg-white
            border
            rounded-2xl
            shadow
            p-10
            text-center
        "
    >

        <div className="text-6xl">

            🧠

        </div>

        <h2
            className="
                text-2xl
                font-bold
                mt-6
            "
        >

            No Explainability Available

        </h2>

        <p
            className="
                mt-4
                text-gray-500
            "
        >

            Run a prediction first to generate
            feature importance values.

        </p>

    </div>

)

: (

    <FeatureImportanceCard

        featureImportance={featureImportance}

    />

)

}

        

        

    </div>

);

}

export default Explainability;