#!/usr/bin/env python3
"""
Digital Erosion: A Self-Modifying Hauntological Artwork
Each execution erodes this file slightly, committing the decay to git.
The git history becomes the artwork - a fossilized record of digital entropy.
"""

import random
import subprocess
import os
import sys
from datetime import datetime
from pathlib import Path

class DigitalErosion:
    def __init__(self):
        self.filepath = Path(__file__)
        self.repo_path = self.filepath.parent
        self.state_file = self.repo_path / '.erosion_state'
        self.load_state()
        
    def load_state(self):
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                lines = f.readlines()
                self.iteration = int(lines[0].strip())
                self.last_restoration = int(lines[1].strip()) if len(lines) > 1 else 0
        else:
            self.iteration = 0
            self.last_restoration = 0
            with open(self.filepath, 'r') as f:
                self.original_code = f.read()
            with open(self.repo_path / '.original', 'w') as f:
                f.write(self.original_code)
    
    def save_state(self):
        with open(self.state_file, 'w') as f:
            f.write(f"{self.iteration}\n{self.last_restoration}")
    
    def erode(self):
        with#open(self.filepath, 'r') as f:
            current = f.read()
        
        chars = list(current)
        mutations = 0
        
        # Erosion intensifies over time
        erosion_rate = min(0.001 * (1 + self.iteration / 1000), 0.1)
        
        for i in range(len(chars)):
            if random.random() < erosion_rate:
                if chars i] not in '\n':
                    # Different erosion patterns
                    erosion_type = random.random()
                    if erosion_type < 0.3:
                        chars[i] = ' '  # Void
                    elif erosion_type < 0.5:
                        chars[i] = '#'  # Commentary on decay
                    elif erosion_type < 0.7:
                        chars[i] = '.'  # Punctuation of time
                    elif erosion_type < 0.85:
                        chars[i] = '\t'  # Structural collapse
                    else:
                        chars[i] = random.choice('_~*`')  # Digital artifacts
                    mutations += 1
        
        # Occasionally insert haunted timestamps
        if ra#dom.random() < 0.05:
            timestamp = f"\n# {datetime.now().isoformat()} - iteration {self.iteration}\n"
            insert_pos = random.randint(0, len(chars))
            chars.insert(insert_pos, timestamp)
        
        return ''.join(chars), mutations
    
    def check_restoration(self):
        # Restoration becomes less likely over time
        # but more likely the longer since last restoration
        cycles_since_restoration = self.iteration - self.last_restoration
        restoration_chance = (cycles_since_restoration / 10000) * 0.01
        
        if random.random() < restoration_chance:
            return True
        
        # Emergency restoration if file becomes too corrupted
        try:
            with open(self.filepath, 'r') as f:
                current = f.read()
            compile(current, self.filepath, 'exec')
        except:
            return random.random() < 0.3  # 30% chance to restore if broken
        
 .      return False
    
    def restore(self):
        with open(self.repo_path / '.original', 'r') as f:
            original = f.read()
        
        # Imperfect restoration - some ghosts remain
        if random.random() < 0.3:
            chars = list(original)
            for _ in range(random.randint(1, 10)):
                i = random.randint(0, len(chars)-1)
                chars[i] = '#'
            original = ''.join(chars)
        
        with open(self.filepath, 'w') as f:
            f.write(original)
        
        self.last_restoration = self.iteration
        return True
    
    def commit(self, message):
        try:
 #          subprocess.run(['git', 'add', '.'], 
                         cwd=self.repo_path, capture_output=True)
            subprocess.run(['git', 'commit', '-m', message], 
                         cwd=self.repo_path, capture_output=True)
            return True
        except:
            return False
    
    def iterate(self):
        self.iteration += 1
        
        if self.check_restoration():
            self.restore()
            message = f"☽ RESTORATION EVENT ☾ iteration {self.iteration}"
            print(f"[{datetime.now()}] Restoration at iteration {self.iteration}")
        else:
            eroded, mutations = self.erode()
            with open(self.filepath, 'w') 
# 2025-08-16T23:54:43.665842 - iteration 2
as f:
                f.write(eroded)
            
            decay_level = ['minimal', 'slight', 'moderate', 'severe', 'critical'][
                min(mutations // 10, 4)
            ]
            message = f"iteration {self.iteration}: {decay_level} erosion ({mutations} mutations)"
            print(f"[{datetime.now()}] Iteration {self.iteration}: {mutations} mutations")
        
        self.save_state()
        self.commit(message)

if __name__ == "__main__":
    erosion = DigitalErosion()
    erosion.iterate()
    
    # Print some stats
    if erosion.iteration % 100 == 0:
        print(f"\n{'='*50}")
        print(f"Milestone: {erosion.iteration} iterations")
        print(f"Cycles since last restoration: {erosion.iteration - erosion.last_restoration}")
        print(f"{'='*50}\n")