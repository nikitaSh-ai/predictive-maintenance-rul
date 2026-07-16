function FeatureImportanceCard({ featureImportance }) {

    const sortedFeatures = Object.entries(featureImportance)
    .sort((a, b) => b[1] - a[1]);

    const maxValue =
    sortedFeatures.length > 0
        ? sortedFeatures[0][1]
        : 1;




    const topFeatures = sortedFeatures.slice(0, 3);

    return (

        <div
            className="
                bg-white
                rounded-xl
                shadow-md
                p-6
            "
        >

            <h2 className="text-2xl font-bold mb-6">

                Feature Importance

            </h2>



            <div
    className="
        bg-blue-50
        border
        border-blue-200
        rounded-xl
        p-5
        mb-8
    "
>

    <h3 className="text-xl font-bold mb-4">

        🏆 Top 3 Contributing Features

    </h3>

    {

        topFeatures.map(

            ([feature, value], index) => (

                <div
                    key={feature}
                    className="
                        flex
                        justify-between
                        py-2
                    "
                >

                    <span>

                        {

                            index === 0
                                ? "🥇"

                            : index === 1
                                ? "🥈"

                            : "🥉"

                        }

                        {" "}

                        {feature}

                    </span>

                    <span className="font-semibold">

                        {value.toFixed(4)}

                    </span>

                </div>

            )

        )

    }

</div>




            {
                  
                  sortedFeatures.map(

                ([feature, value]) => (

                    <div
    key={feature}
    className="mb-5"
>

    <div className="flex justify-between mb-2">

        <span className="font-medium">

            {feature}

        </span>

        <span>

            {value.toFixed(4)}

        </span>

    </div>

    <div
        className="
            w-full
            bg-gray-200
            rounded-full
            h-3
        "
    >

        <div
            className="
                bg-blue-600
                h-3
                rounded-full
                transition-all
                duration-700
            "
           style={{
    width: `${(value / maxValue) * 100}%`,
}}
        />

    </div>

</div>



                )

            )}

        </div>

    );

}

export default FeatureImportanceCard;