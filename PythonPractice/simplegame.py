# game.py - Tkinter 2D Game with FastAPI Backend
import tkinter as tk
from tkinter import messagebox
import random
import requests
from datetime import datetime

# FastAPI Backend URL
API_URL = "http://localhost:8000"

class SpaceShooterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Shooter Game")
        self.root.geometry("800x700")
        self.root.resizable(False, False)
        
        self.user_id = None
        self.username = None
        self.score = 0
        self.game_running = False
        
        # Game objects
        self.player = None
        self.bullets = []
        self.enemies = []
        self.keys = {'Left': False, 'Right': False, 'space': False}
        
        self.show_register_screen()
    
    def show_register_screen(self):
        self.clear_screen()
        
        # Registration Frame
        reg_frame = tk.Frame(self.root, bg="#1a1a2e")
        reg_frame.pack(expand=True, fill='both')
        
        tk.Label(reg_frame, text="🚀 SPACE SHOOTER 🚀", 
                font=("Arial", 32, "bold"), fg="#00ff00", bg="#1a1a2e").pack(pady=30)
        
        # Username
        tk.Label(reg_frame, text="Username:", 
                font=("Arial", 14), fg="white", bg="#1a1a2e").pack(pady=5)
        self.username_entry = tk.Entry(reg_frame, font=("Arial", 14), width=30)
        self.username_entry.pack(pady=5)
        
        # Email
        tk.Label(reg_frame, text="Email:", 
                font=("Arial", 14), fg="white", bg="#1a1a2e").pack(pady=5)
        self.email_entry = tk.Entry(reg_frame, font=("Arial", 14), width=30)
        self.email_entry.pack(pady=5)
        
        # Register Button
        register_btn = tk.Button(reg_frame, text="START GAME", 
                                font=("Arial", 16, "bold"),
                                bg="#00ff00", fg="black",
                                command=self.register_user,
                                padx=20, pady=10)
        register_btn.pack(pady=30)
        
        self.reg_frame = reg_frame
    
    def register_user(self):
        username = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        
        if not username or not email:
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        try:
            # Call FastAPI backend
            response = requests.post(f"{API_URL}/api/users", 
                                    json={"username": username, "email": email},
                                    timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.user_id = data['id']
                self.username = username
                self.start_game()
            else:
                messagebox.showerror("Error", "Registration failed!")
        except requests.exceptions.ConnectionError:
            # If backend is not running, use mock data
            messagebox.showwarning("Backend Offline", 
                                  "Backend not running. Using offline mode.")
            self.user_id = random.randint(1000, 9999)
            self.username = username
            self.start_game()
        except Exception as e:
            messagebox.showerror("Error", f"Registration error: {str(e)}")
    
    def start_game(self):
        self.clear_screen()
        self.score = 0
        self.game_running = True
        
        # Game UI
        self.game_frame = tk.Frame(self.root, bg="#0a0a0a")
        self.game_frame.pack(expand=True, fill='both')
        
        # Score Label
        self.score_label = tk.Label(self.game_frame, 
                                   text=f"Player: {self.username} | Score: {self.score}",
                                   font=("Arial", 14), fg="white", bg="#0a0a0a")
        self.score_label.pack(pady=5)
        
        # Canvas
        self.canvas = tk.Canvas(self.game_frame, width=800, height=600, 
                               bg="#000033", highlightthickness=0)
        self.canvas.pack()
        
        # Instructions
        tk.Label(self.game_frame, text="← → Arrow Keys to Move | SPACE to Shoot",
                font=("Arial", 12), fg="#888888", bg="#0a0a0a").pack(pady=5)
        
        # Initialize game objects
        self.player = {
            'x': 380, 'y': 550, 'width': 40, 'height': 40,
            'rect': self.canvas.create_rectangle(380, 550, 420, 590, fill="lime")
        }
        
        # Draw player ship details
        self.canvas.create_rectangle(385, 540, 395, 550, fill="green")
        self.canvas.create_rectangle(405, 540, 415, 550, fill="green")
        
        self.bullets = []
        self.enemies = []
        
        # Bind keys
        self.root.bind('<KeyPress>', self.key_press)
        self.root.bind('<KeyRelease>', self.key_release)
        
        # Start game loop
        self.game_loop()
        self.spawn_enemy()
    
    def key_press(self, event):
        if event.keysym in self.keys:
            self.keys[event.keysym] = True
    
    def key_release(self, event):
        if event.keysym in self.keys:
            self.keys[event.keysym] = False
    
    def game_loop(self):
        if not self.game_running:
            return
        
        # Move player
        if self.keys['Left'] and self.player['x'] > 0:
            self.player['x'] -= 7
            self.canvas.move(self.player['rect'], -7, 0)
        if self.keys['Right'] and self.player['x'] < 760:
            self.player['x'] += 7
            self.canvas.move(self.player['rect'], 7, 0)
        
        # Shoot bullets
        if self.keys['space']:
            self.shoot_bullet()
        
        # Move bullets
        for bullet in self.bullets[:]:
            bullet['y'] -= 10
            self.canvas.move(bullet['rect'], 0, -10)
            if bullet['y'] < 0:
                self.canvas.delete(bullet['rect'])
                self.bullets.remove(bullet)
        
        # Move enemies
        for enemy in self.enemies[:]:
            enemy['y'] += enemy['speed']
            self.canvas.move(enemy['rect'], 0, enemy['speed'])
            
            # Check collision with player
            if self.check_collision(self.player, enemy):
                self.game_over()
                return
            
            # Check collision with bullets
            for bullet in self.bullets[:]:
                if self.check_collision(bullet, enemy):
                    self.canvas.delete(bullet['rect'])
                    self.canvas.delete(enemy['rect'])
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10
                    self.score_label.config(
                        text=f"Player: {self.username} | Score: {self.score}"
                    )
                    break
            
            # Remove enemies that went off screen
            if enemy['y'] > 600:
                self.canvas.delete(enemy['rect'])
                self.enemies.remove(enemy)
        
        self.root.after(30, self.game_loop)
    
    def shoot_bullet(self):
        if len(self.bullets) < 5:  # Limit bullets
            bullet = {
                'x': self.player['x'] + 18,
                'y': self.player['y'],
                'width': 4,
                'height': 15,
                'rect': self.canvas.create_rectangle(
                    self.player['x'] + 18, self.player['y'],
                    self.player['x'] + 22, self.player['y'] - 15,
                    fill="yellow"
                )
            }
            self.bullets.append(bullet)
    
    def spawn_enemy(self):
        if not self.game_running:
            return
        
        x = random.randint(0, 760)
        enemy = {
            'x': x, 'y': 0, 'width': 40, 'height': 40,
            'speed': random.randint(2, 5),
            'rect': self.canvas.create_rectangle(x, 0, x+40, 40, fill="red")
        }
        self.enemies.append(enemy)
        
        # Spawn next enemy
        self.root.after(random.randint(800, 1500), self.spawn_enemy)
    
    def check_collision(self, obj1, obj2):
        return (obj1['x'] < obj2['x'] + obj2['width'] and
                obj1['x'] + obj1['width'] > obj2['x'] and
                obj1['y'] < obj2['y'] + obj2['height'] and
                obj1['y'] + obj1['height'] > obj2['y'])
    
    def game_over(self):
        self.game_running = False
        
        # Save score to backend
        try:
            requests.post(f"{API_URL}/api/scores",
                         json={"user_id": self.user_id, "score": self.score},
                         timeout=5)
        except:
            pass  # Ignore if backend is offline
        
        self.clear_screen()
        
        # Game Over Screen
        over_frame = tk.Frame(self.root, bg="#1a1a2e")
        over_frame.pack(expand=True, fill='both')
        
        tk.Label(over_frame, text="💥 GAME OVER 💥", 
                font=("Arial", 40, "bold"), fg="#ff0000", bg="#1a1a2e").pack(pady=30)
        
        tk.Label(over_frame, text=f"Final Score: {self.score}", 
                font=("Arial", 24), fg="#ffff00", bg="#1a1a2e").pack(pady=10)
        
        tk.Label(over_frame, text=f"Player: {self.username}", 
                font=("Arial", 18), fg="white", bg="#1a1a2e").pack(pady=5)
        
        # Play Again Button
        play_again_btn = tk.Button(over_frame, text="PLAY AGAIN", 
                                   font=("Arial", 16, "bold"),
                                   bg="#00ff00", fg="black",
                                   command=self.start_game,
                                   padx=20, pady=10)
        play_again_btn.pack(pady=20)
        
        # Exit Button
        exit_btn = tk.Button(over_frame, text="EXIT", 
                            font=("Arial", 14),
                            bg="#ff0000", fg="white",
                            command=self.root.quit,
                            padx=20, pady=8)
        exit_btn.pack(pady=10)
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceShooterGame(root)
    root.mainloop()