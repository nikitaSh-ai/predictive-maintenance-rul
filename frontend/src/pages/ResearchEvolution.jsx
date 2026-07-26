function ResearchEvolution() {

    return (

        <div className="p-8">

            <h1
                className="
                    text-3xl
                    font-bold
                "
            >

                Research Evolution

            </h1>

            <p
                className="
                    mt-2
                    text-gray-500
                "
            >

                How this system evolved from a single-condition baseline
                into a generalized, explainable predictive maintenance
                pipeline.

            </p>

            <h2
                className="
                    text-2xl
                    font-bold
                    mt-10
                    mb-6
                "
            >

                Version 1: Single-Condition Baseline

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

                <p className="text-gray-700 leading-8">

                    Version 1 established the core prediction pipeline
                    using NASA's FD001 dataset — a single operating
                    condition with one dominant fault mode. It validated
                    the end-to-end architecture: GRU-based sequence
                    modeling, Integrated Gradients explainability, and
                    rule-based maintenance decisioning.

                </p>

                <div
                    className="
                        grid
                        grid-cols-1
                        md:grid-cols-3
                        gap-6
                        mt-6
                    "
                >

                    <div
                        className="
                            bg-gray-50
                            rounded-lg
                            p-4
                            text-center
                        "
                    >

                        <p className="text-sm text-gray-500">

                            MAE

                        </p>

                        <p className="text-2xl font-bold text-blue-600">

                            9.92

                        </p>

                    </div>

                    <div
                        className="
                            bg-gray-50
                            rounded-lg
                            p-4
                            text-center
                        "
                    >

                        <p className="text-sm text-gray-500">

                            RMSE

                        </p>

                        <p className="text-2xl font-bold text-blue-600">

                            13.15

                        </p>

                    </div>

                    <div
                        className="
                            bg-gray-50
                            rounded-lg
                            p-4
                            text-center
                        "
                    >

                        <p className="text-sm text-gray-500">

                            R²

                        </p>

                        <p className="text-2xl font-bold text-blue-600">

                            0.902

                        </p>

                    </div>

                </div>

                <p className="text-gray-500 text-sm mt-6">

                    While accurate, Version 1's scope was limited to
                    engines operating under a single, consistent
                    condition — a simplification not representative of
                    real industrial fleets.

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

                Version 2: Generalized Architecture

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

                <p className="text-gray-700 leading-8">

                    Version 2 extended the pipeline to FD001 through
                    FD004 — multiple operating conditions and multiple
                    fault modes — using a single generalized GRU model
                    with global feature scaling, replacing four separate
                    per-dataset models with one unified architecture.

                </p>

                <div
                    className="
                        grid
                        grid-cols-1
                        md:grid-cols-3
                        gap-6
                        mt-6
                    "
                >

                    <div
                        className="
                            bg-gray-50
                            rounded-lg
                            p-4
                            text-center
                        "
                    >

                        <p className="text-sm text-gray-500">

                            MAE (Overall)

                        </p>

                        <p className="text-2xl font-bold text-cyan-600">

                            10.64

                        </p>

                    </div>

                    <div
                        className="
                            bg-gray-50
                            rounded-lg
                            p-4
                            text-center
                        "
                    >

                        <p className="text-sm text-gray-500">

                            RMSE (Overall)

                        </p>

                        <p className="text-2xl font-bold text-cyan-600">

                            15.82

                        </p>

                    </div>

                    <div
                        className="
                            bg-gray-50
                            rounded-lg
                            p-4
                            text-center
                        "
                    >

                        <p className="text-sm text-gray-500">

                            R² (Overall)

                        </p>

                        <p className="text-2xl font-bold text-cyan-600">

                            0.857

                        </p>

                    </div>

                </div>

                <div
                    className="
                        overflow-x-auto
                        mt-6
                    "
                >

                    <table className="min-w-full text-sm">

                        <thead className="bg-gray-100">

                            <tr>

                                <th className="px-4 py-2 text-left">Dataset</th>
                                <th className="px-4 py-2 text-center">MAE</th>
                                <th className="px-4 py-2 text-center">RMSE</th>
                                <th className="px-4 py-2 text-center">R²</th>

                            </tr>

                        </thead>

                        <tbody>

                            <tr className="border-t">
                                <td className="px-4 py-2 font-medium">FD001</td>
                                <td className="px-4 py-2 text-center">10.54</td>
                                <td className="px-4 py-2 text-center">15.16</td>
                                <td className="px-4 py-2 text-center">0.864</td>
                            </tr>

                            <tr className="border-t">
                                <td className="px-4 py-2 font-medium">FD002</td>
                                <td className="px-4 py-2 text-center">12.00</td>
                                <td className="px-4 py-2 text-center">16.74</td>
                                <td className="px-4 py-2 text-center">0.835</td>
                            </tr>

                            <tr className="border-t">
                                <td className="px-4 py-2 font-medium">FD003</td>
                                <td className="px-4 py-2 text-center">9.61</td>
                                <td className="px-4 py-2 text-center">14.03</td>
                                <td className="px-4 py-2 text-center">0.886</td>
                            </tr>

                            <tr className="border-t">
                                <td className="px-4 py-2 font-medium">FD004</td>
                                <td className="px-4 py-2 text-center">10.08</td>
                                <td className="px-4 py-2 text-center">15.93</td>
                                <td className="px-4 py-2 text-center">0.851</td>
                            </tr>

                        </tbody>

                    </table>

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

                Architecture Evolution

            </h2>

            <div
                className="
                    grid
                    grid-cols-1
                    md:grid-cols-2
                    gap-6
                "
            >

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
                            text-lg
                            font-semibold
                            text-blue-600
                            mb-4
                        "
                    >

                        Version 1 Pipeline

                    </h3>

                    <ol className="space-y-2 text-gray-700 list-decimal list-inside">

                        <li>Dataset Upload (FD001 only)</li>
                        <li>Validation</li>
                        <li>Local Feature Scaling</li>
                        <li>GRU Prediction</li>
                        <li>Integrated Gradients Explainability</li>
                        <li>Decision Engine</li>

                    </ol>

                </div>

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
                            text-lg
                            font-semibold
                            text-cyan-600
                            mb-4
                        "
                    >

                        Version 2 Pipeline

                    </h3>

                    <ol className="space-y-2 text-gray-700 list-decimal list-inside">

                        <li>Dataset Upload (FD001–FD004)</li>
                        <li>Validation</li>
                        <li>Engine Split</li>
                        <li>Latest 40-Cycle Extraction</li>
                        <li>Padding (for short sequences)</li>
                        <li>Global Feature Scaling</li>
                        <li>Generalized GRU Prediction</li>
                        <li>Monte Carlo Dropout Uncertainty</li>
                        <li>Integrated Gradients Explainability</li>
                        <li>Decision Engine</li>

                    </ol>

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

                Research Gap

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

                <p className="text-gray-700 leading-8">

                    Most predictive maintenance RUL literature evaluates
                    models on a single operating condition, such as
                    FD001 alone. Few published systems combine
                    multi-condition generalization with explainability,
                    calibrated uncertainty estimation, and decision-level
                    output in a single deployed pipeline.

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

                Contributions

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

                <ul className="space-y-4 text-gray-700">

                    <li className="flex gap-3">
                        <span className="text-blue-600 font-bold">•</span>
                        <span>
                            A single generalized model spanning four
                            operating and fault regimes, replacing four
                            separate per-dataset models.
                        </span>
                    </li>

                    <li className="flex gap-3">
                        <span className="text-blue-600 font-bold">•</span>
                        <span>
                            Integrated Gradients explainability wired
                            directly into the live prediction path,
                            rather than limited to offline analysis.
                        </span>
                    </li>

                    <li className="flex gap-3">
                        <span className="text-blue-600 font-bold">•</span>
                        <span>
                            Monte Carlo Dropout uncertainty quantification
                            feeding directly into risk and priority
                            decisions.
                        </span>
                    </li>

                    <li className="flex gap-3">
                        <span className="text-blue-600 font-bold">•</span>
                        <span>
                            An end-to-end decision engine translating
                            predicted RUL and uncertainty into actionable
                            maintenance recommendations.
                        </span>
                    </li>

                </ul>

            </div>

            <h2
                className="
                    text-2xl
                    font-bold
                    mt-10
                    mb-6
                "
            >

                Performance Trade-off

            </h2>

            <div
                className="
                    bg-gradient-to-r
                    from-blue-50
                    to-cyan-50
                    border
                    rounded-xl
                    p-6
                "
            >

                <p className="text-gray-700 leading-8">

                    Version 2's overall MAE and RMSE are modestly higher
                    than Version 1's single-condition numbers. This is
                    expected: Version 2 solves a strictly harder problem,
                    generalizing across four operating and fault regimes
                    instead of one. The trade-off is specialized accuracy
                    (Version 1) versus cross-condition robustness
                    (Version 2) — a standard and defensible
                    generalization trade-off in machine learning, not a
                    regression in model quality.

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

                Pipeline Evolution

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

                <p className="text-gray-700 leading-8">

                    Version 1 followed a straightforward path: Upload,
                    Validate, Predict, Explain, Decide — built for one
                    dataset. Version 2 introduces Engine Split, latest
                    40-cycle window extraction, and padding for short
                    sequences, alongside global scaling, so the same
                    single API can correctly serve any of the four
                    C-MAPSS datasets without dataset-specific code paths.

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

                Future Work

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

                <ul className="space-y-4 text-gray-700">

                    <li className="flex gap-3">
                        <span className="text-cyan-600 font-bold">•</span>
                        <span>
                            Literature review positioning this system
                            against existing multi-condition RUL
                            approaches.
                        </span>
                    </li>

                    <li className="flex gap-3">
                        <span className="text-cyan-600 font-bold">•</span>
                        <span>
                            Novelty extensions, such as attention
                            mechanisms or transformer-based sequence
                            encoders.
                        </span>
                    </li>

                    <li className="flex gap-3">
                        <span className="text-cyan-600 font-bold">•</span>
                        <span>
                            A formal ablation study isolating the
                            accuracy cost of generalization.
                        </span>
                    </li>

                    <li className="flex gap-3">
                        <span className="text-cyan-600 font-bold">•</span>
                        <span>
                            A research paper draft using this project as
                            the core case study.
                        </span>
                    </li>

                </ul>

            </div>

        </div>

    );

}

export default ResearchEvolution;