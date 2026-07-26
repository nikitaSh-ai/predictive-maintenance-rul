import { useNavigate } from "react-router-dom";



function PredictionCard({ prediction }) {

    console.log(prediction);

    const navigate = useNavigate();

    if (!prediction) return null;

    function getRiskStyle(risk) {

        switch (risk.toLowerCase()) {

            case "low":
                return {
                    bg: "bg-green-50",
                    border: "border-green-200",
                    text: "text-green-600",
                    icon: "🟢",
                };

            case "medium":
                return {
                    bg: "bg-yellow-50",
                    border: "border-yellow-200",
                    text: "text-yellow-600",
                    icon: "🟡",
                };

            case "high":
                return {
                    bg: "bg-red-50",
                    border: "border-red-200",
                    text: "text-red-600",
                    icon: "🔴",
                };

            default:
                return {
                    bg: "bg-gray-50",
                    border: "border-gray-200",
                    text: "text-gray-600",
                    icon: "⚪",
                };

        }

    }

    const riskStyle = getRiskStyle(prediction.risk);

    

    const engineCondition =
        prediction.risk === "Low"
            ? "Healthy"
            : prediction.risk === "Medium"
            ? "Degrading"
            : "Critical";


  

    return (

        <div
            className="
                bg-white
                rounded-2xl
                shadow-lg
                border
                p-8
                mt-8
            "
        >

            <h2
                className="
                    text-3xl
                    font-bold
                    text-center
                "
            >
                Prediction Result
            </h2>

            <p className="text-center text-gray-500 mt-2">
    Engine {prediction.engine_id}
</p>

            <div className="mt-8 text-center">

                <h1
                    className="
                        text-6xl
                        font-extrabold
                        text-blue-600
                    "
                >
                 {prediction.predicted_rul}
                </h1>

                <p className="text-xl text-gray-600">
                    Cycles
                </p>

                <p className="mt-2 text-gray-500">
                    Remaining Useful Life
                </p>

            </div>

            {/* ================= Metrics ================= */}

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-10">

                {/* Risk */}

                <div
                    className={`
                        ${riskStyle.bg}
                        ${riskStyle.border}
                        rounded-xl
                        border
                        p-5
                    `}
                >

                    <p className="text-gray-500">
                        Risk Level
                    </p>

                    <h3
                        className={`
                            text-2xl
                            font-bold
                            mt-2
                            ${riskStyle.text}
                        `}
                    >
                        {riskStyle.icon} {prediction.risk}
                    </h3>

                </div>

                {/* Confidence */}

                <div
                    className="
                        bg-blue-50
                        border
                        border-blue-200
                        rounded-xl
                        p-5
                    "
                >

                    <p className="text-gray-500">
                        Confidence
                    </p>

                    <h3
                        className="
                            text-2xl
                            font-bold
                            text-blue-600
                            mt-2
                        "
                    >
                        {prediction.confidence}
                    </h3>

                </div>

                {/* Health Score */}

                <div
                    className="
                        bg-cyan-50
                        border
                        border-cyan-200
                        rounded-xl
                        p-5
                    "
                >

                    <p className="text-gray-500">
                        Health Score
                    </p>

                    <h3
                        className="
                            text-2xl
                            font-bold
                            text-cyan-600
                            mt-2
                        "
                    >
                        {prediction.health_score}%
                    </h3>

                </div>

                 {/* Uncertainty */}

                 <div
    className="
        bg-purple-50
        border
        border-purple-200
        rounded-xl
        p-5
    "
>

    <p className="text-gray-500">

        Uncertainty

    </p>

    <p className="text-xs text-gray-400 mt-1">

    Monte Carlo Dropout

</p>



    <h3
        className="
            text-2xl
            font-bold
            text-purple-600
            mt-2
        "
    >

        ±{Number(prediction.uncertainty).toFixed(2)}
        <p className="text-sm text-gray-500 mt-2">

    cycles

</p>

    </h3>

</div>


            </div>

            {/* ================= Recommendation ================= */}

            <div
                className="
                    mt-8
                    bg-gray-50
                    rounded-xl
                    border
                    p-6
                "
            >

                <h3 className="text-2xl font-bold mb-6">

                    🛠 Maintenance Recommendation

                </h3>


                <div className="mb-6">

    <span
        className={`
            inline-block
            px-4
            py-2
            rounded-full
            font-semibold
            ${riskStyle.bg}
            ${riskStyle.text}
        `}
    >

        {riskStyle.icon} {prediction.risk.toUpperCase()} PRIORITY

    </span>

</div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

                    <div>

                        <p className="text-sm text-gray-500">
                            🔧 Recommended Action
                        </p>

                        <p className="font-semibold mt-1">
                            {prediction.recommendation}
                        </p>

                    </div>

                    <div>

                        <p className="text-sm text-gray-500">
                           📅 Next Inspection
                        </p>

                        <p className="font-semibold mt-1">
                            {prediction.inspection}
                        </p>

                    </div>

                    <div>

                        <p className="text-sm text-gray-500">
                           🎯 Suggested Focus
                        </p>

                        <p className="font-semibold mt-1">
                            {prediction.focus}
                        </p>

                    </div>

                </div>

            </div>

            {/* ================= AI Summary ================= */}

            <div
                className="
                    mt-8
                    rounded-xl
                    border
                    bg-gradient-to-r
                    from-blue-50
                    to-cyan-50
                    p-6
                "
            >

                <h3 className="text-2xl font-bold mb-6">

                    🤖 AI Prediction Summary

                </h3>


                <div className="space-y-4">

    <div className="flex justify-between">

        <span className="text-gray-500">

            ✓ Engine Status

        </span>

        <span className="font-semibold">

            {engineCondition}

        </span>

    </div>

    <div className="flex justify-between">

        <span className="text-gray-500">

            ✓ Predicted RUL

        </span>

        <span className="font-semibold">
         {prediction.predicted_rul} Cycles

        </span>

    </div>

    <div className="flex justify-between">

        <span className="text-gray-500">

            ✓ Risk Level

        </span>

        <span className={riskStyle.text}>

            {prediction.risk}

        </span>

    </div>

    <div className="flex justify-between">

        <span className="text-gray-500">

            ✓ Confidence

        </span>

        <span className="font-semibold">

            {prediction.confidence}

        </span>

    </div>

    <div className="flex justify-between">

    <span className="text-gray-500">

        ✓ Uncertainty

    </span>

    <span className="font-semibold">

        ±{Number(prediction.uncertainty).toFixed(2)} cycles

    </span>

</div>

    <div className="flex justify-between">

        <span className="text-gray-500">

            ✓ Health Score

        </span>

        <span className="font-semibold">

            {prediction.health_score}%

        </span>

    </div>

    <hr className="my-5"/>

    <div>

        <p className="text-gray-500 mb-2">

            Summary

        </p>

        <p className="text-gray-700 leading-7">

            {prediction.summary}

        </p>

    </div>

</div>

            </div>

            <div className="mt-8 text-center">

                <p className="text-sm text-gray-400">

                    Prediction generated using GRU-based Remaining Useful Life Estimation.

                </p>

            </div>


<div className="mt-10">

    <h3 className="text-xl font-bold mb-4">
        Analysis Tools
    </h3>

    <div className="flex flex-wrap gap-4">

        {/* Decision Intelligence */}
        {/* Decision Intelligence */}
        <button
            onClick={() =>
                navigate("/decision-intelligence", {
                    state: prediction,
                })
            }
            className="
                bg-blue-600
                hover:bg-blue-700
                text-white
                px-6
                py-3
                rounded-xl
                font-semibold
            "
        >
            📊 Decision Intelligence
        </button>

        {/* Explainability */}
        <button
            onClick={() =>
                navigate("/explainability", {
                    state: prediction,
                })
            }
            className="
                bg-green-600
                hover:bg-green-700
                text-white
                px-6
                py-3
                rounded-xl
                font-semibold
            "
        >
            🧠 Explainability
        </button>

        {/* Uncertainty */}
        <button
            onClick={() =>
                navigate("/uncertainty", {
                    state: prediction,
                })
            }
            className="
                bg-purple-600
                hover:bg-purple-700
                text-white
                px-6
                py-3
                rounded-xl
                font-semibold
            "
        >
            📈 Uncertainty
        </button>

    </div>

</div>
        </div>

    );

}

export default PredictionCard;