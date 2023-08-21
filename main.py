import tkinter as tk
from tkinter import ttk, messagebox

class ShoppingListApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Shopping List")
    
        self.shopping_list = []
        
        self.product_name_var = tk.StringVar()
        self.product_quantity_var = tk.StringVar()
        self.product_quantity_unit_var = tk.StringVar()
        self.product_price_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        # Label and entry for product name
        product_name = tk.Label(self.root, text="Product Name:")
        product_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.product_name_entry = tk.Entry(self.root, textvariable=self.product_name_var)
        self.product_name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Label and entry for quantity
        product_quantity = tk.Label(self.root, text="Quantity:")
        product_quantity.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.product_quantity_entry = tk.Entry(self.root, textvariable=self.product_quantity_var)
        self.product_quantity_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Combobox for quantity unit
        self.unit_options = ["kg", "liters", "pieces"]
        
        self.product_quantity_unit_combobox = ttk.Combobox(self.root, values=self.unit_options, textvariable=self.product_quantity_unit_var, width=6)
        self.product_quantity_unit_combobox.grid(row=1, column=2, padx=10, pady=5)
        self.product_quantity_unit_combobox.set("pieces")

        # Label and entry for price
        product_price = tk.Label(self.root, text="Price :")
        product_price.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.product_price_entry = tk.Entry(self.root, textvariable=self.product_price_var)
        self.product_price_entry.grid(row=2, column=1, padx=10, pady=5)

        # Button for adding the product
        self.add_button = tk.Button(self.root, text="Add", command=self.add_product)
        self.add_button.grid(row=3, columnspan=3, padx=15, pady=15)

        # Button for deleting the product
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_product)
        self.delete_button.grid(row=3, column=1, columnspan=3, padx=15, pady=15)

        # Listbox for displaying products
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.grid(row=4, columnspan=3, padx=10, pady=5)
        
        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(self.root, command=self.listbox.yview)
        scrollbar.grid(row=4, column=3, sticky="ns")
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # Label for displaying total price
        self.total_label = tk.Label(self.root, text="Total Price: 0")
        self.total_label.grid(row=6, columnspan=3, padx=10, pady=5)

    def add_product(self):
        # Extract user input information
        product_name = self.product_name_var.get().strip().capitalize()
        product_quantity = self.product_quantity_var.get().strip()
        product_quantity_unit = self.product_quantity_unit_var.get() 
        product_price_per_unit = self.product_price_var.get().strip().replace(",", ".")  
        
        # Calculate total price for the product
        total_price = int(product_quantity) * float(product_price_per_unit)
        
        # Add product details to the listbox and shopping list
        self.listbox.insert(tk.END, f"{product_name} - {product_quantity} {product_quantity_unit}, Total Price: {total_price:.2f} lei")
        self.shopping_list.append(total_price)
         
        # Update displayed total price
        self.update_total()

    def update_total(self):
        # Calculate the sum of prices in the shopping list
        total = sum(self.shopping_list)
        self.total_label.config(text=f"Total Price: {total:.2f} lei")

    def delete_product(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            # Remove the price of the deleted product from the shopping list and update the listbox
            removed_price = self.shopping_list.pop(index)
            self.listbox.delete(index)
            # Update displayed total price
            self.update_total()
        else: 
            messagebox.showwarning("Warning", "Select a product to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingListApp(root)
    root.mainloop()
