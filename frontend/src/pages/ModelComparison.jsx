function ModelComparison() {

    return (

        <div className="p-8">

            <h1
                className="
                    text-3xl
                    font-bold
                "
            >

                Model Comparison

            </h1>

            <p
                className="
                    mt-2
                    text-gray-500
                "
            >

                Compare the performance of different machine learning models
                used for Remaining Useful Life prediction.

            </p>


            <div
    className="
        mt-8
        rounded-2xl
        border
        bg-gradient-to-r
        from-blue-600
        to-cyan-500
        text-white
        p-8
        shadow-lg
    "
>

    <p className="text-lg">

        🏆 Best Performing Model

    </p>

    <h2
        className="
            text-4xl
            font-bold
            mt-3
        "
    >

        GRU (Production Model)

    </h2>

    <p className="mt-4 text-blue-100">

        The GRU model achieved the best prediction performance and
        was selected as the final deployment model for Remaining
        Useful Life estimation.

    </p>

</div>



<h2
    className="
        text-2xl
        font-bold
        mt-10
        mb-6
    "
>

    Performance Metrics

</h2>



<div
    className="
        grid
        grid-cols-1
        md:grid-cols-3
        gap-6
    "
>

    {/* GRU */}

    <div
        className="
            bg-white
            border
            rounded-xl
            shadow
            p-6
        "
    >

        <h3
            className="
                text-2xl
                font-bold
                text-blue-600
            "
        >

            GRU

        </h3>

        <p className="mt-4">

            MAE:
            <strong> 0.0374</strong>

        </p>

        <p className="mt-2">

            RMSE:
            <strong> 0.0497</strong>

        </p>

        <p className="mt-2">

            R²:
            <strong> Coming Soon</strong>

        </p>

    </div>

    {/* Random Forest */}

    <div
        className="
            bg-white
            border
            rounded-xl
            shadow
            p-6
        "
    >

        <h3
            className="
                text-2xl
                font-bold
                text-green-600
            "
        >

            Random Forest

        </h3>

        <p className="mt-4">

            MAE:
            <strong> 0.1066</strong>

        </p>

        <p className="mt-2">

            RMSE:
            <strong> 0.1402</strong>

        </p>

        <p className="mt-2">

            R²:
            <strong> Coming Soon</strong>

        </p>

    </div>

    {/* XGBoost */}

    <div
        className="
            bg-white
            border
            rounded-xl
            shadow
            p-6
        "
    >

        <h3
            className="
                text-2xl
                font-bold
                text-orange-600
            "
        >

            XGBoost

        </h3>

        <p className="mt-4">

            MAE:
            <strong> Coming Soon</strong>

        </p>

        <p className="mt-2">

            RMSE:
            <strong> Coming Soon</strong>

        </p>

        <p className="mt-2">

            R²:
            <strong> Coming Soon</strong>

        </p>

    </div>

</div>


<h2
    className="
        text-2xl
        font-bold
        mt-10
        mb-6
    "
>

    Performance Comparison

</h2>


<div
    className="
        overflow-x-auto
        bg-white
        border
        rounded-xl
        shadow
    "
>

    <table className="min-w-full">

        <thead
            className="
                bg-gray-100
            "
        >

            <tr>

                <th className="px-6 py-4 text-left">

                    Metric

                </th>

                <th className="px-6 py-4 text-center">

                    GRU

                </th>

                <th className="px-6 py-4 text-center">

                    Random Forest

                </th>

                <th className="px-6 py-4 text-center">

                    XGBoost

                </th>

            </tr>

        </thead>

        <tbody>

            <tr className="border-t">

                <td className="px-6 py-4 font-medium">

                    MAE

                </td>

                <td className="px-6 py-4 text-center">

                    0.0374

                </td>

                <td className="px-6 py-4 text-center">

                    0.1066

                </td>

                <td className="px-6 py-4 text-center">

                    Coming Soon

                </td>

            </tr>

            <tr className="border-t">

                <td className="px-6 py-4 font-medium">

                    RMSE

                </td>

                <td className="px-6 py-4 text-center">

                    0.0497

                </td>

                <td className="px-6 py-4 text-center">

                    0.1402

                </td>

                <td className="px-6 py-4 text-center">

                    Coming Soon

                </td>

            </tr>

            <tr className="border-t">

                <td className="px-6 py-4 font-medium">

                    R²

                </td>

                <td className="px-6 py-4 text-center">

                    Coming Soon

                </td>

                <td className="px-6 py-4 text-center">

                    Coming Soon

                </td>

                <td className="px-6 py-4 text-center">

                    Coming Soon

                </td>

            </tr>

        </tbody>

    </table>

</div>


<h2
    className="
        text-2xl
        font-bold
        mt-10
        mb-6
    "
>

    Performance Visualization

</h2>

<div
    className="
        bg-white
        border
        rounded-xl
        shadow
        p-6
    "
>

    <h3
        className="
            text-xl
            font-semibold
            mb-6
        "
    >

        Mean Absolute Error (Lower is Better)

    </h3>
    <div className="mb-6">

    <div className="flex justify-between mb-2">

        <span className="font-medium">

            GRU

        </span>

        <span>

            0.0374

        </span>

    </div>

    <div
        className="
            w-full
            bg-gray-200
            rounded-full
            h-4
        "
    >

        <div
            className="
                bg-blue-600
                h-4
                rounded-full
            "
            style={{ width: "25%" }}
        />

    </div>

</div>



<div className="mb-6">

    <div className="flex justify-between mb-2">

        <span className="font-medium">

            Random Forest

        </span>

        <span>

            0.1066

        </span>

    </div>

    <div
        className="
            w-full
            bg-gray-200
            rounded-full
            h-4
        "
    >

        <div
            className="
                bg-green-600
                h-4
                rounded-full
            "
            style={{ width: "70%" }}
        />

    </div>

</div>


<div>

    <div className="flex justify-between mb-2">

        <span className="font-medium">

            XGBoost

        </span>

        <span>

            Coming Soon

        </span>

    </div>

    <div
        className="
            w-full
            bg-gray-200
            rounded-full
            h-4
        "
    >

        <div
            className="
                bg-orange-500
                h-4
                rounded-full
            "
            style={{ width: "0%" }}
        />

    </div>

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

    <h3
        className="
            text-xl
            font-semibold
            mb-6
        "
    >

        Root Mean Squared Error (Lower is Better)

    </h3>



<div className="mb-6">

    <div className="flex justify-between mb-2">

        <span className="font-medium">

            GRU

        </span>

        <span>

            0.0497

        </span>

    </div>

    <div
        className="
            w-full
            bg-gray-200
            rounded-full
            h-4
        "
    >

        <div
            className="
                bg-blue-600
                h-4
                rounded-full
            "
            style={{ width: "30%" }}
        />

    </div>

</div>

<div className="mb-6">

    <div className="flex justify-between mb-2">

        <span className="font-medium">

            Random Forest

        </span>

        <span>

            0.1402

        </span>

    </div>

    <div
        className="
            w-full
            bg-gray-200
            rounded-full
            h-4
        "
    >

        <div
            className="
                bg-green-600
                h-4
                rounded-full
            "
            style={{ width: "80%" }}
        />

    </div>

</div>
<div>

    <div className="flex justify-between mb-2">

        <span className="font-medium">

            XGBoost

        </span>

        <span>

            Coming Soon

        </span>

    </div>

    <div
        className="
            w-full
            bg-gray-200
            rounded-full
            h-4
        "
    >

        <div
            className="
                bg-orange-500
                h-4
                rounded-full
            "
            style={{ width: "0%" }}
        />

    </div>

</div>
</div>


<div
    className="
        mt-10
        bg-gradient-to-r
        from-blue-50
        to-cyan-50
        border
        rounded-xl
        p-8
    "
>

    <h2
        className="
            text-2xl
            font-bold
            mb-6
        "
    >

        🤖 AI Model Analysis

    </h2>

    <p
        className="
            text-gray-700
            leading-8
        "
    >

        Among all evaluated models, the <strong>GRU model</strong>
        demonstrated the best predictive performance for Remaining
        Useful Life estimation. It achieved the lowest Mean Absolute
        Error and Root Mean Squared Error, indicating more accurate
        and reliable predictions compared to the baseline Random
        Forest model.

    </p>

    <div
    className="
        mt-6
        bg-white
        rounded-xl
        border-l-4
        border-blue-600
        p-5
    "
>

    <p className="text-gray-700">

        <strong>Deployment Decision:</strong>

        The GRU model was selected as the production model because it
        consistently produced lower prediction errors while maintaining
        stable performance across engine degradation stages.

    </p>

</div>
<div
    className="
        mt-5
        bg-white
        rounded-xl
        border-l-4
        border-green-600
        p-5
    "
>

    <p className="text-gray-700">

        <strong>Engineering Insight:</strong>

        Lower MAE and RMSE values indicate that maintenance decisions
        can be scheduled with greater confidence, reducing unexpected
        failures and minimizing unnecessary maintenance costs.

    </p>

</div>

</div>


<div className="mt-10 text-center">

    <p className="text-sm text-gray-400">

        Model comparison is based on evaluation using the NASA
        C-MAPSS FD001 turbofan engine degradation dataset.

    </p>

</div>

</div>

    );

}

export default ModelComparison;