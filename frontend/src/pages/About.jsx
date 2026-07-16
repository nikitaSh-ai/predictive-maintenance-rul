function About() {

    return (

        <div className="space-y-8">

            <div>

                <h1 className="text-3xl font-bold">

                    About This Project

                </h1>

                <p className="text-gray-500 mt-2">

                    Explainable AI based Predictive Maintenance Decision Support System for Remaining Useful Life Estimation.

                </p>

            </div>

<div
    className="
        rounded-2xl
        bg-gradient-to-r
        from-blue-600
        to-cyan-500
        text-white
        p-8
        shadow-lg
    "
>

    <p className="text-lg">

        🚀 Industrial AI Project

    </p>

    <h2
        className="
            text-4xl
            font-bold
            mt-3
        "
    >

        Predictive Maintenance Decision Support System

    </h2>

    <p className="mt-5 text-blue-100 leading-7">

        This project predicts the Remaining Useful Life of aircraft
        turbofan engines using deep learning and provides
        explainability, uncertainty estimation, and intelligent
        maintenance recommendations to support industrial decision making.

    </p>

</div>

<div
    className="
        bg-white
        border
        rounded-xl
        shadow
        p-8
    "
>

    <h2 className="text-2xl font-bold mb-6">

        Project Overview

    </h2>

    <p className="text-gray-700 leading-8">

        The objective of this project is to estimate the Remaining
        Useful Life (RUL) of turbofan engines using historical sensor
        measurements. Along with accurate prediction, the system
        explains model decisions, estimates prediction uncertainty,
        and generates maintenance recommendations to improve
        reliability and reduce unexpected failures.

    </p>

</div>



<div
    className="
        bg-white
        border
        rounded-xl
        shadow
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

        Technologies Used

    </h2>

    <div
        className="
            grid
            grid-cols-2
            md:grid-cols-3
            lg:grid-cols-4
            gap-4
        "
    >

        <div className="bg-blue-50 rounded-lg p-4 text-center font-semibold">
            React
        </div>

        <div className="bg-green-50 rounded-lg p-4 text-center font-semibold">
            FastAPI
        </div>

        <div className="bg-purple-50 rounded-lg p-4 text-center font-semibold">
            PyTorch
        </div>

        <div className="bg-yellow-50 rounded-lg p-4 text-center font-semibold">
            Captum
        </div>

        <div className="bg-cyan-50 rounded-lg p-4 text-center font-semibold">
            NumPy
        </div>

        <div className="bg-red-50 rounded-lg p-4 text-center font-semibold">
            Pandas
        </div>

        <div className="bg-orange-50 rounded-lg p-4 text-center font-semibold">
            Scikit-Learn
        </div>

        <div className="bg-gray-100 rounded-lg p-4 text-center font-semibold">
            Tailwind CSS
        </div>

    </div>

</div>
<div
    className="
        bg-white
        border
        rounded-xl
        shadow
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

        Key Features

    </h2>

    <div className="space-y-4">

        <p>✅ Remaining Useful Life Prediction using GRU</p>

        <p>✅ Explainable AI with Captum Feature Attribution</p>

        <p>✅ Monte Carlo Dropout Uncertainty Estimation</p>

        <p>✅ Intelligent Maintenance Recommendation Engine</p>

        <p>✅ Interactive React Dashboard</p>

        <p>✅ FastAPI Backend for Real Time Predictions</p>

    </div>

</div>


<div
    className="
        bg-white
        border
        rounded-xl
        shadow
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

        Dataset Information

    </h2>

    <div className="space-y-3">

        <p><strong>Dataset:</strong> NASA C-MAPSS FD001</p>

        <p><strong>Domain:</strong> Aircraft Turbofan Engine Predictive Maintenance</p>

        <p><strong>Sequence Length:</strong> 40 Cycles</p>

        <p><strong>Input Features:</strong> 17 Sensor Features</p>

        <p><strong>Prediction Target:</strong> Remaining Useful Life (RUL)</p>

    </div>

</div>



<div
    className="
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

        AI Model Architecture

    </h2>

    <p className="leading-8 text-gray-700">

        NASA C-MAPSS Dataset

        → Data Preprocessing

        → Feature Engineering

        → GRU Deep Learning Model

        → Explainability (Captum)

        → Monte Carlo Dropout

        → Decision Intelligence

        → Maintenance Recommendation

    </p>

</div>

<div className="text-center pt-6">

    <p className="text-sm text-gray-400">

        Built as a research oriented industrial AI project for
        Explainable Predictive Maintenance using Deep Learning.

    </p>

</div>

        </div>

    );

}

export default About;