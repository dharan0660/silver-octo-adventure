
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Cigarette Store Data
store_items = {
    "Marlboro": {"price": 10, "stock": 50, "image": "marlboro.png"},
    "Camel": {"price": 8, "stock": 40, "image": "camel.png"},
    "Winston": {"price": 9, "stock": 30, "image": "winston.png"},
    "Lucky Strike": {"price": 11, "stock": 20, "image": "lucky_strike.png"}
}

# Shopping Cart
cart = {}

# Helper Functions
def add_to_cart(item_name):
    if store_items[item_name]["stock"] > 0:
        cart[item_name] = cart.get(item_name, 0) + 1
        store_items[item_name]["stock"] -= 1
        update_cart_display()
    else:
        messagebox.showinfo("Out of Stock", f"{item_name} is out of stock.")

def update_cart_display():
    cart_text.set("\n".join([f"{item}: {qty}" for item, qty in cart.items()]))
    total_price = sum(store_items[item]["price"] * qty for item, qty in cart.items())
    total_text.set(f"Total: ${total_price}")

def checkout():
    if cart:
        receipt = "\n".join([f"{item}: {qty} @ ${store_items[item]['price']} each" for item, qty in cart.items()])
        total_price = sum(store_items[item]["price"] * qty for item, qty in cart.items())
        receipt += f"\n\nTotal: ${total_price}"
        messagebox.showinfo("Receipt", receipt)
        cart.clear()
        update_cart_display()
    else:
        messagebox.showinfo("Checkout", "Your cart is empty!")

# GUI Setup
root = tk.Tk()
root.title("Cigarette Store")

cart_text = tk.StringVar()
total_text = tk.StringVar(value="Total: $0")

# Store Items Display
frame_items = tk.Frame(root)
frame_items.pack(side=tk.LEFT, padx=10, pady=10)

for item_name, item_data in store_items.items():
    item_frame = tk.Frame(frame_items, relief=tk.RAISED, borderwidth=1)
    item_frame.pack(padx=5, pady=5, fill=tk.X)

    try:
        img = Image.open(item_data["image"])
        img = img.resize((50, 50))
        photo = ImageTk.PhotoImage(img)
        label_img = tk.Label(item_frame, image=photo)
        label_img.image = photo  # Keep a reference to avoid garbage collection
        label_img.pack(side=tk.LEFT, padx=5)
    except Exception as e:
        tk.Label(item_frame, text="[Image not found]").pack(side=tk.LEFT, padx=5)

    tk.Label(item_frame, text=f"{item_name} - ${item_data['price']}").pack(side=tk.LEFT, padx=5)
    tk.Button(item_frame, text="Add to Cart", command=lambda name=item_name: add_to_cart(name)).pack(side=tk.RIGHT, padx=5)

# Cart Display
frame_cart = tk.Frame(root)
frame_cart.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Label(frame_cart, text="Shopping Cart").pack()
cart_display = tk.Label(frame_cart, textvariable=cart_text, justify=tk.LEFT)
cart_display.pack()

tk.Label(frame_cart, textvariable=total_text).pack(pady=5)
tk.Button(frame_cart, text="Checkout", command=checkout).pack(pady=5)

root.mainloop()
