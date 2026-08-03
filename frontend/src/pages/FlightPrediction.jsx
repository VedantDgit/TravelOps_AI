import { useState } from "react";
import { toast } from "react-toastify";

import Layout from "../components/Layout";
import PageHeader from "../components/PageHeader";
import InputField from "../components/InputField";
import PrimaryButton from "../components/PrimaryButton";
import ResultCard from "../components/ResultCard";
import api from "../services/api";

const fromCities = [
  "Brasilia (DF)",
  "Aracaju (SE)",
  "Campo Grande (MS)",
  "Florianopolis (SC)",
  "Natal (RN)"
];

const toCities = [
  "Rio de Janeiro (RJ)",
  "Sao Paulo (SP)",
  "Salvador (BA)",
  "Recife (PE)",
  "Porto Alegre (RS)"
];

const agencies = [
  "FlyingDrops",
  "CloudFy",
  "Rainbow"
];

const flightTypes = [
  "firstClass",
  "premium",
  "economy"
];

const weekDays = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
  "Sunday"
];

function FlightPrediction() {

  const [formData, setFormData] = useState({
    from: "",
    to: "",
    flightType: "",
    agency: "",
    distance: "",
    time: "",
    year: "",
    month: "",
    day: "",
    day_of_week: "",
  });

  const [price, setPrice] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });

  };

  const predictPrice = async () => {

    try {

      setLoading(true);

      const response = await api.post(
        "/predict-flight-price",
        formData
      );

      setPrice(response.data.predicted_price);

      toast.success("Flight price predicted successfully!");

    } catch (error) {

      console.error(error);

      toast.error("Prediction Failed");

    } finally {

      setLoading(false);

    }

  };

  return (

    <Layout>

      <PageHeader
        title="Flight Price Prediction"
        subtitle="Predict airline ticket prices using our Machine Learning model."
      />

      <div className="grid md:grid-cols-2 gap-6">

        {/* From */}

        <div>
          <label className="block text-gray-300 mb-2">
            Departure
          </label>

          <select
            name="from"
            value={formData.from}
            onChange={handleChange}
            className="w-full rounded-xl bg-slate-800 border border-slate-700 p-3 text-white"
          >
            <option value="">Select Departure</option>

            {fromCities.map((city) => (
              <option key={city} value={city}>
                {city}
              </option>
            ))}

          </select>
        </div>

        {/* To */}

        <div>
          <label className="block text-gray-300 mb-2">
            Destination
          </label>

          <select
            name="to"
            value={formData.to}
            onChange={handleChange}
            className="w-full rounded-xl bg-slate-800 border border-slate-700 p-3 text-white"
          >
            <option value="">Select Destination</option>

            {toCities.map((city) => (
              <option key={city} value={city}>
                {city}
              </option>
            ))}

          </select>
        </div>

        {/* Flight Type */}

        <div>
          <label className="block text-gray-300 mb-2">
            Flight Type
          </label>

          <select
            name="flightType"
            value={formData.flightType}
            onChange={handleChange}
            className="w-full rounded-xl bg-slate-800 border border-slate-700 p-3 text-white"
          >
            <option value="">Select Flight Type</option>

            {flightTypes.map((type) => (
              <option key={type} value={type}>
                {type}
              </option>
            ))}

          </select>
        </div>

        {/* Agency */}

        <div>
          <label className="block text-gray-300 mb-2">
            Agency
          </label>

          <select
            name="agency"
            value={formData.agency}
            onChange={handleChange}
            className="w-full rounded-xl bg-slate-800 border border-slate-700 p-3 text-white"
          >
            <option value="">Select Agency</option>

            {agencies.map((agency) => (
              <option key={agency} value={agency}>
                {agency}
              </option>
            ))}

          </select>
        </div>

        <InputField
          label="Distance (km)"
          name="distance"
          type="number"
          value={formData.distance}
          onChange={handleChange}
          placeholder="830"
        />

        <InputField
          label="Flight Time (Hours)"
          name="time"
          type="number"
          value={formData.time}
          onChange={handleChange}
          placeholder="2.5"
        />

        <InputField
          label="Year"
          name="year"
          type="number"
          value={formData.year}
          onChange={handleChange}
          placeholder="2021"
        />

        <InputField
          label="Month"
          name="month"
          type="number"
          value={formData.month}
          onChange={handleChange}
          placeholder="8"
        />

        <InputField
          label="Day"
          name="day"
          type="number"
          value={formData.day}
          onChange={handleChange}
          placeholder="15"
        />

        {/* Day */}

        <div>
          <label className="block text-gray-300 mb-2">
            Day of Week
          </label>

          <select
            name="day_of_week"
            value={formData.day_of_week}
            onChange={handleChange}
            className="w-full rounded-xl bg-slate-800 border border-slate-700 p-3 text-white"
          >
            <option value="">Select Day</option>

            {weekDays.map((day) => (
              <option key={day} value={day}>
                {day}
              </option>
            ))}

          </select>
        </div>

      </div>

      <div className="mt-8">

        <PrimaryButton
          loading={loading}
          onClick={predictPrice}
        >
          Predict Flight Price
        </PrimaryButton>

      </div>

      {price && (

        <ResultCard
          title="Predicted Flight Price"
          value={`₹ ${price}`}
        />

      )}

    </Layout>

  );

}

export default FlightPrediction;