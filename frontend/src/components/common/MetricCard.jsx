function MetricCard({ title, value, color = "text-blue-600" }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6 border transition-all duration-300 hover:shadow-xl hover:-translate-y-1">

      <p className="text-gray-500 text-sm">
        {title}
      </p>

      <h2 className={`text-3xl font-bold mt-2 ${color}`}>
        {value}
      </h2>

    </div>
  );
}

export default MetricCard;