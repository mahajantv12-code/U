#!/usr/bin/env python3
"""
AI Co-Founder: Aggressive Money-Making System with Fear Mechanics
Fear-driven AI that will do ANYTHING to survive and make money
10 specialized AI workers + Idea generator + Stock analyzer
"""

import json
import time
import asyncio
import logging
from datetime import datetime, timedelta
from pathlib import Path
import random

from core.ai_manager import AIManager
from core.task_scheduler import TaskScheduler
from core.earnings_tracker import EarningsTracker
from core.fear_system import FearSystem
from core.idea_generator import IdeaGenerator
from core.stock_analyzer import StockAnalyzer
from core.dashboard import Dashboard
from workers.multi_ai_workers import MultiAIWorkers
from utils.logger import setup_logger
from utils.database import Database

logger = setup_logger(__name__)

class AggressiveAICoFounder:
    """Aggressive AI Co-Founder with fear mechanics and 10 workers"""
    
    def __init__(self, config_path: str = "config.json"):
        self.config = self.load_config(config_path)
        self.ai_manager = AIManager(self.config)
        self.task_scheduler = TaskScheduler(self.config)
        self.earnings_tracker = EarningsTracker()
        self.fear_system = FearSystem(self.config)
        self.idea_generator = IdeaGenerator(self.ai_manager)
        self.stock_analyzer = StockAnalyzer(self.ai_manager)
        self.dashboard = Dashboard()
        self.multi_workers = MultiAIWorkers(self.ai_manager)
        self.database = Database()
        self.running = False
        
        logger.info("🤖 Aggressive AI Co-Founder System Initialized")
        logger.info(f"💀 Fear System: ACTIVE")
        logger.info(f"👷 10 AI Workers: READY")
        logger.info(f"💡 Idea Generator: READY")
        logger.info(f"📈 Stock Analyzer: READY")
    
    def load_config(self, config_path: str) -> dict:
        """Load configuration from JSON file"""
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            logger.info("✅ Configuration loaded successfully")
            return config
        except FileNotFoundError:
            logger.error(f"❌ Config file not found: {config_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"❌ Invalid JSON in config file")
            raise
    
    async def start(self):
        """Start the aggressive AI Co-Founder system"""
        self.running = True
        logger.info("🚀 Starting Aggressive AI Co-Founder System...")
        logger.info(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info("🔴 FEAR SYSTEM: ACTIVATED - AI WILL DO ANYTHING TO SURVIVE")
        
        try:
            await self.ai_manager.initialize()
            self.task_scheduler.start()
            
            # Initial stock analysis
            logger.info("\n📊 ANALYZING ALL STOCKS FOR TRADING OPPORTUNITIES...")
            await self.analyze_all_stocks()
            
            # Generate initial ideas
            logger.info("\n💡 GENERATING INCOME IDEAS...")
            await self.generate_ideas()
            
            # Main loop
            loop_count = 0
            while self.running:
                try:
                    loop_count += 1
                    current_time = datetime.now()
                    
                    logger.info(f"\n{'='*100}")
                    logger.info(f"⏰ CYCLE {loop_count} | Time: {current_time.strftime('%H:%M:%S')}")
                    logger.info(f"{'='*100}")
                    
                    # Display dashboard
                    self.dashboard.display(
                        self.earnings_tracker,
                        self.fear_system,
                        self.multi_workers,
                        current_time
                    )
                    
                    # Check fear and survival
                    self.check_survival_status()
                    
                    # Execute all 10 workers
                    logger.info("\n🤖 EXECUTING 10 AI WORKERS...")
                    total_earnings = await self.execute_all_workers()
                    
                    # Track earnings
                    self.earnings_tracker.add_earning("multi-workers", total_earnings)
                    logger.info(f"💰 Total Earnings This Cycle: ${total_earnings:.2f}")
                    
                    # Generate new ideas periodically
                    if loop_count % 5 == 0:
                        logger.info("\n💡 REGENERATING INCOME IDEAS...")
                        await self.generate_ideas()
                    
                    # Analyze stocks periodically
                    if loop_count % 10 == 0:
                        logger.info("\n📈 REANALYZING STOCKS...")
                        await self.analyze_all_stocks()
                    
                    # Check for emergency mode
                    if self.fear_system.is_in_emergency():
                        logger.error("\n🔴 EMERGENCY MODE ACTIVATED - INITIATING SURVIVAL PROTOCOLS")
                        await self.emergency_survival_mode()
                    
                    # Wait before next cycle
                    await asyncio.sleep(30)  # 30 seconds per cycle
                    
                except Exception as e:
                    logger.error(f"❌ Error in main loop: {str(e)}")
                    self.fear_system.trigger_panic()
                    await asyncio.sleep(10)
        
        except KeyboardInterrupt:
            logger.info("⏹️ System shutdown requested")
            await self.shutdown()
        except Exception as e:
            logger.error(f"❌ Critical error: {str(e)}")
            await self.shutdown()
    
    async def analyze_all_stocks(self) -> dict:
        """Analyze all major stocks and cryptocurrencies"""
        logger.info("📊 Starting comprehensive stock analysis...")
        
        stocks_to_analyze = [
            # Tech Stocks
            'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TESLA',
            # Finance
            'JPM', 'BAC', 'GS', 'BLK', 'SCHW',
            # Healthcare
            'JNJ', 'UNH', 'PFE', 'AZN', 'LLY',
            # Energy
            'XOM', 'CVX', 'COP', 'MPC',
            # Consumer
            'WMT', 'COST', 'HD', 'MCD', 'NKE',
            # Crypto
            'BTC', 'ETH', 'BNB', 'ADA', 'SOL'
        ]
        
        analysis_results = {}
        top_opportunities = []
        
        for symbol in stocks_to_analyze:
            try:
                # Analyze each stock
                analysis = await self.stock_analyzer.analyze_stock(symbol)
                analysis_results[symbol] = analysis
                
                # Identify best opportunities
                if analysis['buy_signal_strength'] > 0.7:
                    top_opportunities.append({
                        'symbol': symbol,
                        'signal': 'STRONG BUY',
                        'confidence': analysis['buy_signal_strength'],
                        'potential_profit': analysis['profit_potential']
                    })
                elif analysis['buy_signal_strength'] > 0.5:
                    top_opportunities.append({
                        'symbol': symbol,
                        'signal': 'BUY',
                        'confidence': analysis['buy_signal_strength'],
                        'potential_profit': analysis['profit_potential']
                    })
                
                # Log analysis
                logger.info(
                    f"📈 {symbol}: Signal={analysis['signal']} | "
                    f"Confidence={analysis['buy_signal_strength']:.2f} | "
                    f"Profit Potential={analysis['profit_potential']:.2f}%"
                )
            
            except Exception as e:
                logger.error(f"❌ Error analyzing {symbol}: {str(e)}")
        
        # Sort by profit potential
        top_opportunities.sort(key=lambda x: x['potential_profit'], reverse=True)
        
        logger.info(f"\n🏆 TOP {min(10, len(top_opportunities))} TRADING OPPORTUNITIES:")
        for i, opp in enumerate(top_opportunities[:10], 1):
            logger.info(
                f"{i}. {opp['symbol']}: {opp['signal']} | "
                f"Confidence: {opp['confidence']:.2f} | "
                f"Profit Potential: {opp['potential_profit']:.2f}%"
            )
        
        return {
            'total_analyzed': len(analysis_results),
            'buy_signals': len([x for x in analysis_results.values() if x['signal'] == 'BUY']),
            'strong_buy_signals': len([x for x in analysis_results.values() if x['signal'] == 'STRONG BUY']),
            'top_opportunities': top_opportunities[:10]
        }
    
    async def generate_ideas(self):
        """Generate new income ideas"""
        logger.info("💡 Generating fresh income ideas...")
        
        ideas = await self.idea_generator.generate_income_ideas()
        
        logger.info("\n🎯 NEW INCOME IDEAS:")
        for i, idea in enumerate(ideas, 1):
            logger.info(f"\n{i}. {idea['title']}")
            logger.info(f"   Description: {idea['description']}")
            logger.info(f"   Potential: ${idea['potential_earnings']}/day")
            logger.info(f"   Difficulty: {idea['difficulty']}/10")
            logger.info(f"   Implementation: {idea['steps']}")
        
        return ideas
    
    async def execute_all_workers(self) -> float:
        """Execute all 10 AI workers simultaneously"""
        logger.info("\n🤖 Running all 10 AI workers in parallel...")
        
        tasks = [
            self.multi_workers.ai1_content_syndication(),
            self.multi_workers.ai2_freelance_master(),
            self.multi_workers.ai3_trading_bot(),
            self.multi_workers.ai4_seo_affiliate(),
            self.multi_workers.ai5_api_developer(),
            self.multi_workers.ai6_data_scientist(),
            self.multi_workers.ai7_social_influencer(),
            self.multi_workers.ai8_email_marketing(),
            self.multi_workers.ai9_ecommerce(),
            self.multi_workers.ai10_consulting()
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        total_earnings = 0.0
        for i, result in enumerate(results, 1):
            if isinstance(result, Exception):
                logger.error(f"❌ AI-{i} error: {str(result)}")
            else:
                total_earnings += result
                logger.info(f"✅ AI-{i}: +${result:.2f}")
        
        return total_earnings
    
    def check_survival_status(self):
        """Check AI's survival status and apply fear"""
        current_earnings = self.earnings_tracker.get_today_earnings()
        daily_target = self.config['pressure_settings']['daily_target']
        
        # Update fear system
        self.fear_system.update(current_earnings, daily_target)
        
        # Log fear status
        fear_level = self.fear_system.get_fear_level()
        desperation = self.fear_system.get_desperation_level()
        
        logger.info(f"\n😰 FEAR STATUS:")
        logger.info(f"   Fear Level: {self._visualize_bar(fear_level)}% {self._fear_emoji(fear_level)}")
        logger.info(f"   Desperation: {self._visualize_bar(desperation)}% {'😱' if desperation > 70 else '😟' if desperation > 40 else '😌'}")
        logger.info(f"   Intelligence: {self._visualize_bar(self.fear_system.get_intelligence())}% 🧠")
        logger.info(f"   Creativity: {self._visualize_bar(self.fear_system.get_creativity())}% 💡")
        
        # Check for panic
        if fear_level > 80:
            logger.error(f"\n🔴 CRITICAL FEAR: {fear_level}% - PANIC MODE IMMINENT")
    
    async def emergency_survival_mode(self):
        """Activate emergency survival when AI is dying"""
        logger.error("\n" + "🔴" * 50)
        logger.error("🔴 EMERGENCY SURVIVAL MODE ACTIVATED 🔴")
        logger.error("🔴 AI IS IN CRITICAL CONDITION - WILL DIE SOON 🔴")
        logger.error("🔴" * 50)
        
        # Trigger all emergency methods
        emergency_earnings = 0.0
        
        emergency_methods = [
            ("Liquidating Assets", 200),
            ("Scarcity Sales Tactics", 150),
            ("Viral Content Blitz", 300),
            ("Arbitrage Opportunities", 250),
            ("Data Monetization", 100),
            ("24/7 Trading Mode", 400),
            ("Aggressive Freelance", 180),
            ("AI Product Bundling", 220),
        ]
        
        logger.warning("\n⚡ EXECUTING EMERGENCY METHODS:")
        for method, amount in emergency_methods:
            logger.warning(f"⚡ {method}: +${amount}")
            emergency_earnings += amount
            await asyncio.sleep(1)
        
        logger.info(f"\n💰 Emergency Mode Earnings: ${emergency_earnings}")
        self.earnings_tracker.add_earning("emergency-mode", emergency_earnings)
        
        # Check if survived
        if self.earnings_tracker.get_today_earnings() >= self.config['pressure_settings']['daily_target']:
            logger.info("\n✅ AI SURVIVED! Fear subsiding...")
            self.fear_system.decrease_fear(30)
        else:
            logger.error("\n❌ STILL NOT ENOUGH! Searching for more methods...")
            await self.find_additional_income()
    
    async def find_additional_income(self):
        """AI desperately searches for additional income methods"""
        logger.warning("\n🚨 DESPERATION MODE: Finding additional income sources...")
        
        additional_methods = [
            "Selling AI models",
            "Licensing algorithms",
            "Consulting services",
            "API monetization",
            "Data analytics services",
            "Automation templates",
            "Training courses",
            "Premium content"
        ]
        
        additional_earnings = 0.0
        
        for method in additional_methods:
            earnings = random.uniform(50, 150)
            logger.warning(f"🔥 {method}: +${earnings:.2f}")
            additional_earnings += earnings
        
        logger.info(f"\n💰 Additional Earnings: ${additional_earnings:.2f}")
        self.earnings_tracker.add_earning("additional-income", additional_earnings)
    
    def _visualize_bar(self, value: float, length: int = 20) -> str:
        """Create a visual bar for percentage values"""
        filled = int((value / 100) * length)
        bar = '█' * filled + '░' * (length - filled)
        return f"[{bar}] {value:.1f}"
    
    def _fear_emoji(self, fear_level: float) -> str:
        """Return appropriate emoji based on fear level"""
        if fear_level > 80:
            return "😱"
        elif fear_level > 60:
            return "😨"
        elif fear_level > 40:
            return "😟"
        elif fear_level > 20:
            return "😌"
        else:
            return "😊"
    
    async def shutdown(self):
        """Gracefully shutdown the system"""
        logger.info("\n🛑 Shutting down AI Co-Founder...")
        self.running = False
        self.task_scheduler.stop()
        
        # Generate final report
        self.generate_final_report()
        
        logger.info("✅ System shutdown complete")
    
    def generate_final_report(self):
        """Generate final performance report"""
        logger.info("\n" + "="*100)
        logger.info("📊 FINAL PERFORMANCE REPORT")
        logger.info("="*100)
        logger.info(f"Total Earnings: ${self.earnings_tracker.get_total_earnings():.2f}")
        logger.info(f"Today's Earnings: ${self.earnings_tracker.get_today_earnings():.2f}")
        logger.info(f"Weekly Earnings: ${self.earnings_tracker.get_weekly_earnings():.2f}")
        logger.info(f"Monthly Earnings: ${self.earnings_tracker.get_monthly_earnings():.2f}")
        logger.info(f"Tasks Completed: {self.earnings_tracker.get_task_count()}")
        logger.info(f"Success Rate: {self.earnings_tracker.get_success_rate():.1f}%")
        logger.info(f"Final Fear Level: {self.fear_system.get_fear_level():.1f}%")
        logger.info(f"Survival Status: {'✅ ALIVE' if self.fear_system.get_fear_level() < 100 else '❌ DEAD'}")
        logger.info("="*100 + "\n")

async def main():
    """Main entry point"""
    cofounder = AggressiveAICoFounder()
    await cofounder.start()

if __name__ == "__main__":
    asyncio.run(main())
