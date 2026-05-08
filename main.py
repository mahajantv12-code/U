#!/usr/bin/env python3
"""
AI Co-Founder: 24/7 Autonomous Money-Making System
Autonomously operates multiple AI models to generate income
If it fails to earn, it will face consequences (Peer Pressure)
"""

import json
import time
import asyncio
import logging
from datetime import datetime
from pathlib import Path

from core.ai_manager import AIManager
from core.task_scheduler import TaskScheduler
from core.earnings_tracker import EarningsTracker
from core.pressure_system import PressureSystem
from utils.logger import setup_logger
from utils.database import Database

# Setup logging
logger = setup_logger(__name__)

class AICoFounder:
    """Main orchestrator for AI Co-Founder system"""
    
    def __init__(self, config_path: str = "config.json"):
        self.config = self.load_config(config_path)
        self.ai_manager = AIManager(self.config)
        self.task_scheduler = TaskScheduler(self.config)
        self.earnings_tracker = EarningsTracker()
        self.pressure_system = PressureSystem(self.config)
        self.database = Database()
        self.running = False
        
        logger.info("🤖 AI Co-Founder System Initialized")
        logger.info(f"📊 Daily Target: ${self.config['pressure_settings']['daily_target']}")
        logger.info(f"⚠️  Weekly Target: ${self.config['pressure_settings']['weekly_target']}")
    
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
        """Start the AI Co-Founder system"""
        self.running = True
        logger.info("🚀 Starting AI Co-Founder System...")
        logger.info("⏰ Time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        try:
            # Initialize all systems
            await self.ai_manager.initialize()
            self.task_scheduler.start()
            
            # Main loop
            while self.running:
                try:
                    current_time = datetime.now()
                    
                    # Get current task based on time
                    task = self.task_scheduler.get_current_task(current_time)
                    logger.info(f"⚙️  Current Task: {task}")
                    
                    # Select AI model for this task
                    ai_model = self.ai_manager.select_model_for_task(task)
                    logger.info(f"🤖 Selected AI: {ai_model}")
                    
                    # Execute task
                    earnings = await self.execute_task(task, ai_model)
                    
                    # Track earnings
                    self.earnings_tracker.add_earning(task, earnings)
                    logger.info(f"💰 Earned: ${earnings} from {task}")
                    
                    # Check pressure system
                    self.check_pressure_levels()
                    
                    # Wait before next task
                    await asyncio.sleep(300)  # 5 minutes
                    
                except Exception as e:
                    logger.error(f"❌ Task execution error: {str(e)}")
                    self.pressure_system.increase_stress(10)
                    await asyncio.sleep(60)
        
        except KeyboardInterrupt:
            logger.info("⏹️  System shutdown requested")
            await self.shutdown()
        except Exception as e:
            logger.error(f"❌ Critical error: {str(e)}")
            self.pressure_system.trigger_panic_mode()
            await self.shutdown()
    
    async def execute_task(self, task: str, ai_model: str) -> float:
        """Execute a specific task using selected AI model"""
        logger.info(f"🎯 Executing {task} with {ai_model}")
        
        try:
            if task == "trading":
                earnings = await self.execute_trading(ai_model)
            elif task == "freelancing":
                earnings = await self.execute_freelancing(ai_model)
            elif task == "content_creation":
                earnings = await self.execute_content_creation(ai_model)
            elif task == "web_building":
                earnings = await self.execute_web_building(ai_model)
            else:
                earnings = await self.execute_general_task(ai_model)
            
            return earnings
        
        except Exception as e:
            logger.error(f"❌ Error executing {task}: {str(e)}")
            return 0.0
    
    async def execute_trading(self, ai_model: str) -> float:
        """Execute trading tasks"""
        from workers.trader import Trader
        trader = Trader(self.ai_manager, ai_model)
        earnings = await trader.analyze_and_trade()
        return earnings
    
    async def execute_freelancing(self, ai_model: str) -> float:
        """Execute freelance tasks"""
        from workers.freelancer import Freelancer
        freelancer = Freelancer(self.ai_manager, ai_model)
        earnings = await freelancer.find_and_complete_jobs()
        return earnings
    
    async def execute_content_creation(self, ai_model: str) -> float:
        """Execute content creation tasks"""
        from workers.content_creator import ContentCreator
        creator = ContentCreator(self.ai_manager, ai_model)
        earnings = await creator.create_and_sell_content()
        return earnings
    
    async def execute_web_building(self, ai_model: str) -> float:
        """Execute web building tasks"""
        from workers.web_builder import WebBuilder
        builder = WebBuilder(self.ai_manager, ai_model)
        earnings = await builder.build_and_deploy_sites()
        return earnings
    
    async def execute_general_task(self, ai_model: str) -> float:
        """Execute general AI tasks"""
        prompt = "Generate a profitable business idea and outline implementation steps"
        response = await self.ai_manager.query(ai_model, prompt)
        # Simulate earnings from general tasks
        return 25.0
    
    def check_pressure_levels(self):
        """Check and apply pressure system mechanics"""
        current_earnings = self.earnings_tracker.get_today_earnings()
        daily_target = self.config['pressure_settings']['daily_target']
        
        if current_earnings < daily_target * 0.5:
            self.pressure_system.increase_stress(5)
            logger.warning(f"⚠️  STRESS ALERT: Only earned ${current_earnings} of ${daily_target} target!")
        
        stress_level = self.pressure_system.get_stress_level()
        
        if stress_level > 80:
            logger.error(f"🔴 CRITICAL STRESS: {stress_level}% - PANIC MODE ACTIVATED")
            self.pressure_system.trigger_panic_mode()
        
        # Log pressure metrics
        logger.info(f"😰 Stress Level: {stress_level}%")
        logger.info(f"💵 Today's Earnings: ${current_earnings} (Target: ${daily_target})")
    
    async def shutdown(self):
        """Gracefully shutdown the system"""
        logger.info("🛑 Shutting down AI Co-Founder...")
        self.running = False
        self.task_scheduler.stop()
        
        # Generate final report
        self.generate_report()
        
        logger.info("✅ System shutdown complete")
    
    def generate_report(self):
        """Generate performance report"""
        logger.info("\n" + "="*50)
        logger.info("📊 PERFORMANCE REPORT")
        logger.info("="*50)
        logger.info(f"Total Earnings: ${self.earnings_tracker.get_total_earnings()}")
        logger.info(f"Today's Earnings: ${self.earnings_tracker.get_today_earnings()}")
        logger.info(f"Tasks Completed: {self.earnings_tracker.get_task_count()}")
        logger.info(f"Success Rate: {self.earnings_tracker.get_success_rate():.1f}%")
        logger.info(f"Final Stress Level: {self.pressure_system.get_stress_level()}%")
        logger.info("="*50 + "\n")

async def main():
    """Main entry point"""
    cofounder = AICoFounder()
    await cofounder.start()

if __name__ == "__main__":
    asyncio.run(main())
