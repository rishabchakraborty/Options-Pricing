function calculate() {
    const spotPrice = document.getElementById("spotPrice").value;
    const strikePrice = document.getElementById("strikePrice").value;
    const timeToMaturity = document.getElementById("timeToMaturity").value;
    const riskFreeRate = document.getElementById("riskFreeRate").value;
    const volatility = document.getElementById("volatility").value;
  
    const optionPrice = blackScholes(spotPrice, strikePrice, timeToMaturity, riskFreeRate, volatility);
  
    document.getElementById("result").innerHTML = `Option price: ${optionPrice.toFixed(2)}`;
  }
  
  function blackScholes(spotPrice, strikePrice, timeToMaturity, riskFreeRate, volatility) {
    const d1 = (Math.log(spotPrice / strikePrice) + (riskFreeRate + (volatility ** 2) / 2) * timeToMaturity) / (volatility * Math.sqrt(timeToMaturity));
    const d2 = d1 - volatility * Math.sqrt(timeToMaturity);
  
    const Nd1 = standardNormalCDF(d1);
    const Nd2 = standardNormalCDF(d2);
  
    const optionPrice = spotPrice * Nd1 - strikePrice * Math.exp(-riskFreeRate * timeToMaturity) * Nd2;
  
    return optionPrice;
  }
  
  function standardNormalCDF(x) {
    const t = 1 / (1 + 0.2316419 * Math.abs(x));
    const d = 0.3989423 * Math.exp(-x * x / 2);
    const p = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
    
    if (x > 0) {
      return 1 - p;
    } else {
      return p;
    }
  }
  