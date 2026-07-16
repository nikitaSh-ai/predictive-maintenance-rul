import { useEffect, useState } from "react";

import { getUncertainty } from "../services/api";

import LoadingSpinner from "../components/common/LoadingSpinner";

import ErrorCard from "../components/common/ErrorCard";

function Uncertainty() {

  
  const [uncertaintyData, setUncertaintyData] = useState(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  


  useEffect(() => {

    async function fetchUncertainty() {

        try {

            const data = await getUncertainty();

console.log("Uncertainty API Response:", data);

setUncertaintyData(data);

        }

        catch (error) {

            console.error(error);

setError(
    "Unable to load uncertainty analysis."
);
        }

        finally {

            setLoading(false);

        }

    }

    fetchUncertainty();

}, []);
  
if (loading) {
    return (
        <LoadingSpinner
            title="Analyzing prediction uncertainty..."
        />
    );
}

if (error) {
    return (
        <ErrorCard
            title="Uncertainty Error"
            message={error}
        />
    );
}

if (!uncertaintyData) {
    return (
        <ErrorCard
            title="No Uncertainty Data"
            message="Run a prediction first to generate uncertainty analysis."
        />
    );
}

const predictionStability =
    uncertaintyData.uncertainty < 2
        ? "High"
        : uncertaintyData.uncertainty < 5
        ? "Moderate"
        : "Low";


return (

    <div className="p-8">

        <h1
            className="
                text-3xl
                font-bold
                mb-8
            "
        >

            Uncertainty Analysis

        </h1>

      



        <>


        <div
    className="
        grid
        grid-cols-1
        md:grid-cols-2
        lg:grid-cols-4
        gap-6
    "
>

    <div
        className="
            bg-blue-50
            border
            border-blue-200
            rounded-xl
            p-6
        "
    >

        <p className="text-gray-500">

            Confidence

        </p>

        <h2
            className="
                text-3xl
                font-bold
                text-blue-600
                mt-3
            "
        >

            {uncertaintyData.confidence}

        </h2>
        <p className="text-sm text-gray-400 mt-2">

    Prediction Confidence

</p>

    </div>

    <div
        className="
            bg-purple-50
            border
            border-purple-200
            rounded-xl
            p-6
        "
    >

        <p className="text-gray-500">

            Uncertainty

        </p>

        <h2
            className="
                text-3xl
                font-bold
                text-purple-600
                mt-3
            "
        >

            ±{uncertaintyData.uncertainty.toFixed(2)} cycles

        </h2>
        <p className="text-sm text-gray-400 mt-2">

    
Standard Deviation
</p>

    </div>

    <div
        className="
            bg-cyan-50
            border
            border-cyan-200
            rounded-xl
            p-6
        "
    >

        <p className="text-gray-500">

            Predicted RUL

        </p>

        <h2
            className="
                text-3xl
                font-bold
                text-cyan-600
                mt-3
            "
        >

            {uncertaintyData.predicted_rul.toFixed(2)} cycles

        </h2>
        <p className="text-sm text-gray-400 mt-2">

    Estimated Remaining Life

</p>

    </div>

    <div
        className="
            bg-red-50
            border
            border-red-200
            rounded-xl
            p-6
        "
    >

        <p className="text-gray-500">

            Risk Level

        </p>

        <h2
            className="
                text-3xl
                font-bold
                text-red-600
                mt-3
            "
        >

            {uncertaintyData.risk}

        </h2>
        <p className="text-sm text-gray-400 mt-2">

  Maintenance Priority

</p>

    </div>

</div>

<div
    className="
        mt-8
        bg-white
        border
        rounded-xl
        shadow
        p-6
    "
>

    <h2
        className="
            text-2xl
            font-bold
            mb-6
        "
    >

        Monte Carlo Summary

    </h2>

    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

        <div>

            <p className="text-gray-500">

                Mean Prediction

            </p>

            <h3
                className="
                    text-2xl
                    font-bold
                    text-blue-600
                    mt-2
                "
            >

               {uncertaintyData.mc_mean.toFixed(2)} cycles

            </h3>

        </div>

        <div>

            <p className="text-gray-500">

                Simulations

            </p>

            <h3
                className="
                    text-2xl
                    font-bold
                    text-green-600
                    mt-2
                "
            >

                {uncertaintyData.mc_samples.length}

            </h3>

        </div>

        <div>

            <p className="text-gray-500">

             Prediction Stability

            </p>

            <h3
                className="
                    text-2xl
                    font-bold
                    text-purple-600
                    mt-2
                "
            >

                {predictionStability}

            </h3>

        </div>

    </div>

</div>



<div
    className="
        mt-8
        bg-gradient-to-r
        from-blue-50
        to-cyan-50
        border
        rounded-xl
        p-6
    "
>

    <h2
        className="
            text-2xl
            font-bold
            mb-5
        "
    >

        🤖 AI Interpretation

    </h2>

    <p
        className="
            text-gray-700
            leading-8
        "
    >

        The GRU model predicts approximately{" "}

        <strong>

           {uncertaintyData.predicted_rul.toFixed(2)} cycles

        </strong>

        {" "}of Remaining Useful Life.

        Across{" "}

        <strong>

            {uncertaintyData.mc_samples.length}

        </strong>

        {" "}Monte Carlo simulations, the model produced an average prediction of{" "}

        <strong>

            {uncertaintyData.mc_mean.toFixed(2)} cycles

        </strong>

       {" "}with an uncertainty of{" "}

        <strong>

            ±{uncertaintyData.uncertainty.toFixed(2)} cycles

        </strong>

        .

        This indicates{" "}

        <strong>

             {predictionStability.toLowerCase()} confidence

        </strong>

        {" "}in the prediction.

    </p>
    <div
    className="
        mt-6
        p-4
        rounded-lg
        bg-white
        border-l-4
        border-blue-500
    "
>

    <p className="text-sm text-gray-600">

        This uncertainty estimate is generated using
        Monte Carlo Dropout, which performs multiple
        stochastic forward passes through the GRU model
        to estimate prediction reliability.

    </p>

</div>


<div className="mt-10 text-center">

    <p className="text-sm text-gray-400">

        Uncertainty estimates are generated using
        Monte Carlo Dropout and should be interpreted
        alongside Remaining Useful Life predictions.

    </p>

</div>

</div>


        </>
    






    </div>


);
}

export default Uncertainty;