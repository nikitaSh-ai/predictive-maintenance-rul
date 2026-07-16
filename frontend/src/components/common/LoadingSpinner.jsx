function LoadingSpinner({

    title = "AI is analyzing your engine...",

    steps = [

        "📂 Reading uploaded dataset",

        "⚙ Creating time sequences",

        "🧠 Running GRU model",

        "🛠 Generating maintenance recommendation",

    ],

}) {

    return (

        <div className="bg-white rounded-2xl shadow-lg border p-10 mt-8">

            <div className="flex flex-col items-center">

                <div
                    className="
                        w-16
                        h-16
                        border-4
                        border-blue-200
                        border-t-blue-600
                        rounded-full
                        animate-spin
                    "
                />

                <h2 className="text-2xl font-bold mt-6">

    {title}

</h2>

                <div className="mt-8 space-y-3 text-gray-600">

    {steps.map((step) => (

        <p key={step}>

            {step}

        </p>

    ))}

</div>

            </div>

        </div>

    );

}

export default LoadingSpinner;