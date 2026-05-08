#!/usr/bin/env python3
"""
Content Creator Worker: Generate and sell content
"""

import logging
import asyncio
import random
from typing import List

logger = logging.getLogger(__name__)

class ContentCreator:
    """Creates and sells digital content"""
    
    def __init__(self, ai_manager, model: str):
        self.ai_manager = ai_manager
        self.model = model
        self.content_created = 0
        self.content_sold = 0
        
        logger.info(f"✍️  Content Creator initialized with {model}")
    
    async def create_and_sell_content(self) -> float:
        """Create content and simulate sales"""
        total_earnings = 0.0
        
        logger.info("📝 Creating content...")
        
        content_pieces = random.randint(3, 8)
        
        for i in range(content_pieces):
            try:
                earnings = await self.create_content_piece()
                total_earnings += earnings
                self.content_created += 1
                logger.info(f"📄 Content {i+1} created and sold: +${earnings}")
            except Exception as e:
                logger.error(f"❌ Error creating content: {str(e)}")
        
        logger.info(f"💰 Total content earnings: ${total_earnings}")
        return total_earnings
    
    async def create_content_piece(self) -> float:
        """Create a single piece of content"""
        content_types = [
            'Blog Post',
            'Email Sequence',
            'Sales Copy',
            'Social Media Content',
            'Product Description',
            'Tutorial Guide'
        ]
        
        content_type = random.choice(content_types)
        
        # Generate content using AI
        prompt = f"Create a compelling {content_type} about digital marketing"
        content = await self.ai_manager.query(self.model, prompt, max_tokens=3000)
        
        # Simulate sales
        earnings = random.uniform(15, 75)
        self.content_sold += 1
        
        logger.info(f"📤 {content_type} created: ${earnings:.2f}")
        return earnings
    
    async def publish_to_platforms(self) -> List[str]:
        """Publish content to multiple platforms"""
        platforms = [
            'Medium',
            'Dev.to',
            'Hashnode',
            'LinkedIn',
            'Twitter',
            'Content Marketplace'
        ]
        
        logger.info(f"📤 Publishing to {len(platforms)} platforms...")
        return platforms
