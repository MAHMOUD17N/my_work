import customtkinter as ctk

ctk.set_appearance_mode("dark")

class ModernNeonApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Neon Buttons App")
        self.geometry("950x550")           
        self.configure(fg_color="#05070c")       

        self.title_label = ctk.CTkLabel(
            self, 
            text="Neon Buttons", 
            font=ctk.CTkFont(family="Segoe UI", size=42, weight="bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(pady=50)

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=40)

        self.btn_follow = ctk.CTkButton(
            self.buttons_frame,
            text="FOLLOW BUTTON",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#39ff14",         
            fg_color="transparent",        
            border_color="#183c10",       
            border_width=2,
            corner_radius=25,             
            width=200,
            height=60,
            command=lambda: print("Followed!")
        )
        self.btn_follow.pack(side="left", padx=25)
        
        self.btn_follow.bind("<Enter>", lambda e: self.activate_neon(self.btn_follow, "#39ff14"))
        self.btn_follow.bind("<Leave>", lambda e: self.deactivate_neon(self.btn_follow, "#39ff14", "#183c10"))

        self.btn_like = ctk.CTkButton(
            self.buttons_frame,
            text="LIKE BUTTON",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#ff007f",         
            fg_color="transparent",
            border_color="#450a25",
            border_width=2,
            corner_radius=25,
            width=200,
            height=60,
            command=lambda: print("Liked!")
        )
        self.btn_like.pack(side="left", padx=25)
        
        self.btn_like.bind("<Enter>", lambda e: self.activate_neon(self.btn_like, "#ff007f"))
        self.btn_like.bind("<Leave>", lambda e: self.deactivate_neon(self.btn_like, "#ff007f", "#450a25"))

        self.btn_save = ctk.CTkButton(
            self.buttons_frame,
            text="SAVE BUTTON",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#00f3ff",          
            fg_color="transparent",
            border_color="#093845",
            border_width=2,
            corner_radius=25,
            width=200,
            height=60,
            command=lambda: print("Saved!")
        )
        self.btn_save.pack(side="left", padx=25)
        
        self.btn_save.bind("<Enter>", lambda e: self.activate_neon(self.btn_save, "#00f3ff"))
        self.btn_save.bind("<Leave>", lambda e: self.deactivate_neon(self.btn_save, "#00f3ff", "#093845"))

    def activate_neon(self, button, glow_color):
        """Activate the light and large neon glow when the mouse approaches."""
        button.configure(
            text_color="#ffffff", 
            border_color=glow_color, 
            border_width=3,            
            fg_color=glow_color       
        )

    def deactivate_neon(self, button, glow_color, base_border):
        """Turn off the light and return the button to its idle state when the mouse moves away."""
        button.configure(
            text_color=glow_color, 
            border_color=base_border, 
            border_width=2, 
            fg_color="transparent"
        )

if __name__ == "__main__":
    app = ModernNeonApp()
    app.mainloop()



# Neon button



