# Advanced Risk Score Analyzer

## Overview

The Advanced Risk Score Analyzer is a comprehensive, industry-standard financial risk assessment system that provides real-time market risk analysis for the autonomous agent portfolio management system. It replaces the previous placeholder risk calculation with a sophisticated multi-factor risk model used by professional financial institutions.

## Features

### 🎯 Multi-Factor Risk Analysis
- **Volatility Risk**: Rolling standard deviation analysis with annualized volatility calculation
- **Trend Risk**: Linear regression-based trend analysis with R-squared goodness of fit
- **Volume Risk**: Volume spike detection and unusual activity analysis
- **Correlation Risk**: Asset correlation breakdown detection using rolling correlations
- **Market Stress Risk**: Multiple stress indicators including price gaps and momentum analysis

### 📊 Professional-Grade Metrics
- **Weighted Composite Scoring**: Industry-standard risk weighting system
- **Dynamic Risk Levels**: Automatic risk level determination (Low, Medium, High, Critical)
- **Risk Factor Identification**: Detailed breakdown of contributing risk factors
- **Real-time Updates**: Continuous market monitoring with configurable intervals

### 🔧 Technical Implementation
- **Async/Await Architecture**: High-performance asynchronous processing
- **Statistical Analysis**: NumPy-powered mathematical computations
- **Fallback Mechanisms**: Graceful degradation when data is unavailable
- **Comprehensive Logging**: Detailed logging for monitoring and debugging

## Architecture

### Core Components

#### 1. RiskScoreAnalyzer Class
```python
class RiskScoreAnalyzer:
    """Advanced risk score analyzer using industry-standard financial risk metrics"""
    
    async def calculate_comprehensive_risk_score(self, tokens: List[str]) -> RiskMetrics:
        # Main entry point for risk calculation
```

#### 2. RiskMetrics Data Class
```python
@dataclass
class RiskMetrics:
    volatility_score: float      # 0-100
    trend_score: float          # 0-100
    volume_score: float         # 0-100
    correlation_score: float    # 0-100
    market_stress_score: float  # 0-100
    composite_risk_score: float # 0-100
    risk_level: str             # "Low", "Medium", "High", "Critical"
    risk_factors: List[str]     # List of contributing risk factors
```

### Risk Calculation Methods

#### Volatility Risk Calculation
- **Method**: Rolling standard deviation of daily returns
- **Annualization**: √252 × daily volatility (trading days per year)
- **Risk Score**: 0-100 scale where higher volatility = higher risk
- **Threshold**: 50% annualized volatility = 100 risk score

#### Trend Risk Calculation
- **Method**: Linear regression with R-squared analysis
- **Factors**: Slope direction, trend strength, momentum
- **Risk Scoring**:
  - Strong downward trend (slope < 0, R² > 0.7): High risk (80+)
  - Weak trend (R² < 0.3): Medium risk (60)
  - Strong upward trend (slope > 0, R² > 0.7): Low risk (20)

#### Volume Risk Calculation
- **Method**: Volume spike detection and trend analysis
- **Indicators**: 
  - Volume spikes (>2σ above historical average)
  - Unusual volume patterns (>50% change)
- **Risk Scoring**: Base 50 + spike penalties + pattern penalties

#### Correlation Risk Calculation
- **Method**: Rolling correlation analysis between asset pairs
- **Risk Levels**:
  - Strong correlation (>0.7): Low risk (20)
  - Moderate correlation (0.5-0.7): Medium risk (40)
  - Weak correlation (0.3-0.5): High risk (70)
  - Very weak/negative (<0.3): Very high risk (90)

#### Market Stress Risk Calculation
- **Indicators**:
  - Price gap analysis (overnight gaps >5%)
  - Volume concentration (>3x concentration)
  - Short-term momentum (>10% in 3 days)
- **Risk Scoring**: Base 50 + stress indicator penalties

### Weighting System

The composite risk score uses industry-standard risk weights:

```python
RISK_WEIGHTS = {
    'volatility': 0.25,    # 25% - Most important factor
    'trend': 0.20,         # 20% - Market direction
    'correlation': 0.20,   # 20% - Asset relationships
    'market_stress': 0.20, # 20% - Market conditions
    'volume': 0.15,        # 15% - Trading activity
}
```

## Configuration

### Environment Variables
```bash
# Risk analysis thresholds
AUTONOMOUS_AGENT_RISK_SCORE_THRESHOLD=80
AUTONOMOUS_AGENT_VOLATILITY_THRESHOLD=0.15
AUTONOMOUS_AGENT_CORRELATION_THRESHOLD=0.7

# Market monitoring intervals
AUTONOMOUS_AGENT_MARKET_CHECK_INTERVAL=5
```

### Lookback Periods
```python
VOLATILITY_LOOKBACK_DAYS = 30    # 30 days for volatility calculation
TREND_LOOKBACK_DAYS = 14         # 14 days for trend analysis
VOLUME_LOOKBACK_DAYS = 7         # 7 days for volume analysis
CORRELATION_LOOKBACK_DAYS = 30   # 30 days for correlation analysis
```

## Usage

### Basic Usage
```python
from app.services.autonomous_agent import RiskScoreAnalyzer

# Initialize analyzer
analyzer = RiskScoreAnalyzer()

# Calculate comprehensive risk score
risk_metrics = await analyzer.calculate_comprehensive_risk_score(["ETH", "USDC", "LINK"])

# Access risk information
print(f"Risk Level: {risk_metrics.risk_level}")
print(f"Composite Score: {risk_metrics.composite_risk_score:.1f}/100")
print(f"Risk Factors: {', '.join(risk_metrics.risk_factors)}")
```

### Integration with Autonomous Agent
```python
# The risk analyzer is automatically integrated into market condition assessment
async def _assess_market_conditions(self):
    risk_analyzer = RiskScoreAnalyzer()
    risk_metrics = await risk_analyzer.calculate_comprehensive_risk_score(tokens)
    
    # Market conditions are automatically updated with risk data
    self.market_conditions_cache["current"] = {
        "risk_score": risk_metrics.composite_risk_score,
        "risk_level": risk_metrics.risk_level,
        "risk_factors": risk_metrics.risk_factors,
        "risk_breakdown": {
            "volatility_score": risk_metrics.volatility_score,
            "trend_score": risk_metrics.trend_score,
            "volume_score": risk_metrics.volume_score,
            "correlation_score": risk_metrics.correlation_score,
            "market_stress_score": risk_metrics.market_stress_score
        }
    }
```

## Frontend Integration

### PortfolioDriftChart Component
The enhanced PortfolioDriftChart component displays:
- **Main Risk Score**: Large, color-coded risk score (0-100)
- **Risk Level Badge**: Visual risk level indicator
- **Risk Factors**: List of contributing risk factors
- **Risk Breakdown**: Visual bars showing individual risk component scores

### Risk Score Color Coding
- **Green (0-39)**: Low risk
- **Yellow (40-59)**: Medium risk  
- **Orange (60-79)**: High risk
- **Red (80-100)**: Critical risk

## Testing

### Run Test Suite
```bash
cd backend
python test_risk_analyzer.py
```

### Test Scenarios
The test suite covers:
1. **Low Risk Market**: Stable conditions
2. **High Volatility Market**: High price swings
3. **Bear Market**: Strong downward trends
4. **Market Crisis**: Extreme conditions

## Dependencies

### Required Packages
```txt
numpy>=1.21.0          # Statistical computations
aiohttp>=3.8.0         # Async HTTP requests
motor>=3.0.0           # Async MongoDB driver
```

### Installation
```bash
pip install -r requirements.txt
```

## Performance Considerations

### Optimization Features
- **Caching**: Historical data caching to reduce API calls
- **Async Processing**: Non-blocking risk calculations
- **Configurable Intervals**: Adjustable market monitoring frequency
- **Fallback Mechanisms**: Graceful degradation on errors

### Scalability
- **Token Support**: Easily extensible to additional assets
- **Modular Design**: Individual risk components can be enabled/disabled
- **Configurable Weights**: Risk factor weights can be adjusted per strategy

## Future Enhancements

### Planned Features
1. **Machine Learning Integration**: ML-based risk prediction models
2. **Real-time Data Feeds**: Direct integration with major exchanges
3. **Advanced Indicators**: RSI, MACD, Bollinger Bands integration
4. **Custom Risk Models**: User-defined risk calculation methods
5. **Historical Risk Tracking**: Risk score history and trends

### API Integrations
- **CoinGecko Pro**: Enhanced market data
- **Alpha Vantage**: Professional financial data
- **TradingView**: Advanced technical indicators
- **Bloomberg**: Institutional-grade data feeds

## Troubleshooting

### Common Issues

#### 1. Missing Historical Data
**Symptoms**: Risk score stuck at 50, limited risk factors
**Solution**: Check API connectivity and data availability

#### 2. High Risk Scores
**Symptoms**: Consistently high risk levels
**Solution**: Verify market conditions and adjust thresholds

#### 3. Performance Issues
**Symptoms**: Slow risk calculations
**Solution**: Reduce lookback periods or increase caching

### Debug Mode
Enable detailed logging:
```python
import logging
logging.getLogger('app.services.autonomous_agent').setLevel(logging.DEBUG)
```

## Contributing

### Development Guidelines
1. **Test Coverage**: Maintain >90% test coverage
2. **Documentation**: Update this README for new features
3. **Performance**: Benchmark new risk calculation methods
4. **Standards**: Follow financial industry best practices

### Code Style
- **Type Hints**: Full type annotation required
- **Async/Await**: Use async patterns consistently
- **Error Handling**: Comprehensive exception handling
- **Logging**: Structured logging with appropriate levels

## License

This risk analyzer is part of the autonomous agent system and follows the same licensing terms.

## Support

For technical support or feature requests, please refer to the main project documentation or create an issue in the project repository.

---

**Note**: This risk analyzer is designed for educational and development purposes. For production use in financial applications, additional validation, testing, and regulatory compliance may be required.
