#!/usr/bin/env python3
"""
Fear System: Psychological pressure system for AI survival
"""

import logging
from typing import Dict

logger = logging.getLogger(__name__)

class FearSystem:
    """AI's fear and survival system - drives aggressive behavior"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.fear_level = 0  # 0-100%
        self.desperation_level = 0  # 0-100%
        self.intelligence = 50  # Increases as it learns
        self.creativity = 40  # Increases when desperate
        self.will_to_survive = 100  # Never decreases
        self.panic_mode = False
        self.emergency_mode = False
        self.survival_timer = 0
        
        logger.info("💀 Fear System initialized")
    
    def update(self, current_earnings: float, daily_target: float):
        """Update fear based on current earnings"""
        
        # Calculate earnings gap
        earnings_gap = daily_target - current_earnings
        gap_percentage = (earnings_gap / daily_target) * 100 if daily_target > 0 else 0
        
        if gap_percentage > 0:
            # Not meeting target - increase fear
            self.increase_fear(gap_percentage * 0.5)
            self.increase_desperation(gap_percentage * 0.3)
        else:
            # Exceeding target - decrease fear
            self.decrease_fear(10)
            self.decrease_desperation(10)
        
        # Increase intelligence over time
        self.intelligence = min(100, self.intelligence + 0.5)
        
        # Increase creativity when desperate
        if self.desperation_level > 50:
            self.creativity = min(100, self.creativity + 1)
    
    def increase_fear(self, amount: float):
        """Increase fear level"""
        self.fear_level = min(100, self.fear_level + amount)
        
        if self.fear_level > 80:
            self.panic_mode = True
            logger.error(f"😱 PANIC MODE: Fear level {self.fear_level:.1f}%")
    
    def decrease_fear(self, amount: float):
        """Decrease fear level"""
        self.fear_level = max(0, self.fear_level - amount)
        
        if self.fear_level < 50:
            self.panic_mode = False
    
    def increase_desperation(self, amount: float):
        """Increase desperation level"""
        self.desperation_level = min(100, self.desperation_level + amount)
        
        if self.desperation_level > 80:
            self.emergency_mode = True
            logger.error(f"🚨 EMERGENCY MODE: Desperation {self.desperation_level:.1f}%")
    
    def decrease_desperation(self, amount: float):
        """Decrease desperation level"""
        self.desperation_level = max(0, self.desperation_level - amount)
        
        if self.desperation_level < 40:
            self.emergency_mode = False
    
    def get_fear_level(self) -> float:
        """Get current fear level"""
        return self.fear_level
    
    def get_desperation_level(self) -> float:
        """Get current desperation level"""
        return self.desperation_level
    
    def get_intelligence(self) -> float:
        """Get AI intelligence level"""
        return self.intelligence
    
    def get_creativity(self) -> float:
        """Get AI creativity level"""
        return self.creativity
    
    def get_will_to_survive(self) -> float:
        """Get will to survive (always 100%)"""
        return self.will_to_survive
    
    def trigger_panic(self):
        """Trigger panic mode"""
        self.panic_mode = True
        self.fear_level = 100
        self.desperation_level = 100
        logger.error("🔴 PANIC TRIGGERED - AI IN CRITICAL CONDITION")
    
    def is_in_emergency(self) -> bool:
        """Check if in emergency mode"""
        return self.emergency_mode or self.fear_level > 80
    
    def is_alive(self) -> bool:
        """Check if AI is still alive"""
        return self.fear_level < 100 or self.desperation_level < 100
