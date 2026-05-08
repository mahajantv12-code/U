#!/usr/bin/env python3
"""
Earnings Tracker: Track all income from different tasks
"""

import logging
from datetime import datetime, timedelta
from typing import Dict, List

logger = logging.getLogger(__name__)

class EarningsTracker:
    """Tracks earnings from all sources"""
    
    def __init__(self):
        self.earnings = []
        self.total_earned = 0.0
        self.daily_earned = {}
        
        logger.info("💰 Earnings Tracker initialized")
    
    def add_earning(self, task: str, amount: float, timestamp: datetime = None):
        """Record an earning"""
        if timestamp is None:
            timestamp = datetime.now()
        
        self.earnings.append({
            'task': task,
            'amount': amount,
            'timestamp': timestamp
        })
        
        self.total_earned += amount
        
        # Track daily earnings
        date_key = timestamp.strftime("%Y-%m-%d")
        if date_key not in self.daily_earned:
            self.daily_earned[date_key] = 0.0
        self.daily_earned[date_key] += amount
        
        logger.info(f"✅ Recorded ${amount} from {task}")
    
    def get_total_earnings(self) -> float:
        """Get total earnings"""
        return self.total_earned
    
    def get_today_earnings(self) -> float:
        """Get today's earnings"""
        today = datetime.now().strftime("%Y-%m-%d")
        return self.daily_earned.get(today, 0.0)
    
    def get_weekly_earnings(self) -> float:
        """Get earnings from last 7 days"""
        week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        total = 0.0
        
        for date, amount in self.daily_earned.items():
            if date >= week_ago:
                total += amount
        
        return total
    
    def get_monthly_earnings(self) -> float:
        """Get earnings from last 30 days"""
        month_ago = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        total = 0.0
        
        for date, amount in self.daily_earned.items():
            if date >= month_ago:
                total += amount
        
        return total
    
    def get_earnings_by_task(self) -> Dict[str, float]:
        """Get earnings breakdown by task"""
        breakdown = {}
        
        for earning in self.earnings:
            task = earning['task']
            if task not in breakdown:
                breakdown[task] = 0.0
            breakdown[task] += earning['amount']
        
        return breakdown
    
    def get_task_count(self) -> int:
        """Get number of tasks completed"""
        return len(self.earnings)
    
    def get_success_rate(self) -> float:
        """Get success rate (positive earnings count / total tasks)"""
        if not self.earnings:
            return 0.0
        
        successful = sum(1 for e in self.earnings if e['amount'] > 0)
        return (successful / len(self.earnings)) * 100
