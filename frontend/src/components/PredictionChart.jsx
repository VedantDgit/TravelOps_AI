import {
  BarChart,
  Bar,
  ResponsiveContainer,
  XAxis,
  Tooltip,
} from "recharts";

const data = [
  {
    name: "Flight",
    value: 95,
  },
  {
    name: "Gender",
    value: 92,
  },
  {
    name: "Hotel",
    value: 97,
  },
];

function PredictionChart() {

  return (

    <div className="bg-slate-800 rounded-2xl p-6 mt-10">

      <h2 className="text-white text-2xl font-bold mb-5">
        Model Accuracy
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <BarChart data={data}>

          <XAxis dataKey="name" />

          <Tooltip />

          <Bar
            dataKey="value"
            fill="#3b82f6"
          />

        </BarChart>

      </ResponsiveContainer>

    </div>

  );

}

export default PredictionChart;