import { NavLink } from "react-router-dom";
import navigation from "../../config/navigation";

function Sidebar() {
  return (
  <aside className="w-72 bg-white border-r border-gray-200 flex flex-col shadow-sm">

       <div className="p-6 border-b border-gray-200">

    <h2 className="text-xl font-bold text-blue-700">
        Predictive Maintenance
    </h2>

    <p className="text-sm text-gray-500 mt-1">
        Industrial AI Dashboard
    </p>

</div>

      <nav className="flex-1 px-4 py-4">

        {navigation.map((item) => {

          const Icon = item.icon;

          return (

            <NavLink
              key={item.path}
              to={item.path}
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