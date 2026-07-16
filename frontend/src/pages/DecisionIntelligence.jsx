import { useLocation } from "react-router-dom";

import { useNavigate } from "react-router-dom";

function DecisionIntelligence() {

    const location = useLocation();

    const prediction = location.state;

    const navigate = useNavigate();



    if (!prediction) {

   return (

    <div className="p-8">

        <div
            className="
                max-w-2xl
                mx-auto
                mt-12
                bg-white
                border
                rounded-2xl
                shadow
                p-10
                text-center
            "
        >

            <div className="text-6xl">

                📊

            </div>

            <h2
                className="
                    text-3xl
                    font-bold
                    mt-6
                "
            >

                No Prediction Available

            </h2>

            <p
                className="
                    mt-4
                    text-gray-500
                    leading-7
                "
            >

                Run a Remaining Useful Life prediction first
                to generate maintenance recommendations.

            </p>


            <button
    onClick={() => navigate("/predict")}
    className="
        mt-8
        px-6
        py-3
        bg-blue-600
        text-white
        rounded-xl
        font-semibold
        hover:bg-blue-700
        transition
    "
>

    Go to Predict RUL

</button>

        </div>

    </div>

);
}



    return (

    <div className="space-y-6">

       <div className="mb-8">

    <h1
        className="
            text-4xl
            font-bold
            text-gray-800
        "
    >

        🧠 Decision Intelligence

    </h1>

    <p
        className="
            text-gray-500
            mt-2
        "
    >

        AI powered maintenance recommendations based on predicted Remaining Useful Life.

    </p>

</div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

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

            Priority

        </p>

        <h2
            className="
                text-3xl
                font-bold
                text-red-600
                mt-2
            "
        >

           <span
    className="
        inline-block
        bg-red-600
        text-white
        px-4
        py-2
        rounded-full
        text-xl
        font-bold
    "
>

    {prediction.priority}

</span>

        </h2>

    </div>

    <div
        className="
            bg-yellow-50
            border
            border-yellow-200
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
                text-yellow-700
                mt-2
            "
        >

            {prediction.risk}

        </h2>

    </div>

</div>


<div
    className="
        mt-8
        bg-white
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

        🛠 Maintenance Recommendation

    </h2>

    <p
        className="
            text-lg
            leading-8
            text-gray-700
        "
    >

        {prediction.recommendation}

    </p>

</div>


<div
    className="
        grid
        grid-cols-1
        md:grid-cols-3
        gap-6
        mt-8
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

            📅 Inspection

        </p>

        <h3
            className="
                text-xl
                font-bold
                mt-3
                text-blue-700
            "
        >

            {prediction.inspection}

        </h3>

    </div>

    <div
        className="
            bg-green-50
            border
            border-green-200
            rounded-xl
            p-6
        "
    >

        <p className="text-gray-500">

            🎯 Maintenance Focus

        </p>

        <h3
            className="
                text-xl
                font-bold
                mt-3
                text-green-700
            "
        >

            {prediction.focus}

        </h3>

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

            💡 Decision Reason

        </p>

        <h3
            className="
                text-lg
                font-semibold
                mt-3
                text-purple-700
            "
        >

            {prediction.reason}

        </h3>

    </div>

</div>

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

    <h2
        className="
            text-2xl
            font-bold
            mb-4
        "
    >

        📋 Executive Summary

    </h2>

    <p
        className="
            text-gray-700
            leading-8
        "
    >

        {prediction.summary}

    </p>

</div>

<div className="mt-10 text-center">

    <p className="text-sm text-gray-400">

        Decision generated using the AI powered Decision Support Engine.

    </p>

</div>


    </div>

);

}

export default DecisionIntelligence;