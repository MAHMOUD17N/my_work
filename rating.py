import customtkinter as ctk

class StarRatingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Rating Animation")
        self.geometry("400x250")
        ctk.set_appearance_mode("dark")
        
        self.current_rating = 0
        self.stars = []
        
        self.title_label = ctk.CTkLabel(
            self, 
            text="Rating Animation", 
            font=("Arial", 26, "bold"),
            text_color="white"
        )
        self.title_label.pack(pady=(40, 20))
        
        self.stars_frame = ctk.CTkFrame(self)
        self.stars_frame.pack(pady=20)
        
        for i in range(1, 6):
            star = ctk.CTkLabel(
                self.stars_frame,
                text="☆",                
                font=("Arial", 45),       
                text_color="#606060",
                cursor="hand2" 
            )
            star.pack(side="left", padx=10)
            
            star.bind("<Enter>", lambda event, idx=i: self.update_stars_visual(idx))
            star.bind("<Leave>", lambda event: self.update_stars_visual(self.current_rating))
            star.bind("<Button-1>", lambda event, idx=i: self.set_rating(idx))
            
            self.stars.append(star)

    def update_stars_visual(self, rating_value):
        for i, star in enumerate(self.stars):
            if i < rating_value:
                star.configure(text="★", text_color="#FFB800")
            else:
                star.configure(text="☆", text_color="#606060")

    def set_rating(self, rating_value):
        self.current_rating = rating_value
        self.update_stars_visual(rating_value)


if __name__ == "__main__":
    app = StarRatingApp()
    app.mainloop()

# rating
