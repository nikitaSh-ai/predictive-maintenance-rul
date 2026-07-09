function LoadingSpinner() {

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

                    AI is analyzing your engine...

                </h2>

                <div className="mt-8 space-y-3 text-gray-600">

                    <p>📂 Reading uploaded dataset</p>

                    <p>⚙ Creating time sequences</p>

                    <p>🧠 Running GRU model</p>

                    <p>🛠 Generating maintenance recommendation</p>

                </div>

            </div>

        </div>

    );

}

export default LoadingSpinner;