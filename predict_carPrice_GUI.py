import customtkinter as ctk
import pandas as pd
import numpy as np
import joblib
import tkinter.messagebox as msg
from CTkMessagebox import CTkMessagebox

class AppCarPricePrediction(ctk.CTk):

    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)

        self._set_appearance_mode('light')
        self.resizable(width=False, height=False)
        self.title('Car Price Prediction')

        # ==== Load Data ==== #
        self.df = pd.read_csv('Final Project to Load/finalCarDataset.csv')

        # ==== Load ML Model ==== #
        self.model = joblib.load('Final Project to Load/random_forest_carPrice.pkl')

        # ==== Container ==== #
        self.container = ctk.CTkFrame(self)
        self.container.pack(expand= True, fill='both', ipadx= 5, ipady= 5, padx=2, pady=2)

        # ==== Row 0 ==== #
        self.row0 = ctk.CTkFrame(self.container)
        self.row0.pack(expand=True, fill='x', padx=10, pady=(10, 10), ipadx=10, ipady=10)
        self.top_label = ctk.CTkLabel(self.row0, text='Welcome to Predict Car Price', font=('XTronicRegular', 26))
        self.top_label.pack(expand=True, fill='both', pady=(10, 10))

        # ==== Row 1 ==== #
        self.row1 = ctk.CTkFrame(self.container)
        self.row1.pack(expand=True, fill='x', padx=10, pady=(0, 10), ipadx=10, ipady=10)

            # ----- Brand ----- #
        self.create_label(self.row1, text='Brand', side='left')
        self.brand_combo = self.create_combo(self.row1, items= self.all_items('Brand'), side='left', setText='Choose Brand')
            # ----- Model ----- #
        self.model_entry = self.create_text(self.row1, placeHolder='Enter Model', side='right')
        self.create_label(self.row1, text='Model', side='right')

        # ==== Row 2 ==== #
        self.row2 = ctk.CTkFrame(self.container)
        self.row2.pack(expand=True, fill='x', padx=10, pady=(0, 10), ipadx=10, ipady=10)

            # ----- Year ----- #
        self.create_label(self.row2, text='Year', side='left')
        self.year_combo = self.create_combo(self.row2, items=[str(i) for i in range(1990, 2026)], side='left', setText='Choose Year')
            # ----- Miles ----- #
        self.mile_entry = self.create_text(self.row2, placeHolder='Miles(k mile)', side='right')
        self.create_label(self.row2, text='Miles', side='right')



        # ==== Row 3 ==== #
        self.row3 = ctk.CTkFrame(self.container)
        self.row3.pack(expand=True, fill='x', padx=10, pady=(0, 10), ipadx=10, ipady=10)

            # ----- Control ----- #
        self.create_label(self.row3, text='Control', side='left')
        self.control_combo = self.create_combo(self.row3, items=self.all_items('Control'), side='left', setText='Choose Control')
            # ----- Fuel ----- #
        self.fuel_combo = self.create_combo(self.row3, items=self.all_items('Fuel'), side='right', setText='Choose Fuel')
        self.create_label(self.row3, text='Fuel', side='right')


        # ==== Row 4 ==== #
        self.row4 = ctk.CTkFrame(self.container)
        self.row4.pack(expand=True, fill='x', padx=10, pady=(0, 10), ipadx=10, ipady=10)

            # ----- Location ----- #
        self.create_label(self.row4, text='Location', side='left')
        self.location_combo = self.create_combo(self.row4, items=self.all_items('Location'), side='left', setText='Choose Location')
            # ----- EngineSize ----- #
        self.enginesize_entry = self.create_text(self.row4, placeHolder='Engine Size(L)(like 320d, 2.0T or 2.0)', side='right')
        self.create_label(self.row4, text='Engine Size', side='right')

        # ==== Row 5 ==== #
        self.row5 = ctk.CTkFrame(self.container)
        self.row5.pack(expand=True, fill='x', padx=10, pady=(0, 10), ipadx=10, ipady=10)

            # ----- Doors ----- #
        self.create_label(self.row5, text='Doors', side='left')
        self.doors_combo = self.create_combo(self.row5, items=['2', '3', '4', '5', '6'], side='left', setText='Choose Number of Doors')

            # ----- Emission ----- #
        self.emission_combo = self.create_combo(self.row5, items=self.all_items('Emission'), side='right', setText='Choose Emission')
        self.create_label(self.row5, text='Emission', side='right')

        # ==== Row 6 ==== #
        self.row6 = ctk.CTkFrame(self.container)
        self.row6.pack(expand=True, fill='x', padx=10, pady=(0, 10), ipadx=10, ipady=10)

            # ----- Predict Botton ----- #
        self.pred_botton = ctk.CTkButton(self.row6,
                                         width=350,
                                         height=50,
                                         corner_radius= 15,
                                         text='Predict Car Price',
                                         font=('XTronicRegular', 20),
                                         command=self.predict_price)
        self.pred_botton.pack(expand=True, pady=(15, 15))


    # Get unique list
    def all_items(self, itemColumn):
        item = self.df[itemColumn].unique().tolist()
        item.sort(key=lambda x: x.lower())
        return item

    def create_combo(self, root, items, side, setText):
        combo = ctk.CTkComboBox(root, values= items, width= 220, height= 30, font=('XTronicRegular', 14))
        combo.pack(side= side, padx=10, pady=10)
        combo.set(setText)
        return combo
    
    def create_text(self, root, placeHolder, side):
        text = ctk.CTkEntry(root, placeholder_text= placeHolder, width=220, height=30, font=('XTronicRegular', 14))
        text.pack(side= side, padx=10, pady=10)
        return text

    def create_label(self, root, text, side):
        self.lbl = ctk.CTkLabel(root, text= text, font=('XTronicRegular', 16))
        self.lbl.pack(side= side, padx=(10, 10))
        return self.lbl

    def predict_price(self):
        try:
            brand = self.brand_combo.get()
            model = self.model_entry.get()
            year = int(self.year_combo.get())
            miles = float(self.mile_entry.get())
            control = self.control_combo.get()
            fuel = self.fuel_combo.get()
            location = self.location_combo.get()
            engine_size = float(self.enginesize_entry.get())
            doors = int(self.doors_combo.get())
            emission = self.emission_combo.get()


            input_data = pd.DataFrame([{
                'Brand': brand,
                'Model': model,
                'Year': year,
                'Miles(k miles)': miles,
                'Control': control,
                'Fuel': fuel,
                'Location': location,
                'EngineSize': engine_size,
                'Doors': doors,
                'Emission': emission
            }])

            log_price = self.model.predict(input_data)[0]
            predicted_price = np.exp(log_price)

            CTkMessagebox(title='Predicted Price',
                          message=f'Predicted Car Price:\n {predicted_price:,.0f}£',
                          icon='check',
                          option_1='Thank',
                          corner_radius=15,
                          font=('Berlin Sans FB Demi', 25))

        except Exception as e:
            CTkMessagebox(title='Error',
                          message=f'Something went wrong:\n{e}',
                          icon='warning',
                          font=('Berlin Sans FB Demi', 25))



if __name__ == '__main__':
    app = AppCarPricePrediction()
    app.mainloop()