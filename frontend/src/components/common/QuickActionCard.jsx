import { Link } from "react-router-dom";

function QuickActionCard({
    title,
    description,
    icon,
    to,
}) {

    return (

        <Link
            to={to}
            className="
            block
            bg-white
            rounded-xl
            border
            border-gray-200
            shadow-md
            p-6
            transition-all
            duration-300
            hover:-translate-y-1
            hover:shadow-xl
            "
        >

            <div className="text-4xl mb-4">
                {icon}
            </div>

            <h3 className="text-xl font-bold text-gray-800">
                {title}
            </h3>

            <p className="text-gray-500 mt-2">
                {description}
            </p>

            <p className="text-blue-600 font-semibold mt-6">
                Open →
            </p>

        </Link>

    );

}

export default QuickActionCard;