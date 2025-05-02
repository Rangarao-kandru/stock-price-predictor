import React, { useState } from 'react';

const App = () => {
  const [ticker, setTicker] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handlePrediction = async () => {
    setLoading(true);
    setError('');
    setPrediction(null);
    try {
      const response = await fetch(`https://your-backend-api-url/predict?ticker=${ticker}`);
      const data = await response.json();
      setPrediction(data);
    } catch (err) {
      setError('Failed to fetch prediction');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Stock Price Prediction</h1>
      <input
        type="text"
        placeholder="Enter stock ticker"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
      />
      <button onClick={handlePrediction} disabled={loading}>
        {loading ? 'Loading...' : 'Get Prediction'}
      </button>

      {error && <p>{error}</p>}
      {prediction && (
        <div>
          <p>Predicted Price: ${prediction.predicted_price}</p>
          <p>Volume: {prediction.volume}</p>
          <p>Market Trend: {prediction.trend}</p>
        </div>
      )}
    </div>
  );
};

export default App;
    