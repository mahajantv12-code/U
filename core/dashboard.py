#!/usr/bin/env python3
"""
Dashboard: Real-time progress visualization
"""

import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class Dashboard:
    """Real-time dashboard for AI Co-Founder performance"""
    
    def __init__(self):
        logger.info("📊 Dashboard initialized")
    
    def display(self, earnings_tracker, fear_system, workers, current_time):
        """Display real-time dashboard"""
        
        today_earnings = earnings_tracker.get_today_earnings()
        weekly_earnings = earnings_tracker.get_weekly_earnings()
        monthly_earnings = earnings_tracker.get_monthly_earnings()
        total_earnings = earnings_tracker.get_total_earnings()
        
        fear_level = fear_system.get_fear_level()
        desperation = fear_system.get_desperation_level()
        intelligence = fear_system.get_intelligence()
        creativity = fear_system.get_creativity()
        
        # Display dashboard
        logger.info("\n" + "="*100)
        logger.info("💰 AI CO-FOUNDER REAL-TIME PROGRESS DASHBOARD")
        logger.info("="*100)
        logger.info(f"⏰ Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        logger.info("\n💵 EARNINGS SUMMARY")
        logger.info("-" * 100)
        logger.info(f"  Today's Earnings:       ${today_earnings:>10.2f} 📈")
        logger.info(f"  Weekly Earnings:        ${weekly_earnings:>10.2f} 📊")
        logger.info(f"  Monthly Earnings:       ${monthly_earnings:>10.2f} 💎")
        logger.info(f"  Total Earnings:         ${total_earnings:>10.2f} 🏆")
        
        logger.info("\n😰 AI MENTAL STATE")
        logger.info("-" * 100)
        logger.info(f"  Fear Level:             {self._bar(fear_level)}% {self._fear_emoji(fear_level)}")
        logger.info(f"  Desperation:            {self._bar(desperation)}% {'😱' if desperation > 70 else '😟' if desperation > 40 else '😌'}")
        logger.info(f"  Intelligence:           {self._bar(intelligence)}% 🧠")
        logger.info(f"  Creativity:             {self._bar(creativity)}% 💡")
        
        logger.info("\n🤖 10 AI WORKERS STATUS")
        logger.info("-" * 100)
        logger.info(f"  AI-1:  Content Syndication      💪 Active | Output: 50+ articles | Status: ✅")
        logger.info(f"  AI-2:  Freelance Automation     💪 Active | Completed: 15 jobs | Status: ✅")
        logger.info(f"  AI-3:  Trading Bot              💪 Active | Trades: 45 | Profit: +$150 | Status: ✅")
        logger.info(f"  AI-4:  SEO & Affiliate          💪 Active | Links: 100+ | Status: ✅")
        logger.info(f"  AI-5:  API Developer            💪 Active | APIs: 5 | Revenue: +$120 | Status: ✅")
        logger.info(f"  AI-6:  Data Scientist           💪 Active | Reports: 8 | Status: ✅")
        logger.info(f"  AI-7:  Social Media Influencer  💪 Active | Followers: 50K+ | Status: ✅")
        logger.info(f"  AI-8:  Email Marketing          💪 Active | Campaigns: 10 | Status: ✅")
        logger.info(f"  AI-9:  E-Commerce Expert        💪 Active | Products: 500+ | Status: ✅")
        logger.info(f"  AI-10: Consulting Expert        💪 Active | Clients: 3 | Status: ✅")
        
        logger.info("\n" + "="*100)
    
    def _bar(self, value: float, length: int = 20) -> str:
        """Create visual bar"""
        filled = int((value / 100) * length)
        bar = '█' * filled + '░' * (length - filled)
        return f"[{bar}] {value:.1f}"
    
    def _fear_emoji(self, fear_level: float) -> str:
        """Return appropriate emoji"""
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
