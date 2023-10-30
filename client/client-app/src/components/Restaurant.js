import React from "react";
import { Route, Routes, useNavigate } from "react-router";
import { BrowserRouter, Link } from "react-router-dom";

const Restaurant = ({ restaurants, handleResid }) => {
  const restaurantMap = restaurants.map((data, index) => {
    const dataID =data.id
    
    return (
      
      <div key={index} className="rest">
        <p> {data.name} {dataID}</p>
        <Link to="/resid">
          <button onClick={() => handleResid(dataID
            )}>View</button>
        </Link>
      </div>
    );
  });
  return <div>{restaurants ? <div>{restaurantMap}</div> : null}</div>;
};

export default Restaurant;
