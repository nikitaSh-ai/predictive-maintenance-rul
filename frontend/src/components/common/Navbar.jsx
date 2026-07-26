import { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { PredictionContext } from "../../context/PredictionContext";

function Navbar() {

  const { predictionResults, clearPredictionSession } = useContext(PredictionContext);

  const navigate = useNavigate();

  const handleClearSession = () => {

    clearPredictionSession();

    navigate("/predict");

  };

  return (
    <header className="bg-blue-700 text-white shadow-md">
      <div className="px-8 py-4 flex justify-between items-center">
        {/* Left Side */}
        <div>
          <h1 className="text-3xl font-bold">
            Predictive Maintenance AI Dashboard
          </h1>
          <p className="text-blue-100 mt-1">
            Remaining Useful Life Estimation & Decision Support
          </p>
        </div>
        {/* Right Side */}
        <div className="text-right flex items-center gap-6">

          {
            Array.isArray(predictionResults) && predictionResults.length > 0 && (

              <button
                onClick={handleClearSession}
                className="
                  bg-white/10
                  hover:bg-white/20
                  border
                  border-white/30
                  px-4
                  py-2
                  rounded-lg
                  text-sm
                  font-semibold
                  transition
                "
              >
                Clear Session
              </button>

            )
          }

          <div>
            <p className="font-semibold">
              🟢 Backend Ready
            </p>
            <p className="text-blue-100">
              GRU Model
            </p>
          </div>

        </div>
      </div>
    </header>
  );
}
export default Navbar;