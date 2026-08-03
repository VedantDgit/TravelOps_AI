import { NavLink } from "react-router-dom";

import {
  FaHome,
  FaPlane,
  FaUser,
  FaHotel
} from "react-icons/fa";

const menus = [
  {
    name: "Dashboard",
    icon: <FaHome />,
    path: "/",
  },

  {
    name: "Flight Prediction",
    icon: <FaPlane />,
    path: "/flight",
  },

  {
    name: "Gender Prediction",
    icon: <FaUser />,
    path: "/gender",
  },

  {
    name: "Hotel Recommendation",
    icon: <FaHotel />,
    path: "/recommendation",
  },
];

function Sidebar() {
  return (
    <div className="w-72 bg-slate-950 border-r border-slate-700 min-h-screen">

      <div className="p-6">

        <h2 className="text-white text-2xl font-bold">
          Dashboard
        </h2>

        <p className="text-gray-400 text-sm mt-1">
          Navigation
        </p>

      </div>

      <div className="px-4 space-y-3">

        {menus.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center gap-4 p-4 rounded-xl transition ${
                isActive
                  ? "bg-blue-600 text-white shadow-lg"
                  : "text-gray-300 hover:bg-slate-800"
              }`
            }
          >
            <span className="text-xl">
              {item.icon}
            </span>

            <span className="font-medium">
              {item.name}
            </span>

          </NavLink>
        ))}

      </div>

    </div>
  );
}

export default Sidebar;