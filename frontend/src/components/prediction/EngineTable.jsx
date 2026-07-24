import { useState } from "react";

function EngineTable({
    predictions,
    onView
}) {

    const [search, setSearch] = useState("");
    const [riskFilter, setRiskFilter] = useState("All");
    const [sortBy, setSortBy] = useState("engine");

    if (!predictions || predictions.length === 0) {
        return null;
    }




    const exportCSV = () => {

    const headers = [
        "Engine ID",
        "Predicted RUL",
        "Risk",
        "Priority"
    ];

    const rows = filteredPredictions.map(engine => [

        engine.engine_id,
        engine.predicted_rul,
        engine.risk,
        engine.priority

    ]);

    const csvContent = [

        headers.join(","),
        ...rows.map(row => row.join(","))

    ].join("\n");

    const blob = new Blob(
        [csvContent],
        { type: "text/csv;charset=utf-8;" }
    );

    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.download = "engine_predictions.csv";

    link.click();

    URL.revokeObjectURL(url);

};

    const filteredPredictions = predictions
    .filter((engine) => {

        const matchesSearch =
            engine.engine_id
                .toString()
                .includes(search);

        const matchesRisk =
            riskFilter === "All" ||
            engine.risk === riskFilter;

        return matchesSearch && matchesRisk;

    })
    .sort((a, b) => {

        if (sortBy === "engine") {

            return a.engine_id - b.engine_id;

        }

        if (sortBy === "rulAsc") {

            return a.predicted_rul - b.predicted_rul;

        }

        if (sortBy === "rulDesc") {

            return b.predicted_rul - a.predicted_rul;

        }

        return 0;

    });

    return (

        <div
            className="
                mt-8
                bg-white
                rounded-2xl
                shadow-lg
                border
                overflow-hidden
            "
        >

            <div className="p-6 border-b">

                <h2 className="text-2xl font-bold">

                    Engine Predictions

                </h2>

            </div>
<div className="p-4 border-b bg-gray-50">

    <div className="flex flex-wrap items-center gap-4">

        <input
            type="text"
            placeholder="🔍 Search Engine ID..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="
                w-full
                md:w-80
                px-4
                py-2
                border
                border-gray-300
                rounded-lg
                focus:outline-none
                focus:ring-2
                focus:ring-blue-500
            "
        />

        <select
            value={riskFilter}
            onChange={(e) => setRiskFilter(e.target.value)}
            className="
                w-40
                px-3
                py-2
                border
                border-gray-300
                rounded-lg
                bg-white
                focus:outline-none
                focus:ring-2
                focus:ring-blue-500
            "
        >

            <option value="All">All Risks</option>
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
            <option value="Critical">Critical</option>

        </select>

        <select
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
            className="
                w-48
                px-3
                py-2
                border
                border-gray-300
                rounded-lg
                bg-white
                focus:outline-none
                focus:ring-2
                focus:ring-blue-500
            "
        >

            <option value="engine">
                Sort: Engine ID
            </option>

            <option value="rulAsc">
                RUL (Low → High)
            </option>

            <option value="rulDesc">
                RUL (High → Low)
            </option>

        </select>

        <button
    onClick={exportCSV}
        className="
            px-5
            py-2
            rounded-lg
            border
            border-blue-600
            text-blue-600
            hover:bg-blue-600
            hover:text-white
            transition
        "
    >
        Export CSV
    </button>


    </div>

</div>
            
            <table className="w-full">

                <thead className="bg-gray-100">

                    <tr>

                        <th className="p-4 text-left">
                            Engine
                        </th>

                        <th className="p-4 text-left">
                            Predicted RUL
                        </th>

                        <th className="p-4 text-left">
                            Risk
                        </th>

                        <th className="p-4 text-left">
                            Priority
                        </th>

                        <th className="p-4 text-left">
                            Action
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {
                       filteredPredictions.map((engine) => (

                            <tr
                                key={engine.engine_id}
                                className="border-t"
                            >

                                <td className="p-4">

                                    {engine.engine_id}

                                </td>

                                <td className="p-4">

                                    {engine.predicted_rul}

                                </td>

                                <td className="p-4">

                                    {engine.risk}

                                </td>

                                <td className="p-4">

                                    {engine.priority}

                                </td>

                                <td className="p-4">

                                    <button
    onClick={() => onView(engine)}
    className="
        px-3
        py-1
        bg-blue-600
        text-white
        rounded-lg
        hover:bg-blue-700
    "
>

    View

</button>

                                </td>

                            </tr>

                        ))
                    }

                </tbody>

            </table>

        </div>

    );

}

export default EngineTable;