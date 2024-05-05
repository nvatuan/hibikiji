import React, { useEffect, useState } from 'react';
import {getHealthCheck, getHistory, saveHistory} from '../api/api';

const HistoryTable = ({ history, setHistory, clearHistory }) => {
  useEffect(() => {
    getHistory().then(response => response.json())
      .then(data => {
        setHistory(data.data.history)
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>Button</th>
          <th>Result</th>
          <th style={{ width: '500px' }}>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        {
          history.length === 0 && (
            <tr>
              <td colSpan="3">No history available</td>
            </tr>
          )
        }
        {history.map((row, index) => (
          <tr key={index}>
            <td>{row.button}</td>
            <td>{row.result}</td>
            <td>{new Date(row.timestamp).toLocaleString()}</td>
          </tr>
        ))}
        <tr>
          <td colSpan={"3"}>
            <button style={{ width: '100%', display: 'block' }}
              onClick={() => clearHistory()}
            >Clear History</button>
          </td>
        </tr>
      </tbody>
    </table>
  );
};

export default HistoryTable;