function DecisionIntelligence({ prediction }) {

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

            <h2 className="text-2xl font-bold mb-6">

                📊 Decision Intelligence

            </h2>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

                <div>

                    <p className="text-gray-500">
                        Priority
                    </p>

                    <p className="font-semibold mt-2">
                        {prediction.priority}
                    </p>

                </div>

                <div>

                    <p className="text-gray-500">
                        Risk Level
                    </p>

                    <p className="font-semibold mt-2">
                        {prediction.risk}
                    </p>

                </div>

                <div>

                    <p className="text-gray-500">
                        Recommendation
                    </p>

                    <p className="font-semibold mt-2">
                        {prediction.recommendation}
                    </p>

                </div>

                <div>

                    <p className="text-gray-500">
                        Inspection
                    </p>

                    <p className="font-semibold mt-2">
                        {prediction.inspection}
                    </p>

                </div>

                <div className="md:col-span-2">

                    <p className="text-gray-500">
                        Reason
                    </p>

                    <p className="font-semibold mt-2">
                        {prediction.reason}
                    </p>

                </div>

            </div>

        </div>

    );

}

export default DecisionIntelligence;