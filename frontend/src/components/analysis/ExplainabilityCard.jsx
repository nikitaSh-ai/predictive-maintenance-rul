function ExplainabilityCard({ prediction }) {

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

                🔍 Explainability

            </h2>

            <p className="text-gray-500 mb-6">

                Top contributing features for this prediction.

            </p>
            <div className="space-y-4">

{
    prediction.feature_importance
        ?.slice(0, 10)
        .map((feature, index) => (

            <div
                key={index}
                className="border rounded-xl p-4"
            >

                <div className="flex justify-between">

                    <span className="font-medium">

                        {feature.feature}

                    </span>

                    <span className="font-bold text-blue-600">

                        {feature.importance.toFixed(4)}

                    </span>

                </div>

            </div>

        ))
}

</div>

        </div>

    );

}

export default ExplainabilityCard;