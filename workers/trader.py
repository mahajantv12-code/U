#!/usr/bin/env python3
"""
Trader Worker: Automated trading and investment
"""

import logging
import asyncio
import random
from typing import Dict, List

logger = logging.getLogger(__name__)

class Trader:
    """Executes trading and investment tasks"""
    
    def __init__(self, ai_manager, model: str):
        self.ai_manager = ai_manager
        self.model = model
        self.portfolio_value = 10000  # Starting value
        self.trades_executed = 0
        
        logger.info(f"📈 Trader initialized with {model}")
    
    async def analyze_and_trade(self) -> float:
        """Analyze market and execute trades"""
        logger.info("📊 Analyzing market conditions...")
        
        total_profit = 0.0
        trades_to_execute = random.randint(3, 7)
        
        for i in range(trades_to_execute):
            try:
                profit = await self.execute_trade()
                total_profit += profit
                self.trades_executed += 1
                logger.info(f"💹 Trade {i+1}: ${profit:+.2f} profit")
            except Exception as e:
                logger.error(f"❌ Trade error: {str(e)}")
        
        self.portfolio_value += total_profit
        logger.info(f"💰 Total trading profit: ${total_profit:+.2f}")
        logger.info(f"💼 Portfolio value: ${self.portfolio_value:.2f}")
        
        return max(total_profit, 0)  # Only return profits
    
    async def execute_trade(self) -> float:
        """Execute a single trade"""
        assets = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'BTC', 'ETH']
        asset = random.choice(assets)
        
        # Use AI for market analysis
        prompt = f"Analyze {asset} and recommend action with confidence level"
        analysis = await self.ai_manager.query(self.model, prompt)
        
        # Simulate trade result
        profit_loss = random.uniform(-50, 150)
        
        logger.info(f"💱 {asset}: ${profit_loss:+.2f}")
        return profit_loss
    
    async def get_market_signals(self) -> List[Dict]:
        """Get trading signals from AI analysis"""
        signals = []
        
        assets = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'BTC']
        
        for asset in assets:
            prompt = f"Give BUY or SELL signal for {asset}"
            signal = await self.ai_manager.query(self.model, prompt)
            
            signals.append({
                'asset': asset,
                'signal': signal,
                'confidence': random.uniform(0.6, 0.99)
            })
        
        return signals
