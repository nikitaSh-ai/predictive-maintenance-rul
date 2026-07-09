function CircularProgress({
    value,
    size = 140,
    strokeWidth = 12,
}) {



    const radius = (size - strokeWidth) / 2;

const circumference = 2 * Math.PI * radius;

const offset =
    circumference -
    (value / 100) * circumference;
    return (

    <div
        className="relative inline-flex items-center justify-center"
        style={{
            width: size,
            height: size,
        }}
    >

        <svg
            width={size}
            height={size}
        >

            {/* Background Circle */}

            <circle
                cx={size / 2}
                cy={size / 2}
                r={radius}
                stroke="#E5E7EB"
                strokeWidth={strokeWidth}
                fill="none"
            />

            {/* Progress Circle */}

            <circle
                cx={size / 2}
                cy={size / 2}
                r={radius}
                stroke="#06B6D4"
                strokeWidth={strokeWidth}
                fill="none"
                strokeDasharray={circumference}
                strokeDashoffset={offset}
                strokeLinecap="round"
                transform={`rotate(-90 ${size / 2} ${size / 2})`}
            />

        </svg>
<div
    className="
        absolute
        text-3xl
        font-bold
        text-cyan-600
    "
>

    {value}%

</div>




    </div>

);
}

export default CircularProgress;