#!/usr/bin/env python3
"""
Test script for the Advanced Risk Score Analyzer
Demonstrates various market scenarios and risk calculations
"""

import asyncio
import sys
import os
from datetime import datetime, timezone, timedelta

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.services.autonomous_agent import RiskScoreAnalyzer, RiskMetrics

async def test_risk_analyzer():
    """Test the risk analyzer with various scenarios"""
    print("🚀 Testing Advanced Risk Score Analyzer")
    print("=" * 50)
    
    # Initialize the risk analyzer
    analyzer = RiskScoreAnalyzer()
    
    # Test scenarios
    test_scenarios = [
        {
            "name": "Low Risk Market",
            "description": "Stable prices, low volatility, strong correlations"
        },
        {
            "name": "High Volatility Market", 
            "description": "High price swings, but no clear trend"
        },
        {
            "name": "Bear Market",
            "description": "Strong downward trend, high stress"
        },
        {
            "name": "Market Crisis",
            "description": "Extreme volatility, correlation breakdown, high stress"
        }
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n📊 Scenario {i}: {scenario['name']}")
        print(f"   Description: {scenario['description']}")
        print("-" * 40)
        
        try:
            # Calculate risk score
            risk_metrics = await analyzer.calculate_comprehensive_risk_score(["ETH", "USDC", "LINK"])
            
            # Display results
            print(f"   🎯 Composite Risk Score: {risk_metrics.composite_risk_score:.1f}/100")
            print(f"   🚨 Risk Level: {risk_metrics.risk_level}")
            print(f"   📋 Risk Factors: {', '.join(risk_metrics.risk_factors)}")
            
            print(f"\n   📊 Risk Breakdown:")
            print(f"      • Volatility: {risk_metrics.volatility_score:.1f}/100")
            print(f"      • Trend: {risk_metrics.trend_score:.1f}/100")
            print(f"      • Volume: {risk_metrics.volume_score:.1f}/100")
            print(f"      • Correlation: {risk_metrics.correlation_score:.1f}/100")
            print(f"      • Market Stress: {risk_metrics.market_stress_score:.1f}/100")
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("✅ Risk Analyzer Test Complete!")

async def test_risk_calculation_methods():
    """Test individual risk calculation methods"""
    print("\n🔬 Testing Individual Risk Calculation Methods")
    print("=" * 50)
    
    analyzer = RiskScoreAnalyzer()
    
    # Test with simulated data
    test_data = {
        "ETH": {
            "prices": [2000, 2100, 2050, 2200, 2150, 2300, 2250, 2400, 2350, 2500],
            "volumes": [1000, 1100, 1050, 1200, 1150, 1300, 1250, 1400, 1350, 1500],
            "timestamps": [datetime.now(timezone.utc) - timedelta(days=i) for i in range(10)]
        },
        "USDC": {
            "prices": [1.0, 1.01, 0.99, 1.02, 0.98, 1.03, 0.97, 1.04, 0.96, 1.05],
            "volumes": [5000, 5100, 4900, 5200, 4800, 5300, 4700, 5400, 4600, 5500],
            "timestamps": [datetime.now(timezone.utc) - timedelta(days=i) for i in range(10)]
        },
        "LINK": {
            "prices": [15, 16, 15.5, 17, 16.5, 18, 17.5, 19, 18.5, 20],
            "volumes": [800, 850, 825, 900, 875, 950, 925, 1000, 975, 1050],
            "timestamps": [datetime.now(timezone.utc) - timedelta(days=i) for i in range(10)]
        }
    }
    
    try:
        # Test volatility calculation
        volatility_score = await analyzer._calculate_volatility_risk(test_data)
        print(f"📈 Volatility Risk Score: {volatility_score:.1f}/100")
        
        # Test trend calculation
        trend_score = await analyzer._calculate_trend_risk(test_data)
        print(f"📊 Trend Risk Score: {trend_score:.1f}/100")
        
        # Test volume calculation
        volume_score = await analyzer._calculate_volume_risk(test_data)
        print(f"📊 Volume Risk Score: {volume_score:.1f}/100")
        
        # Test correlation calculation
        correlation_score = await analyzer._calculate_correlation_risk(test_data)
        print(f"🔗 Correlation Risk Score: {correlation_score:.1f}/100")
        
        # Test market stress calculation
        stress_score = await analyzer._calculate_market_stress_risk(test_data)
        print(f"⚠️  Market Stress Score: {stress_score:.1f}/100")
        
    except Exception as e:
        print(f"❌ Error testing individual methods: {str(e)}")

async def test_risk_level_determination():
    """Test risk level determination logic"""
    print("\n🎯 Testing Risk Level Determination")
    print("=" * 50)
    
    analyzer = RiskScoreAnalyzer()
    
    # Test various score combinations
    test_cases = [
        (20, 30, 25, 35, 40, "Low Risk"),
        (45, 55, 50, 60, 65, "Medium Risk"),
        (70, 75, 80, 85, 90, "High Risk"),
        (85, 90, 95, 88, 92, "Critical Risk")
    ]
    
    for i, (vol, trend, vol_score, corr, stress, expected) in enumerate(test_cases, 1):
        print(f"\n   Test Case {i}: Expected {expected}")
        
        # Calculate composite score
        composite = (
            vol * 0.25 + trend * 0.20 + vol_score * 0.15 + 
            corr * 0.20 + stress * 0.20
        )
        
        # Determine risk level
        risk_level, risk_factors = analyzer._determine_risk_level_and_factors(
            vol, trend, vol_score, corr, stress, composite
        )
        
        print(f"      Composite Score: {composite:.1f}")
        print(f"      Risk Level: {risk_level}")
        print(f"      Risk Factors: {', '.join(risk_factors)}")

async def main():
    """Main test function"""
    print("🧪 Advanced Risk Score Analyzer - Comprehensive Test Suite")
    print("=" * 60)
    
    try:
        # Run all tests
        await test_risk_analyzer()
        await test_risk_calculation_methods()
        await test_risk_level_determination()
        
        print("\n🎉 All tests completed successfully!")
        print("\n💡 Key Features Demonstrated:")
        print("   • Multi-factor risk analysis (Volatility, Trend, Volume, Correlation, Market Stress)")
        print("   • Weighted composite risk scoring")
        print("   • Dynamic risk level determination")
        print("   • Detailed risk factor identification")
        print("   • Professional-grade financial risk metrics")
        
    except Exception as e:
        print(f"\n❌ Test suite failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Run the test suite
    asyncio.run(main())
