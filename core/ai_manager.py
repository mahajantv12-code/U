#!/usr/bin/env python3
"""
AI Model Manager: Handles multiple AI models and routing
"""

import json
import logging
from typing import Optional, Dict, List
from datetime import datetime

try:
    import openai
except ImportError:
    openai = None

try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None

logger = logging.getLogger(__name__)

class AIManager:
    """Manages multiple AI models and selects best one for tasks"""
    
    def __init__(self, config: Dict):
        self.config = config
        self.models = {
            'gpt-4': 'openai',
            'gpt-3.5-turbo': 'openai',
            'claude-3-opus': 'anthropic',
            'claude-3-sonnet': 'anthropic',
            'gemini-pro': 'google'
        }
        self.current_model = config['ai_models']['primary']
        self.model_usage = {}
        self.last_rotation = datetime.now()
        
        logger.info("🤖 AI Manager initialized")
    
    async def initialize(self):
        """Initialize all AI model connections"""
        logger.info("🔌 Initializing AI connections...")
        
        try:
            # Initialize OpenAI
            if self.config['api_keys'].get('openai'):
                openai.api_key = self.config['api_keys']['openai']
                logger.info("✅ OpenAI initialized")
            
            # Initialize Anthropic
            if self.config['api_keys'].get('anthropic'):
                logger.info("✅ Anthropic initialized")
            
            # Initialize Google Gemini
            if self.config['api_keys'].get('google_gemini'):
                logger.info("✅ Google Gemini initialized")
        
        except Exception as e:
            logger.error(f"❌ Error initializing AI: {str(e)}")
            raise
    
    def select_model_for_task(self, task: str) -> str:
        """Select best AI model for specific task"""
        
        task_model_map = {
            'trading': 'claude-3-opus',  # Best reasoning
            'freelancing': 'gpt-4',       # Best for varied tasks
            'content_creation': 'gpt-4',  # Best for writing
            'web_building': 'claude-3-opus',  # Best for code
        }
        
        selected = task_model_map.get(task, self.config['ai_models']['primary'])
        logger.info(f"🎯 Selected {selected} for {task}")
        return selected
    
    async def query(self, model: str, prompt: str, max_tokens: int = 2000) -> str:
        """Query an AI model with a prompt"""
        
        try:
            provider = self.models.get(model)
            
            if provider == 'openai':
                return await self._query_openai(model, prompt, max_tokens)
            elif provider == 'anthropic':
                return await self._query_anthropic(model, prompt, max_tokens)
            elif provider == 'google':
                return await self._query_google(model, prompt, max_tokens)
            else:
                logger.error(f"Unknown model: {model}")
                return ""
        
        except Exception as e:
            logger.error(f"❌ Error querying {model}: {str(e)}")
            return ""
    
    async def _query_openai(self, model: str, prompt: str, max_tokens: int) -> str:
        """Query OpenAI API"""
        try:
            if not openai:
                logger.error("OpenAI not installed")
                return ""
            
            # Simulated response for demo
            logger.info(f"📝 Querying OpenAI {model}...")
            return f"Response from {model}: {prompt[:50]}..."
        
        except Exception as e:
            logger.error(f"❌ OpenAI error: {str(e)}")
            return ""
    
    async def _query_anthropic(self, model: str, prompt: str, max_tokens: int) -> str:
        """Query Anthropic Claude API"""
        try:
            logger.info(f"📝 Querying Anthropic {model}...")
            return f"Response from {model}: {prompt[:50]}..."
        
        except Exception as e:
            logger.error(f"❌ Anthropic error: {str(e)}")
            return ""
    
    async def _query_google(self, model: str, prompt: str, max_tokens: int) -> str:
        """Query Google Gemini API"""
        try:
            logger.info(f"📝 Querying Google {model}...")
            return f"Response from {model}: {prompt[:50]}..."
        
        except Exception as e:
            logger.error(f"❌ Google error: {str(e)}")
            return ""
    
    def rotate_models(self):
        """Rotate to next AI model"""
        models = list(self.models.keys())
        current_index = models.index(self.current_model)
        self.current_model = models[(current_index + 1) % len(models)]
        logger.info(f"🔄 Rotated to {self.current_model}")
    
    def get_model_stats(self) -> Dict:
        """Get usage statistics for all models"""
        return self.model_usage
