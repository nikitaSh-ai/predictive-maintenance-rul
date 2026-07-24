import { useLocation } from "react-router-dom";

function Explainability({ prediction }) {

        const { state: prediction } = useLocation();
    if (
        !prediction ||
        !prediction.feature_importance
    ) {
        return null;
    }

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

                🧠 Explainability

            </h2>

            <p className="text-gray-500 mb-8">

                Top sensor contributions influencing this prediction.

            </p>

            <div className="space-y-5">

                {
                    prediction.feature_importance
                        .slice(0, 10)
                        .map((feature) => (

                            <div
                                key={feature.feature}
                            >

                                <div
                                    className="
                                        flex
                                        justify-between
                                        mb-2
                                    "
                                >

                                    <span>

                                        {feature.feature}

                                    </span>

                                    <span
                                        className="font-semibold"
                                    >

                                        {feature.importance.toFixed(2)}

                                    </span>

                                </div>

                                <div
                                    className="
                                        w-full
                                        h-3
                                        bg-gray-200
                                        rounded-full
                                    "
                                >

                                    <div
                                        className="
                                            h-3
                                            rounded-full
                                            bg-blue-600
                                        "
                                        style={{
                                            width: `${Math.min(
                                                feature.importance * 8,
                                                100
                                            )}%`
                                        }}
                                    />

                                </div>

                            </div>

                        ))
                }

            </div>

        </div>

    );

}

export default Explainability;