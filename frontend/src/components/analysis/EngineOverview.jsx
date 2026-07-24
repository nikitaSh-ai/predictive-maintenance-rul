function EngineOverview({ prediction }) {

    if (!prediction) return null;

    return (

        <div
            className="
                bg-white
                rounded-2xl
                shadow-lg
                border
                p-8
            "
        >

            <div className="flex items-center justify-between">

                <div>

                    <h2 className="text-3xl font-bold">

                        Engine {prediction.engine_id}

                    </h2>

                    <p className="text-gray-500 mt-2">

                        Complete diagnostic overview

                    </p>

                </div>

                <div
                    className="
                        text-right
                    "
                >

                    <p className="text-gray-500">

                        Predicted RUL

                    </p>

                    <h1 className="text-5xl font-bold text-blue-600">

                        {prediction.predicted_rul}

                    </h1>

                    <p className="text-gray-500">

                        Cycles

                    </p>

                </div>

            </div>

            <div
                className="
                    grid
                    grid-cols-2
                    md:grid-cols-4
                    gap-6
                    mt-8
                "
            >

                <div>

                    <p className="text-gray-500">

                        Risk

                    </p>

                    <p className="font-bold text-xl">

                        {prediction.risk}

                    </p>

                </div>

                <div>

                    <p className="text-gray-500">

                        Priority

                    </p>

                    <p className="font-bold text-xl">

                        {prediction.priority}

                    </p>

                </div>

                <div>

                    <p className="text-gray-500">

                        Health Score

                    </p>

                    <p className="font-bold text-xl">

                        {prediction.health_score}%

                    </p>

                </div>

                <div>

                    <p className="text-gray-500">

                        Confidence

                    </p>

                    <p className="font-bold text-xl">

                        {prediction.confidence}

                    </p>

                </div>

            </div>

        </div>

    );

}

export default EngineOverview;