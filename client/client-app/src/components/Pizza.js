import React from "react";
import { Link } from "react-router-dom";

const Pizza = ({ pizza, handlePizid }) => {
  const pizzaMap = pizza.map((data, index) => {
    const dataID = data.id;

    return (
      <div key={index} className="rest">
        <p>
          {" "}
          {data.name} {dataID}
        </p>
        <Link to="/pizid">
          <button onClick={() => handlePizid(dataID)}>View</button>
        </Link>
      </div>
    );
  });

  return <div>{pizzaMap}</div>;
};

export default Pizza;
