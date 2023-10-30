import React, { useState, useEffect } from "react";
import { Route, Routes, useNavigate } from "react-router";
import { BrowserRouter, Link } from "react-router-dom";
import Restaurant from "./components/Restaurant";
import ResId from "./components/ResId";
import Pizza from "./components/Pizza";
import Pizid from "./components/Pizid";
import RestaurantPizza from "./components/RestaurantPizza";

function App() {
  const [restaurants, setRestaurants] = useState([{}]);
  const [resId, setResId] = useState({});
  const [pizza, setPizza] = useState([{}])
  const [pizId, setPizId ] = useState({})

  useEffect(() => {
    fetch("http://127.0.0.1:5000/restaurant")
      .then((res) => res.json())
      .then((data) => {
        // console.log(data)
        setRestaurants(data)});
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/pizza")
      .then((res) => res.json())
      .then((data) => {
        // console.log(data)
        setPizza(data)});
  }, []);
  
  async function handleResid(id) {
    console.log(id);
    try {
      const response = await fetch(`http://127.0.0.1:5000/restaurant/${id}`);
      const data = await response.json();
      console.log(data);
     setResId(data)
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }

  async function handlePizid(id) {
    console.log(id);
    try {
      const response = await fetch(`http://127.0.0.1:5000/pizza/${id}`);
      const data = await response.json();
      console.log(data);
     setPizId(data)
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }


  return (
    <div className="App">
      <Routes>
        <Route
          path="/*"
          element={
            <Restaurant restaurants={restaurants} handleResid={handleResid} />
          }
        />
        <Route path="/pizza" element = {<Pizza pizza={pizza} handlePizid={handlePizid} /> } />
        <Route path="/resid" element={<ResId resId={resId} />} />
        <Route path="/pizid" element={<Pizid pizId={pizId} /> } />
        <Route path="/restaurantpizza" element={<RestaurantPizza restaurants={restaurants} pizza={pizza}/> } />
      </Routes>
    </div>
  );
}

export default App;
