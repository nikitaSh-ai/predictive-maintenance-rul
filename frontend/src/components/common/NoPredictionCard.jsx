import { useNavigate } from "react-router-dom";

function NoPredictionCard({ icon = "📊" }) {

    const navigate = useNavigate();

    return (

        <div className="p-8">

            <div
                className="
                    max-w-2xl
                    mx-auto
                    mt-12
                    bg-white
                    border
                    rounded-2xl
                    shadow
                    p-10
                    text-center
                "
            >

                <div className="text-6xl">

                    {icon}

                </div>

                <h2
                    className="
                        text-3xl
                        font-bold
                        mt-6
                    "
                >

                    No Prediction Available

                </h2>

                <p
                    className="
                        mt-4
                        text-gray-500
                        leading-7
                    "
                >

                    Run a Remaining Useful Life prediction first
                    to generate maintenance recommendations.

                </p>

                <button
                    onClick={() => navigate("/predict")}
                    className="
                        mt-8
                        px-6
                        py-3
                        bg-blue-600
                        text-white
                        rounded-xl
                        font-semibold
                        hover:bg-blue-700
                        transition
                    "
                >

                    Go to Predict RUL

                </button>

            </div>

        </div>

    );

}

export default NoPredictionCard;