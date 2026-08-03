import { motion } from "framer-motion";

function StatsCard({ title, value, color }) {
  return (
    <motion.div
      whileHover={{ scale: 1.05 }}
      className="bg-slate-800 rounded-2xl shadow-lg p-6"
    >
      <h3 className="text-gray-400">{title}</h3>

      <h1
        className="text-4xl font-bold mt-3"
        style={{ color }}
      >
        {value}
      </h1>
    </motion.div>
  );
}

export default StatsCard;