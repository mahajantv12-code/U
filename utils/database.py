#!/usr/bin/env python3
"""
Database Manager: SQLite storage for earnings and metrics
"""

import sqlite3
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List

logger = logging.getLogger(__name__)

class Database:
    """SQLite database for persistent storage"""
    
    def __init__(self, db_path: str = 'data/ai_cofounder.db'):
        self.db_path = db_path
        Path('data').mkdir(exist_ok=True)
        self.init_db()
        
        logger.info("💾 Database initialized")
    
    def init_db(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create earnings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS earnings (
                id INTEGER PRIMARY KEY,
                task TEXT,
                amount REAL,
                timestamp TEXT,
                ai_model TEXT
            )
        ''')
        
        # Create metrics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS metrics (
                id INTEGER PRIMARY KEY,
                date TEXT,
                daily_earnings REAL,
                stress_level INTEGER,
                tasks_completed INTEGER,
                success_rate REAL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def insert_earning(self, task: str, amount: float, ai_model: str):
        """Insert earning record"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO earnings (task, amount, timestamp, ai_model)
            VALUES (?, ?, ?, ?)
        ''', (task, amount, datetime.now().isoformat(), ai_model))
        
        conn.commit()
        conn.close()
    
    def get_earnings_summary(self) -> Dict:
        """Get earnings summary"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT SUM(amount) FROM earnings')
        total = cursor.fetchone()[0] or 0.0
        
        cursor.execute('SELECT COUNT(*) FROM earnings')
        count = cursor.fetchone()[0] or 0
        
        conn.close()
        
        return {
            'total_earned': total,
            'tasks_completed': count,
            'average_per_task': total / count if count > 0 else 0
        }
