import React from "react";
import Display from "./Display";
import ButtonPanel from "./ButtonPanel";
import calculate from "../logic/calculate";
import "./App.css";

import HistoryPanel from "./HistoryPanel";
import {saveHistory, clearHistory} from "../api/api";

export default class App extends React.Component {
  state = {
    total: null,
    next: null,
    operation: null,
    history: [],
    historyError: null,
  };

  callSaveHistory = (button, result) => {
    saveHistory({ button, result }).
      then(response => {
        if (response.ok) return response.json();
        this.setState({
          ...this.state,
          historyError: response.statusText,
        })
      }).
      then(data => {
        console.log(data)
        this.setState({
          ...this.state,
          history: data.data.history,
        })
      })
  }


  handleClick = buttonName => {
    const newState = calculate(this.state, buttonName)
    this.callSaveHistory(buttonName, newState.total || newState.next || "0")
    this.setState(newState);
  };

  setHistory = (v) => {
    this.setState({
      ...this.state,
      history: v,
    });
  };

  clearHistory = () => {
    this.setHistory([]);
    clearHistory().then(response => null)
  }

  getDisplayValue = () => {
    return this.state.total || this.state.next || "0";
  }

  render() {
    return (
    <div className="component-app-wrapper">
      <div className="component-app">
        <div className="calculator">
          <Display value={this.getDisplayValue()} />
          <ButtonPanel
            clickHandler={this.handleClick}
            setHistory={(v) => this.setHistory(v)}
          />
        </div>
        <div className="history">
          <HistoryPanel history={this.state.history}
            setHistory={(v) => this.setHistory(v)}
            clearHistory={() => this.clearHistory()}
            error={this.state.historyError} />
        </div>
      </div>
    </div>
    );
  }
}