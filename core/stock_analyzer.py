#!/usr/bin/env python3
"""
Stock Analyzer: Analyzes stocks and identifies trading opportunities
"""

import logging
import random
from typing import Dict, List

logger = logging.getLogger(__name__)

class StockAnalyzer:
    """Comprehensive stock analysis for trading"""
    
    def __init__(self, ai_manager):
        self.ai_manager = ai_manager
        self.analysis_cache = {}
        logger.info("📈 Stock Analyzer initialized")
    
    async def analyze_stock(self, symbol: str) -> Dict:
        """Analyze a single stock"""
        
        try:
            # Simulate real analysis
            price = random.uniform(10, 500)
            volatility = random.uniform(0.1, 0.5)
            volume_trend = random.uniform(0.8, 1.2)
            
            # Generate signals
            buy_signal_strength = self._calculate_buy_signal(price, volatility, volume_trend)
            profit_potential = self._calculate_profit_potential(volatility, volume_trend)
            
            analysis = {
                'symbol': symbol,
                'price': price,
                'volatility': volatility,
                'volume_trend': volume_trend,
                'buy_signal_strength': buy_signal_strength,
                'profit_potential': profit_potential,
                'signal': self._get_signal(buy_signal_strength),
                'recommendation': self._get_recommendation(buy_signal_strength),
                'support_level': price * 0.95,
                'resistance_level': price * 1.05
            }
            
            self.analysis_cache[symbol] = analysis
            return analysis
        
        except Exception as e:
            logger.error(f"❌ Error analyzing {symbol}: {str(e)}")
            return {}
    
    def _calculate_buy_signal(self, price: float, volatility: float, volume_trend: float) -> float:
        """Calculate buy signal strength (0-1)"""
        # Simulate technical analysis
        signal = (
            (1 - volatility) * 0.4 +  # Lower volatility = better
            (volume_trend - 0.8) * 0.6  # Volume increase = better
        )
        return max(0, min(1, signal + random.uniform(-0.1, 0.2)))
    
    def _calculate_profit_potential(self, volatility: float, volume_trend: float) -> float:
        """Calculate profit potential percentage"""
        potential = (
            volatility * 200 +  # Higher volatility = more potential
            (volume_trend - 1) * 100  # Volume increase = momentum
        )
        return min(50, max(5, potential))
    
    def _get_signal(self, buy_signal: float) -> str:
        """Get trading signal"""
        if buy_signal > 0.7:
            return "STRONG BUY"
        elif buy_signal > 0.5:
            return "BUY"
        elif buy_signal > 0.3:
            return "HOLD"
        else:
            return "SELL"
    
    def _get_recommendation(self, buy_signal: float) -> str:
        """Get trading recommendation"""
        if buy_signal > 0.8:
            return "Immediate entry recommended - Strong uptrend"
        elif buy_signal > 0.6:
            return "Consider buying on dips - Positive momentum"
        elif buy_signal > 0.4:
            return "Wait for clearer signals - Neutral"
        else:
            return "Avoid buying - Downtrend expected"
    
    async def analyze_top_stocks(self, limit: int = 25) -> List[Dict]:
        """Analyze top stocks and return sorted by buy signal"""
        
        top_symbols = [
            'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TESLA',
            'JPM', 'BAC', 'GS', 'JNJ', 'UNH', 'PFE', 'XOM', 'CVX',
            'WMT', 'COST', 'HD', 'MCD', 'NKE', 'BTC', 'ETH', 'BNB', 'ADA', 'SOL'
        ]
        
        analyses = []
        for symbol in top_symbols[:limit]:
            analysis = await self.analyze_stock(symbol)
            analyses.append(analysis)
        
        # Sort by buy signal strength
        analyses.sort(key=lambda x: x['buy_signal_strength'], reverse=True)
        
        return analyses
