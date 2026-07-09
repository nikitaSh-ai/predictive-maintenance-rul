function PipelineStep({ title, isLast = false }) {
  return (
    <div className="flex flex-col items-center">

      <div
        className="
          bg-blue-600
          text-white
          px-6
          py-3
          rounded-xl
          shadow-md
          font-semibold
          w-64
          text-center
        "
      >
        {title}
      </div>

      {!isLast && (
        <div className="text-3xl text-blue-600 my-3">
          ↓
        </div>
      )}

    </div>
  );
}

export default PipelineStep;