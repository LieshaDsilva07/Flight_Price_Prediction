<h1>✈️ Flight Price Prediction with SQL-Based Data Exploration</h1>

<p>This project predicts airline ticket prices using machine learning techniques and includes structured SQL-based data exploration to understand key trends and improve model performance.</p>

<hr />

<h2>📂 Project Structure</h2>

<pre>
flight_price_prediction/
├── data/
│   └── Data_Train.csv
├── model/
│   ├── Flight_price_pred.ipynb
│   ├── Flight_price_pred.html
│   └── flight_price_model.pkl
├── sql_queries/
│   └── queries.sql
</pre>

<hr />

<h2>📊 Project Goals</h2>
<ul>
  <li>Understand factors affecting airline ticket prices (e.g. stops, airlines, routes)</li>
  <li>Build a regression model to accurately predict flight prices</li>
  <li>Perform SQL-based data exploration to derive insights</li>
  <li>Improve model performance through feature engineering and EDA</li>
</ul>

<hr />

<h2>🔍 SQL-Based Data Exploration</h2>
<p>Before modeling, I performed SQL analysis using <strong>MySQL</strong> to uncover trends in the flight data:</p>

<ul>
  <li>Average price by airline</li>
  <li>Number of flights from each source</li>
  <li>Top 5 most expensive flights</li>
  <li>Average price based on number of stops</li>
  <li>Cheapest flights per airline</li>
  <li>Day-wise price trends</li>
  <li>Most common flight routes</li>
</ul>

<p>📄 <strong>SQL script:</strong> <a href="sql_queries/queries.sql">sql_queries/queries.sql</a></p>

<hr />

<h2>🤖 Machine Learning Model</h2>
<ul>
  <li><strong>Algorithm:</strong> Regression (e.g., Random Forest / Linear Regression)</li>
  <li><strong>Accuracy:</strong> ~93.7%</li>
  <li><strong>Tech stack:</strong> Python, Pandas, Scikit-learn, NumPy, Matplotlib, Seaborn</li>
</ul>

<p>📘 <a href="model/Flight_price_pred.ipynb">Notebook</a><br />
🌐 <a href="model/Flight_price_pred.html">HTML Version</a></p>

<hr />

<h2>📌 Key Libraries Used</h2>
<ul>
  <li>pandas, numpy, scikit-learn, matplotlib, seaborn</li>
  <li>MySQL for structured querying and analysis</li>
</ul>

<hr />

<h2>🧠 What I Learned</h2>
<ul>
  <li>Real-world data preprocessing and cleaning (e.g., duration conversion)</li>
  <li>Feature engineering for regression tasks</li>
  <li>Exploratory analysis using SQL + Python</li>
  <li>Model evaluation using metrics: R², MAE, RMSE</li>
</ul>

<hr />


