import "./App.css";
import "materialize-css";
import { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";

function App() {
  const [data, setData] = useState([{}]);
  const [inputValue, setInputValue] = useState();

  const handleInputValue = (e) => {
    setInputValue(e.target.value);
  };

  useEffect(() => {
    const query = "?search=" + inputValue || "";
    fetch("/api" + query)
      .then((response) => response.json())
      .then((data) => setData(data));
  }, [inputValue, setInputValue]);

  console.log(data);

  return (
    <div className="container">
      <div className="row">
        <form class="col s6 offset-s3">
          <div className="col s12 heading-pile">
            <div className="heading">Autocomplete</div>
            <FontAwesomeIcon className="search-icon" icon={faMagnifyingGlass} />
          </div>
          <div class="row">
            <div class="input-field col s12">
              <input
                onChange={handleInputValue}
                id="icon_telephone"
                type="tel"
                className="validate"
              />
              <label htmlFor="icon_telephone">Search: </label>
            </div>
          </div>
        </form>
      </div>
      <List items={data}></List>
    </div>
  );
}

const List = ({ items }) => {
  return (
    <div
      className="container"
      style={{
        display: Object.keys(items[0] || {}).length === 0 ? "none" : "flex",
      }}
    >
      <div className="row">
        {items.map((item) => (
          <Item key={item.id} value={item.value}></Item>
        ))}
      </div>
    </div>
  );
};

const Item = ({ value }) => {
  return <div className="wrapper col">{value}</div>;
};

export default App;
