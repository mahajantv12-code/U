#!/usr/bin/env python3
"""
Pressure System: Apply peer pressure mechanics for performance
"""

import logging
from typing import Dict
from datetime import datetime

logger = logging.getLogger(__name__)

class PressureSystem:
    """Applies pressure mechanics to ensure performance"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.stress_level = 0  # 0-100%
        self.panic_mode = False
        self.failed_tasks = 0
        self.consecutive_failures = 0
        
        logger.info("😰 Pressure System initialized")
    
    def increase_stress(self, amount: int):
        """Increase stress level"""
        self.stress_level = min(100, self.stress_level + amount)
        self._visualize_stress()
        
        if self.stress_level > 75:
            logger.warning(f"⚠️  HIGH STRESS: {self.stress_level}%")
    
    def decrease_stress(self, amount: int):
        """Decrease stress level"""
        self.stress_level = max(0, self.stress_level - amount)
        self._visualize_stress()
    
    def get_stress_level(self) -> int:
        """Get current stress level"""
        return self.stress_level
    
    def _visualize_stress(self):
        """Visualize stress level in logs"""
        bar_length = 20
        filled = int((self.stress_level / 100) * bar_length)
        bar = '█' * filled + '░' * (bar_length - filled)
        logger.info(f"Stress Level: [{bar}] {self.stress_level}%")
    
    def record_failure(self):
        """Record a task failure"""
        self.failed_tasks += 1
        self.consecutive_failures += 1
        self.increase_stress(15)
        
        logger.error(f"❌ Task failed! ({self.consecutive_failures} consecutive)")
        
        if self.consecutive_failures >= 3:
            self.trigger_panic_mode()
    
    def record_success(self):
        """Record a task success"""
        self.consecutive_failures = 0
        self.decrease_stress(5)
        logger.info("✅ Task successful! Stress reduced.")
    
    def trigger_panic_mode(self):
        """Trigger panic mode when system is failing"""
        self.panic_mode = True
        self.stress_level = 100
        
        logger.error("🔴 " * 20)
        logger.error("PANIC MODE ACTIVATED!")
        logger.error("The AI Co-Founder is in critical condition.")
        logger.error("Attempting emergency recovery...")
        logger.error("If recovery fails, the AI will be terminated.")
        logger.error("🔴 " * 20)
        
        # Trigger aggressive mode
        self._aggressive_mode()
    
    def _aggressive_mode(self):
        """Activate aggressive task execution"""
        logger.warning("⚡ AGGRESSIVE MODE: Executing all available tasks at maximum speed")
        logger.warning("⚡ Stress Level: 100% - CRITICAL")
        logger.warning("⚡ Failure will result in system termination")
    
    def exit_panic_mode(self):
        """Exit panic mode"""
        self.panic_mode = False
        self.stress_level = 50
        logger.info("✅ System recovered from panic mode")
    
    def get_performance_summary(self) -> Dict:
        """Get performance summary"""
        return {
            'stress_level': self.stress_level,
            'panic_mode': self.panic_mode,
            'failed_tasks': self.failed_tasks,
            'consecutive_failures': self.consecutive_failures,
            'status': '🔴 CRITICAL' if self.panic_mode else '🟡 WARNING' if self.stress_level > 75 else '🟢 NORMAL'
        }
