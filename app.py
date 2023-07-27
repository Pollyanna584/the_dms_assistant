from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
from DnDShop.TavernTreasure import generate_general_store, adjust_prices
import pandas as pd
import os
from name_generator import NameGenerator  # replace 'name_generator' with your script's name

app = Flask(__name__)

app.config['SECRET_KEY'] = 'PoXu9hYm6W96vrtEkomwX4fjAJVMteEi'  # you should use a real, secret key here

class StoreForm(FlaskForm):
    pet_percentage_low = FloatField('Pet Percentage Low:', validators=[DataRequired()], default=5)
    pet_percentage_high = FloatField('Pet Percentage High:', validators=[DataRequired()], default=10)
    magic_item_percentage_low = FloatField('Magic Item Percentage Low:', validators=[DataRequired()], default=5)
    magic_item_percentage_high = FloatField('Magic Item Percentage High:', validators=[DataRequired()], default=10)
    consumable_percentage_low = FloatField('Consumable Percentage Low:', validators=[DataRequired()], default=30)
    consumable_percentage_high = FloatField('Consumable Percentage High:', validators=[DataRequired()], default=40)
    price_adjustment_low = FloatField('Price Adjustment Low:', validators=[DataRequired()], default=5)
    price_adjustment_high = FloatField('Price Adjustment High:', validators=[DataRequired()], default=10)
    num_items_in_shop_low_percent = FloatField('Number of Items in Shop Low Percent:', validators=[DataRequired()], default=5)
    num_items_in_shop_high_percent = FloatField('Number of Items in Shop High Percent:', validators=[DataRequired()], default=10)
    submit = SubmitField('Generate')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = StoreForm()
    if form.validate_on_submit():
        # Get the range data from the form
        price_adjustment_range = (form.price_adjustment_low.data, form.price_adjustment_high.data)
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

        # Generate the store inventory
        store_inventory = generate_general_store(df_summons_pets, df_magical, df_consumables, pet_percentage_range, magic_item_percentage_range, consumable_percentage_range, price_adjustment_range, num_items_in_shop_low_percent, num_items_in_shop_high_percent)

        # Generate the store name
        try:
            generator = NameGenerator()
            title = generator.generate_random_name()
        except Exception as e:
            print(f"An error occurred: {e}")
            title = "Error in name generation"
        
        return render_template('inventory.html', store_inventory=store_inventory, title=title)
    return render_template('home.html', form=form)

# @app.route('/inventory')
# def inventory():
#     try:
#         generator = NameGenerator()
#         title = generator.generate_random_name()
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         title = "Error in name generation"
        
#     return render_template('inventory.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
