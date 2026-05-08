#!/usr/bin/env python3
"""
Task Scheduler: 24/7 task distribution based on time
"""

import logging
from datetime import datetime
from typing import Dict, Optional
from apscheduler.schedulers.background import BackgroundScheduler

logger = logging.getLogger(__name__)

class TaskScheduler:
    """Schedules different AI tasks throughout the day"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.scheduler = BackgroundScheduler()
        self.schedule_map = config['daily_schedule']
        self.current_task = None
        
        logger.info("📅 Task Scheduler initialized")
    
    def start(self):
        """Start the scheduler"""
        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("🚀 Task Scheduler started")
    
    def stop(self):
        """Stop the scheduler"""
        if self.scheduler.running:
            self.scheduler.shutdown()
            logger.info("⏹️  Task Scheduler stopped")
    
    def get_current_task(self, current_time: datetime) -> str:
        """Get task for current time"""
        hour = current_time.hour
        
        # Map hour to task
        if 0 <= hour < 6:
            return "trading"
        elif 6 <= hour < 12:
            return "freelancing"
        elif 12 <= hour < 18:
            return "content_creation"
        elif 18 <= hour < 24:
            return "web_building"
        else:
            return "general"
    
    def schedule_task(self, hour: int, minute: int, task_name: str, callback):
        """Schedule a specific task"""
        try:
            self.scheduler.add_job(
                callback,
                'cron',
                hour=hour,
                minute=minute,
                id=f"{task_name}_{hour}_{minute}"
            )
            logger.info(f"✅ Scheduled {task_name} at {hour:02d}:{minute:02d}")
        except Exception as e:
            logger.error(f"❌ Error scheduling task: {str(e)}")
    
    def get_schedule_info(self) -> Dict:
        """Get current schedule information"""
        current_time = datetime.now()
        current_task = self.get_current_task(current_time)
        
        return {
            'current_time': current_time.strftime("%H:%M:%S"),
            'current_task': current_task,
            'next_task_in_minutes': self._get_next_task_time(current_time)
        }
    
    def _get_next_task_time(self, current_time: datetime) -> int:
        """Calculate minutes until next task"""
        hour = current_time.hour
        
        if hour < 6:
            next_hour = 6
        elif hour < 12:
            next_hour = 12
        elif hour < 18:
            next_hour = 18
        else:
            next_hour = 24
        
        minutes_remaining = (next_hour - hour - 1) * 60 + (60 - current_time.minute)
        return minutes_remaining
