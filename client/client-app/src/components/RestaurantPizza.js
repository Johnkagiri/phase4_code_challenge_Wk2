import React, { useState } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

const RestaurantPizza = ({ restaurants, pizza }) => {
  const [refreshPage, setRefreshPage] = useState(false);

  const formik = useFormik({
    initialValues: {
      price: "",
      restaurant_id: "",
      pizza_id: "",
    },
    // validationSchema: formSchema,
    onSubmit: (values) => {
      fetch("http://127.0.0.1:5000/restaurantpizza", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      }).then((res) => {
        console.log(res.json());
        if (res.status == 200) {
          setRefreshPage(!refreshPage);
        }
      });
    },
  });

  return (
    <div>
      <form onSubmit={formik.handleSubmit}>
        <label>Select restaurant</label>
        <select
          name="restaurant_id"
          value={formik.values.restaurant_id}
          onChange={formik.handleChange}
        >
          {restaurants.map((data, index) => (
            <option key={index} value={data.id}>
              {data.name}
            </option>
          ))}
        </select>

        <label>Select pizza</label>
        <select
          name="pizza_id"
          value={formik.values.pizza_id}
          onChange={formik.handleChange}
        >
          {pizza.map((data, index) => (
            <option key={index} value={data.id}>
              {data.name}
            </option>
          ))}
        </select>
        <label>Price: </label>
        <input
          name="price"
          onChange={formik.handleChange}
          value={formik.values.price}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default RestaurantPizza;

