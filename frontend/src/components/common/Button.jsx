function Button({
    children,
    onClick,
    type = "button",
    disabled = false,
}) {
    return (

        <button
            type={type}
            onClick={onClick}
            disabled={disabled}
            className="
                bg-blue-600
               enabled:hover:bg-blue-700
                text-white
                px-6
                py-3
                rounded-xl
                font-semibold
                shadow-md
                transition-all
                duration-300
             enabled:hover:shadow-lg
                disabled:opacity-50
                disabled:cursor-not-allowed
            "
        >
            {children}
        </button>

    );
}

export default Button;