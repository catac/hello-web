import { useState } from 'react';
import './App.css';

// Pre-defined list of symbols
const symbols = ['NVDA', 'GOOGL', 'USD_CHF'];

function App() {
  const [selectedSymbol, setSelectedSymbol] = useState<string>('');
  const [price, setPrice] = useState<string | null>(null);
  const [timestamp, setTimestamp] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSymbolChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedSymbol(event.target.value);
  };

  const fetchPrice = async () => {
    if (!selectedSymbol) {
      setError('Please select a symbol.');
      return;
    }

    try {
      const response = await fetch(`/last_price/${selectedSymbol}`);
      if (!response.ok) {
        throw new Error('Price not available for the given symbol.');
      }
      const data = await response.json();
      setPrice(data.price);
      setTimestamp(data.timestamp);
      setError(null);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred.');
      }
      setPrice(null);
      setTimestamp(null);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Stock Price Viewer</h1>
        <div className="controls">
          <select onChange={handleSymbolChange} value={selectedSymbol}>
            <option value="" disabled>Select a symbol</option>
            {symbols.map(symbol => (
              <option key={symbol} value={symbol}>{symbol}</option>
            ))}
          </select>
          <button onClick={fetchPrice}>Get Price</button>
        </div>
        {error && <p className="error">{error}</p>}
        {price && timestamp && (
          <div className="price-display">
            <h2>{selectedSymbol}</h2>
            <p>Price: {price}</p>
            <p>Timestamp: {timestamp}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;