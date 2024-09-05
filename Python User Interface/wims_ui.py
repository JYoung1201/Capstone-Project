import tkinter as tk
from tkinter import messagebox

# Sample data
products = [
    {"ProductID": 1, "ProductName": "Product A", "UnitPrice": 10.00},
    {"ProductID": 2, "ProductName": "Product B", "UnitPrice": 15.00}
]

# Create main application window
root = tk.Tk()
root.title("Warehouse Inventory Management System (WIMS)")

# Create and place widgets

# Frame for product management
frame_products = tk.Frame(root)
frame_products.pack(padx=10, pady=10)

tk.Label(frame_products, text="Product ID").grid(row=0, column=0)
tk.Label(frame_products, text="Product Name").grid(row=0, column=1)
tk.Label(frame_products, text="Unit Price").grid(row=0, column=2)

# Entry widgets for adding products
entry_id = tk.Entry(frame_products)
entry_name = tk.Entry(frame_products)
entry_price = tk.Entry(frame_products)

entry_id.grid(row=1, column=0)
entry_name.grid(row=1, column=1)
entry_price.grid(row=1, column=2)

# Add Product Button
def add_product():
    try:
        product_id = int(entry_id.get())
        product_name = entry_name.get()
        unit_price = float(entry_price.get())
        products.append({"ProductID": product_id, "ProductName": product_name, "UnitPrice": unit_price})
        messagebox.showinfo("Success", "Product added successfully!")
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid data.")

tk.Button(frame_products, text="Add Product", command=add_product).grid(row=2, column=0, columnspan=3, pady=5)

# Frame for order management
frame_orders = tk.Frame(root)
frame_orders.pack(padx=10, pady=10)

tk.Label(frame_orders, text="Order ID").grid(row=0, column=0)
tk.Label(frame_orders, text="Product ID").grid(row=0, column=1)
tk.Label(frame_orders, text="Quantity").grid(row=0, column=2)

# Entry widgets for adding orders
entry_order_id = tk.Entry(frame_orders)
entry_product_id = tk.Entry(frame_orders)
entry_quantity = tk.Entry(frame_orders)

entry_order_id.grid(row=1, column=0)
entry_product_id.grid(row=1, column=1)
entry_quantity.grid(row=1, column=2)

# Add Order Button
def add_order():
    try:
        order_id = int(entry_order_id.get())
        product_id = int(entry_product_id.get())
        quantity = int(entry_quantity.get())
        # For simplicity, no real order processing here
        messagebox.showinfo("Success", "Order added successfully!")
        entry_order_id.delete(0, tk.END)
        entry_product_id.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid data.")

tk.Button(frame_orders, text="Add Order", command=add_order).grid(row=2, column=0, columnspan=3, pady=5)

# Run the application
root.mainloop()
