function FleetSummary({ predictions }) {

    if (!predictions || predictions.length === 0) {
        return null;
    }

    const totalEngines = predictions.length;

    const healthy = predictions.filter(
        (engine) => engine.risk === "Low"
    ).length;

    const medium = predictions.filter(
        (engine) => engine.risk === "Medium"
    ).length;

    const high = predictions.filter(
        (engine) => engine.risk === "High"
    ).length;

    const critical = predictions.filter(
        (engine) => engine.risk === "Critical"
    ).length;


    const averageRUL =
    (
        predictions.reduce(
            (sum, engine) =>
                sum + engine.predicted_rul,
            0
        ) / totalEngines
    ).toFixed(1);

const lowestRUL = Math.min(
    ...predictions.map(
        (engine) => engine.predicted_rul
    )
);

const highestRUL = Math.max(
    ...predictions.map(
        (engine) => engine.predicted_rul
    )
);

    return (

        <div
            className="
                bg-white
                rounded-2xl
                shadow-lg
                border
                p-6
                mt-8
            "
        >

            <h2 className="text-2xl font-bold mb-6">

                Fleet Summary

            </h2>

            <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-8 gap-4">

                <div className="text-center">

                    <p className="text-gray-500">
                        Total
                    </p>

                    <h3 className="text-3xl font-bold">

                        {totalEngines}

                    </h3>

                </div>

                <div className="text-center">

                    <p className="text-green-600">

                        Healthy

                    </p>

                    <h3 className="text-3xl font-bold">

                        {healthy}

                    </h3>

                </div>

                <div className="text-center">

                    <p className="text-yellow-600">

                        Medium

                    </p>

                    <h3 className="text-3xl font-bold">

                        {medium}

                    </h3>

                </div>

                <div className="text-center">

                    <p className="text-orange-600">

                        High

                    </p>

                    <h3 className="text-3xl font-bold">

                        {high}

                    </h3>

                </div>

                <div className="text-center">

                    <p className="text-red-600">

                        Critical

                    </p>

                    <h3 className="text-3xl font-bold">

                        {critical}

                    </h3>

                </div>

            </div>


            <div className="text-center">

    <p className="text-blue-600">

        Average RUL

    </p>

    <h3 className="text-3xl font-bold">

        {averageRUL}

    </h3>

</div>

<div className="text-center">

    <p className="text-indigo-600">

        Lowest RUL

    </p>

    <h3 className="text-3xl font-bold">

        {lowestRUL}

    </h3>

</div>

<div className="text-center">

    <p className="text-purple-600">

        Highest RUL

    </p>

    <h3 className="text-3xl font-bold">

        {highestRUL}

    </h3>

</div>

        </div>

    );

}

export default FleetSummary;


















