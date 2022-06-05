import "./App.css";
import "materialize-css";
import { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import Highlighter from "react-highlight-words";

function App() {
  const [operation, setOperation] = useState("autocomplete");

  const handleOperation = (event) => {
    setOperation(event.target.value);
  };

  return (
    <div className="container content">
      <div className="row">
        <div className="col m6 s12 offset-m3">
          <div className="col s12 heading-pile">
            <div className="heading">Search engine</div>
            <FontAwesomeIcon className="search-icon" icon={faMagnifyingGlass} />
          </div>
          <div className="row radio-wrapper" onChange={handleOperation}>
            <label className="radio-btn">
              <input
                name="group1"
                type="radio"
                value="autocomplete"
                checked={operation === "autocomplete"}
              />
              <span>Autocomplete</span>
            </label>
            <label className="radio-btn">
              <input
                name="group1"
                type="radio"
                value="text-search"
                checked={operation === "text-search"}
              />
              <span>Full text search</span>
            </label>
          </div>
        </div>
        {operation === "autocomplete" ? (
          <AutoComplete></AutoComplete>
        ) : (
          <FullTextSearch></FullTextSearch>
        )}
      </div>
    </div>
  );
}

function AutoComplete() {
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

  return (
    <div class="row">
      <div class="input-field col m6 s12 offset-m3">
        <input
          onChange={handleInputValue}
          id="icon_telephone"
          type="tel"
          className="validate"
        />
        <label htmlFor="icon_telephone">Write a query: </label>
      </div>
      <List items={data}></List>
    </div>
  );
}

const FullTextSearch = () => {
  const [data, setData] = useState({ data: [] });
  const [inputValue, setInputValue] = useState();

  const paragraph = `I am an extraordinarily ordinary woman who has lived an
    extraordinary life. For a little while, the world of my everyday
    became the place where the religious go to confront their genesis; I
    went to be reborn there. I walked ancient lands of ageless beliefs
    where the patriarchs and pariahs, messengers and messiahs, the
    baptized and the baptizers of my religious upbringing once lived and
    breathed, loved and learned and died. I met the modern-day
    Philistines—the people of Goliath—and the descendants of the Assyrians
    and Nubians, too. I stood in the Red Sea and the Dead Sea and climbed
    the mountain from which Moses saw the Promised Land. I bought gold,
    frankincense, and myrrh in a dark and moody alleyway where one of the
    three wise men once stood and visited the little chapel in Cairo that
    covered the cave where the baby Jesus had escaped Herod’s brutality.`;

  const handleInputValue = (e) => {
    setInputValue(e.target.value);
  };

  useEffect(() => {
    const query = "?search=" + inputValue || "";
    fetch("/text" + query)
      .then((response) => response.json())
      .then((data) => setData(data));
  }, [inputValue, setInputValue]);

  // Should be added that text highlites a query from a server

  console.log(data);

  return (
    <div class="row">
      <div class="input-field col m6 s12 offset-m3">
        <input
          id="icon_telephone"
          type="tel"
          className="validate custom-input"
          onChange={handleInputValue}
        />
        <label htmlFor="icon_telephone">Write a query: </label>
      </div>

      <div className="col m8 offset-m2">
        <p className="paragraph">
          <Highlighter
            highlightClassName="YourHighlightClass"
            searchWords={[inputValue]}
            autoEscape={true}
            textToHighlight={paragraph}
            highlightStyle={{ backgroundColor: "#2bb1a4" }}
          ></Highlighter>
        </p>
      </div>
    </div>
  );
};

const List = ({ items }) => {
  return (
    <div
      className="container"
      style={{
        display: Object.keys(items[0] || {}).length === 0 ? "none" : "flex",
      }}
    >
      <div className="row item-wrapper">
        {items.map((item) => (
          <Item key={item.id} value={item.value} items={items.length}></Item>
        ))}
      </div>
    </div>
  );
};

const Item = ({ value, items }) => {
  console.log(items);
  let styles = items > 1 ? "wrapper col m6 s12" : "wrapper col m12 s12";
  return <div className={styles}>{value}</div>;
};

export default App;
