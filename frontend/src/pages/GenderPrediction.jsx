import { useState } from "react";
import { toast } from "react-toastify";

import Layout from "../components/Layout";
import PageHeader from "../components/PageHeader";
import InputField from "../components/InputField";
import PrimaryButton from "../components/PrimaryButton";
import ResultCard from "../components/ResultCard";
import api from "../services/api";

function GenderPrediction() {

  const [formData, setFormData] = useState({
    company: "",
    age: "",
  });

  const [gender, setGender] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {

    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });

  };

  const predictGender = async () => {

    try {

      setLoading(true);

      const response = await api.post(
        "/predict-gender",
        {
          company: formData.company,
          age: Number(formData.age),
        }
      );

      console.log(response.data);

      setGender(response.data.predicted_gender);

      toast.success("Gender predicted successfully!");

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
        title="Gender Prediction"
        subtitle="Predict gender using the trained Machine Learning classification model."
      />

      <div className="grid md:grid-cols-2 gap-6">

        <div>
            <label className="block text-gray-300 mb-2">
                Company
            </label>

            <select
                name="company"
                value={formData.company}
                onChange={handleChange}
                className="w-full rounded-xl bg-slate-800 border border-slate-700 p-3 text-white focus:outline-none focus:border-blue-500"
            >
                <option value="">Select Company</option>
                <option value="Acme Factory">Acme Factory</option>
                <option value="Monsters CYA">Monsters CYA</option>
                <option value="Umbrella LTDA">Umbrella LTDA</option>
                <option value="Wonka Company">Wonka Company</option>
            </select>
        </div>

        <InputField
          label="Age"
          name="age"
          type="number"
          value={formData.age}
          onChange={handleChange}
          placeholder="25"
        />

      </div>

      <div className="mt-8">

        <PrimaryButton
          loading={loading}
          onClick={predictGender}
        >
          Predict Gender
        </PrimaryButton>

      </div>

      {gender && (

        <ResultCard
          title="Predicted Gender"
          value={gender}
        />

      )}

    </Layout>

  );

}

export default GenderPrediction;