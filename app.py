from flask import Flask, render_template, session, make_response, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from DnDShop.TavernTreasure import generate_general_store, adjust_prices
import pandas as pd
import os
import csv
import io
from name_generator import NameGenerator #Shop Name Generator
from Shopkeeper.shopkeeper_name import ShopkeeperGenerator

app = Flask(__name__)

app.config['SECRET_KEY'] = 'PoXu9hYm6W96vrtEkomwX4fjAJVMteEi'  # you should use a real, secret key here

class StoreForm(FlaskForm):
    pet_percentage_low = FloatField('Pet Percentage - Low:', validators=[DataRequired()], default=3)
    pet_percentage_high = FloatField('Pet Percentage - High:', validators=[DataRequired()], default=5)
    magic_item_percentage_low = FloatField('Magic Item Percentage - Low:', validators=[DataRequired()], default=5)
    magic_item_percentage_high = FloatField('Magic Item Percentage - High:', validators=[DataRequired()], default=10)
    consumable_percentage_low = FloatField('Consumable Percentage - Low:', validators=[DataRequired()], default=30)
    consumable_percentage_high = FloatField('Consumable Percentage - High:', validators=[DataRequired()], default=40)
    price_adjustment_low = FloatField('Discount Percentage - Low:', validators=[NumberRange(min=-100, max=100)], default=-10)
    price_adjustment_high = FloatField('Discount Percentage - High:', validators=[NumberRange(min=-100, max=100)], default=0)
    num_items_in_shop_low_percent = FloatField('Number of Items in Shop - Low Percent:', validators=[DataRequired()], default=5)
    num_items_in_shop_high_percent = FloatField('Number of Items in Shop - High Percent:', validators=[DataRequired()], default=10)
    submit = SubmitField('Generate')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = StoreForm()
    if form.validate_on_submit():
        # Get the range data from the form
        price_adjustment_low = 100 + form.price_adjustment_low.data
        price_adjustment_high = 100 + form.price_adjustment_high.data
        price_adjustment_range = (price_adjustment_low, price_adjustment_high)
        pet_percentage_range = (form.pet_percentage_low.data, form.pet_percentage_high.data)
        magic_item_percentage_range = (form.magic_item_percentage_low.data, form.magic_item_percentage_high.data)
        consumable_percentage_range = (form.consumable_percentage_low.data, form.consumable_percentage_high.data)
        num_items_in_shop_range = (form.num_items_in_shop_low_percent.data, form.num_items_in_shop_high_percent.data)

        # unpack num_items_in_shop_range into separate variables
        num_items_in_shop_low_percent, num_items_in_shop_high_percent = num_items_in_shop_range

        # Load and process CSV files
        data_dir = os.path.dirname(os.path.realpath(__file__))
        df_magical = pd.read_csv(f'{data_dir}/DnDShop/Items/magic_items.csv').dropna(subset=['Name'])
        df_summons_pets = pd.read_csv(f'{data_dir}/DnDShop/Items/summons_pets.csv').dropna(subset=['Name'])
        df_consumables = pd.read_csv(f'{data_dir}/DnDShop/Items/consumable_items.csv').dropna(subset=['Name'])

        df_magical['Price'] = pd.to_numeric(df_magical['Price'], errors='coerce')
        df_summons_pets['Price'] = pd.to_numeric(df_summons_pets['Price'], errors='coerce')
        df_consumables['Price'] = pd.to_numeric(df_consumables['Price'], errors='coerce')

        df_magical = adjust_prices(df_magical, price_adjustment_range)
        df_summons_pets = adjust_prices(df_summons_pets, price_adjustment_range)
        df_consumables = adjust_prices(df_consumables, price_adjustment_range)

        # Generate the store name and the shopkeeper
        try:
            generator = NameGenerator()
            store_title = generator.generate_random_name()
            shopkeeper_generator = ShopkeeperGenerator()
            shopkeeper = shopkeeper_generator.generate_shopkeeper()  # generate a shopkeeper
        except Exception as e:
            print(f"An error occurred: {e}")
            store_title = "Error in name generation"
            shopkeeper = {"Name": "Error", "Race": "Error", "Voice": "Error"}

        # Generate the store inventory
        store_inventory = generate_general_store(df_summons_pets, df_magical, df_consumables, pet_percentage_range, magic_item_percentage_range, consumable_percentage_range, price_adjustment_range, num_items_in_shop_low_percent, num_items_in_shop_high_percent)

        session['store_inventory'] = [(item_name, item_price) for item_name, item_price in store_inventory]
        session['store_title'] = store_title
        session['shopkeeper'] = shopkeeper  # store the shopkeeper details in the session
        
        return redirect(url_for('inventory'))  # redirect to the inventory route
    return render_template('home.html', form=form)

@app.route('/inventory')
def inventory():
    store_inventory = session.get('store_inventory', [])
    store_title = session.get('store_title', "Default Store Name")
    shopkeeper = session.get('shopkeeper', {"Name": "Default", "Race": "Default", "Voice": "Default"})  # get the shopkeeper details from the session
    
    # Convert inventory to list of dictionaries for the template
    store_inventory_dicts = [{"Item Name": item[0], "Item Price": item[1]} for item in store_inventory]
    return render_template('inventory.html', store_inventory=store_inventory_dicts, shopkeeper=shopkeeper, store_title=store_title)



@app.route('/download')
def download():
    # Get store inventory and title from the session
    store_inventory = session.get('store_inventory', [])
    store_title = session.get('store_title', "Default Store Name")
    shopkeeper = session.get('shopkeeper', {"Name": "Default", "Race": "Default", "Voice": "Default"})

    # Convert the inventory to a CSV
    si_csv = io.StringIO()
    writer = csv.writer(si_csv)
    writer.writerow(['Shopkeeper Name', shopkeeper["Name"]])
    writer.writerow(['Shopkeeper Race', shopkeeper["Race"]])
    writer.writerow(['Shopkeeper Voice', shopkeeper["Voice"]])
    writer.writerow([])  # Optional empty row for separation
    writer.writerow(['Item Name', 'Item Price'])

    for item in store_inventory:
        writer.writerow([item[0], item[1]])  # Each item is a tuple (name, price)
    
    # Create the response
    output = make_response(si_csv.getvalue())
    output.headers["Content-Disposition"] = f"attachment; filename={store_title.replace(' ', '_')}.csv"
    output.headers["Content-type"] = "text/csv"
    return output



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1738, debug=True)


