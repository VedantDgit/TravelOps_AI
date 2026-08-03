import { Link } from "react-router-dom";

function QuickActionCard({
  title,
  path,
  color,
}) {

  return (

    <Link
      to={path}
      className={`${color} rounded-xl p-6 text-white hover:scale-105 transition`}
    >

      <h2 className="text-xl font-bold">

        {title}

      </h2>

    </Link>

  );

}

export default QuickActionCard;