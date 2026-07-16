import { NavLink } from "react-router-dom";
import { X } from "lucide-react";
import navigation from "../../config/navigation";
function Sidebar({
    sidebarOpen,
    setSidebarOpen,
}) {
  return (
<aside
    className={`
        fixed
        top-0
        left-0
        h-full
        w-72
        bg-white
        border-r
        border-gray-200
        shadow-lg
        z-50
        transform
        transition-transform
        duration-300

        ${
            sidebarOpen
                ? "translate-x-0"
                : "-translate-x-full"
        }

        md:translate-x-0
        md:static
        md:flex
        md:flex-col
    `}
>
<div
    className="
        p-6
        border-b
        border-gray-200
        flex
        items-start
        justify-between
    "
>
<div>

    <h2 className="text-xl font-bold text-blue-700">
        Predictive Maintenance
    </h2>

    <p className="text-sm text-gray-500 mt-1">
        Industrial AI Dashboard
    </p>

</div>

<button
    onClick={() => setSidebarOpen(false)}
    className="
        md:hidden
        p-2
        rounded-lg
        hover:bg-gray-100
    "
>
    <X size={22} />
</button>
   

</div>

      <nav className="flex-1 px-4 py-4">

        {navigation.map((item) => {

          const Icon = item.icon;

          return (

            <NavLink
              key={item.path}
              to={item.path}
               onClick={() => {
        if (window.innerWidth < 768) {
            setSidebarOpen(false);
        }
    }}
              className={({ isActive }) =>
`
flex items-center
gap-3
rounded-xl
px-4
py-3
mb-2
font-medium
transition-all
duration-300
${
isActive
? "bg-blue-600 text-white shadow-md"
: "text-gray-700 hover:bg-blue-50 hover:text-blue-700 hover:translate-x-1"
}
`
}
            >

              <Icon size={20} />

              <span>{item.name}</span>

            </NavLink>

          );

        })}

      </nav>
      <div className="p-4 border-t border-gray-200">

    <p className="text-xs text-gray-400 text-center">
        Version 1.0
    </p>

</div>

    </aside>
  );
}

export default Sidebar;