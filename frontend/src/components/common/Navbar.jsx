function Navbar() {
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

        <div className="text-right">

          <p className="font-semibold">
            🟢 Backend Ready
          </p>

          <p className="text-blue-100">
            GRU Model
          </p>

        </div>

      </div>

    </header>
  );
}

export default Navbar;